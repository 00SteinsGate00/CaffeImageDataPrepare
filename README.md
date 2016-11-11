# Caffe Image Datbase Prepare

When you download image datasets from the internet, they often come seperated into folders per class.

[Caffe](http://caffe.berkeleyvision.org) requires you to input the files as one text file, containing the path to the image and the class label (as a number).

This script creates such a file from an image database folder, generating class numbers.

It is even able to split up the images between **training** and **test set** by an arbitrary **ratio**.

## Data

The directory structure of your database should be like this

```
Database
	|- Class_1
		|- Image_1
		|- Image_2
			...
			
	|- Class_2
		|- Image_1
		|- Image_2
		|- Image_3
			...
	...
```

## Usage

The command line interface is simple

```
caffe_image_prep <database directory> [options]
```

This will generate a file called `output.txt` containing the path to every image together with its class label.

### Options

|   Option  | Short Version |  Value | Default    |                                          Meaning                                         |
|:---------:|:-------------:|:------:|------------|:----------------------------------------------------------------------------------------:|
|  --train  |       -t      | string | output.txt | The output file for the training set                                                     |
|   --test  |       -T      | string |   *none*   | The output file for the test set                                                         |
|  --table  |      -ta      | string |   *none*   | File listing the class tables along with the classnames                                  |
|  --ration |       -r      |  float |     0.8    | The ration to between training and test set images. Must be between 0 and 1.             |
| --verbose |       -v      |   int  |      1     | The amount of verbosity. 0 = silent, 1 = output summary (default), 2 = processing output |


## Examples

The following will store the path, along with the class label for every image in the `101_ObjectCategories` directoy into `output.txt``

```
caffe_image_prep 101_ObjectCategories
```
The following will split the images into a *training* and a *test set* by a ration of **0.75** (75% traning, 25% test). The output will be stored in the files `data_training.txt` and `data_test.txt` repectively.

```
caffe_image_prep 101_ObjectCategories --train data_train.txt --test data_test.txt --ration 0.75
```

The following will output both a *training* and a *test set* with the default split ration of **0.8**. Furthermore it will create a table file `data_table.txt` listing the class labels (numbers between 0 and n) together with the class names (derived from the foldernames).

```
caffe_image_prep 101_ObjectCategories --train data_train.txt --test data_test.txt --table data_table.txt
```


## Install 

[Download](https://github.com/00SteinsGate00/KodiTVShowNamer/archive/master.zip) the repository or clone it using

```
git clone https://github.com/00SteinsGate00/KodiTVShowNamer.git
```

Follow the script to some place inside your `$PATH`, for example `/usr/bin` and set the correct permissions.

```
sudo cp caffe_image_prepare.py /usr/bin/caffe_image_prep
sudo chmod +x /usr/bin/caffe_image_prep
```

## Licence

[MIT Licence](LICENCE.md)

