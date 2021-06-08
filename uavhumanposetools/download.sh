#!/bin/bash
pip install gdown

if [ ! -d $1 ]; then
    mkdir -p $1
fi

gdown TRAIN_LINK
unzip skeleton_action_recognition_train_split.zip -d $1/
rm skeleton_action_recognition_train_split.zip

gdown TEST_LINK
unzip skeleton_action_recognition_test_split.zip -d $1/
rm skeleton_action_recognition_test_split.zip
