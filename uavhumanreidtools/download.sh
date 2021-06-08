#!/bin/bash
pip install gdown

if [ ! -d $1 ]; then
    mkdir -p $1
fi

gdown TRAIN_LINK
unzip reid_bounding_box_train.zip -d $1/
rm reid_bounding_box_train.zip

gdown TEST_LINK
unzip reid_bounding_box_test_and_query_splits.zip -d $1/
rm reid_bounding_box_test_and_query_splits.zip
