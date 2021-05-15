#!/bin/bash
UAVHumanPath=$(dirname $(pwd))
pip install gdown
gdown https://drive.google.com/uc?id=1g5LWFyWtPnuBsw-0YYg7RgbqDxckjjbk
tar -xvf sutd_rgb+d_skeletons.tar.gz -C $UAVHumanPath/
rm sutd_rgb+d_skeletons.tar.gz