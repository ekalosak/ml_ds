import os
from os.path import join, exists, splitext
import sys
import random
import math
import pdb
import numpy as np
import pandas as pd
import scipy.stats as stats
from itertools import chain, combinations

ROOT = 'root'
TRAINDATA = join(os.pardir, 'datasets', 'titanic-train.csv')

# http://www.pythonschool.net/data-structures-algorithms/binary-tree/
class BinaryTree(object):

    ''' parent must be ROOT or BinaryTree, childs must be None or BT,
    value can be anything '''

    def __init__(self, parent, value = None, left = None, right = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.update()

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self, value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
    def setRightChild(self, r):
        self.right = r
        self.update()
    def setLeftChild(self, l):
        self.left = l
        self.update()
    def getChildren(self):
        return self.children
    def getParent(self):
        return self.parent

    def getRoot(self):
        p = self
        if p.parent == ROOT:
            return p
        else:
            while p.parent != ROOT:
                p = p.parent
        return p

    def train(self, response_variable):
        df = self.df

        print "training only on categorical variables now"
        categ_col = df.columns[(df.dtypes == object).tolist()].tolist()
        if response_variable in categ_col:
            categ_col.remove(response_variable)
        rf = df[response_variable]
        cf = df[categ_col]

        print "removing categorical columns with too many categories"
        for col in cf.columns:
            if len(np.unique(cf[col])) > len(cf)/2:
                del cf[col]
                categ_col.remove(col)

        for col in categ_col:
            ccf = cf[col]
            categs = np.unique(ccf.values)
            pos_splits = [x for x in self.powerset(categs) if
                    len(x) > 0 and len(x) < len(categs)]

            # TODO
            ''' continue here
            find splits with maximal information gain using stats.entropy
            select the split with the highest information gain
                as the next decision split'''
            pdb.set_trace()

    def powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    def update(self):
        self.children = self.right, self.left
        self.validate()

    def validate(self):
        for c in self.children:
            if c is not None:
                assert type(c) == BinaryTree
        assert self.parent == ROOT or type(self.parent) == BinaryTree

class DecisionTree(BinaryTree):

    def import_data(self, datadir):
        self.df = pd.read_csv(datadir)
        self.dimensions = self.df.columns.tolist()

    def getData(self):
        return self.df

    def validate(self):
        BinaryTree.validate(self)
    def update(self):
        BinaryTree.update(self)


def test():
    # BinaryTree tests
    bt = BinaryTree(ROOT)
    rc = BinaryTree(bt)
    bt.setRightChild(rc)
    assert bt.getRightChild() == rc
    assert rc in bt.getChildren()

    # DecisionTree tests
    dt = DecisionTree(ROOT)
    dt.import_data(TRAINDATA)
    assert dt.getRoot() == dt
    assert dt.getParent() == ROOT

    print 'Passed tests!!'
    return bt, dt

def main(stuff):
    # Train a decision tree on the titanic-train.csv dataset
    #   This will be a classification tree

    dt = stuff[1]
    response = 'Survived'
    dt.train(response)

    pdb.set_trace()

if __name__ == '__main__':
    stuff = test()
    main(stuff)
