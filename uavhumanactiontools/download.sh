#!/bin/bash
UAVHumanPath=$(dirname $(pwd))
curl -L "https://docs.google.com/uc?export=download&id=15Y7c3X1LwB-5cWrK5LfNxq-67z8-Og3Y" > UAVHuman.7z
7z x UAVHuman.7z
mv UAVHuman $UAVHumanPath/
rm UAVHuman.7z