import argparse


# ################ #
# Argument Parsing #
# ################ #

description = """Caffe Image Database Preparation

A tool that takes a path to a directory containing directories of images,
each representing a single class.
It will produce outputfiles containg the image path and the class label as a number
between 0 and #classes."""

parser = argparse.ArgumentParser()
parser.add_argument("data", help="Directory with the image data")
parser.add_argument("-t", "--train", help="The outputfile for the training set")
parser.add_argument("-T", "--test", help="The outputfile for the test set")
parser.add_argument("-r", "--ratio", help="Ration to split between training and test set. Default is 0.8")
parser.parse_args()
