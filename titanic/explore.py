import os
from os.path import join, splitext, exists, abspath, basename

import pandas as pd
import pdb
import ggplot as ggp

import utils

log = utils.makeLogger('titanic-data-exploration')

# Load dataframe
DFN = abspath(join(os.curdir, os.pardir, 'datasets', 'titanic-train.csv'))
df = pd.read_csv(DFN)
log.debug("{} has columns: {}".format(basename(DFN), df.columns.tolist()))

# Plot exploratory data analysis
log.debug("Plotting exploratory slices")
pt = ggp.ggplot(ggp.aes(x='Sex', fill='Survived'), data=df) + \
             ggp.geom_bar()
# NOTE type "pt" into the debugger to show the plot

pdb.set_trace()
