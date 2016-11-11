#!/usr/bin/env python

import argparse
import os
import sys

# ###### #
# Config #
# ###### #

# directory containing the images
data_path = None

# output file for the training data
train_output = "output.txt"

# output file for the test data
test_output = None

# ratio to split traning and test set
ratio = 0.8



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
arguments = parser.parse_args()



# ##################### #
# Argument Verification #
# ##################### #

# Dir containing the image data
data_path = os.path.abspath(arguments.data)

# check if the database path exists
if(not os.path.exists(data_path)):
    print ("Cannot find '%s'" % data_path)
    sys.exit()

# check if the database path is a directory
if(not os.path.isdir(data_path)):
    print ("Data path '%s' is not a directory" % data_path)
    sys.exit()

# set training output
if(arguments.train):
    train_output = os.path.abspath(arguments.train)
else:
    train_output = os.path.abspath(train_output)

# set test output
if(arguments.test):
    test_output = os.path.abspath(arguments.test)

# split ratio
if(arguments.ratio):
    try:
        # cast to float
        tmp_ratio = float(arguments.ratio)
        # check boundaries (0 to 1)
        if(tmp_ratio >= 0 and tmp_ratio <= 1):
            ratio = tmp_ratio
        else:
            print ("'%s' is not a floating point number between 0 and 1" % arguments.ratio)
            sys.exit()
    # no float value
    except ValueError:
        print ("'%s' is not a floating point number between 0 and 1" % arguments.ratio)
        sys.exit()



# ############### #
# Data Processing #
# ############### #

# open the files in write mode

train_file = open(train_output, 'w')

if(test_output):
    test_file = open(test_output, 'w')

class_label = 0
count = 0

# iterate through the whole data directory
for class_folder in os.listdir(data_path):

    # build the absolute path for the class directory
    class_dir = "%s/%s" % (data_path, class_folder)

    # check if it is a directory
    if(os.path.isdir(class_dir)):

        # process every image
        for image in os.listdir(class_dir):

            # check if a test file is desired
            if(test_output):

                # check wether the current image belongs to training or test set
                # training set
                if(count <= ratio * len(images)):
                    train_file.write("%s/%s %d\n" % (class_dir, image, class_label))
                # test set
                else:
                    test_file.write("%s/%s %d\n" % (class_dir, image, class_label))

                # increment the count variable
                count += 1

            # no test output
            # put every file in the training set
            else:
                train_file.write("%s/%s %d\n" % (class_dir, image, class_label))

        # increment the class label
        class_label += 1
        # reset count
        count = 0


# close the files
train_file.close()
if(test_output):
    test_file.close()
