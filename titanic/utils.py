import logging
import matplotlib.pyplot as plt
import os
from os.path        import join, exists, splitext

def addtopdf(img, txt, pdf, bw=False, spec=False, specC=False):

    fig = plt.figure()
    fig.suptitle(txt)
    plt.axis('off')

    if bw: plt.imshow(img, cmap="gray")
    elif spec: plt.imshow(img, cmap=plt.cm.gray)
    elif specC: plt.imshow(img, cmap=plt.cm.spectral)
    else: plt.imshow(img)

    pdf.savefig()
    plt.close()

def makeLogger(name, dr=os.curdir, verbose=True):
    """ make a logger with name <name> in directory
    <dir>. If <verbose>, set commandline out for debug"""

    # Setup the log object, handles log.debug() etc
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)s\
        %(message)s')

    # Setup file output
    fileHandlerPath = join(dr, "%s.log" % name)
    fileHandler = logging.FileHandler(fileHandlerPath)
    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(logging.INFO)

    # Setup console output
    if verbose:
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(formatter)
        consoleHandler.setLevel(logging.DEBUG)

    # Add the handlers to the logger
    log.addHandler(fileHandler)
    if verbose: log.addHandler(consoleHandler)

    return log

if __name__ == '__main__':
    print "This is not a commandline utility"
