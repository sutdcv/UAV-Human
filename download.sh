#!/bin/bash
UAVHumanPath=$(pwd)
curl -L "https://docs.google.com/uc?export=download&id=15Y7c3X1LwB-5cWrK5LfNxq-67z8-Og3Y" > $UAVHumanPath/UAVHuman.7z
7z x $UAVHumanPath/UAVHuman.7z
rm $UAVHumanPath/UAVHuman.7z