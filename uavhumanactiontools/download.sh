#!/bin/bash
UAVHumanPath=$(dirname $(pwd))
curl -L "LINK" > UAVHuman.7z
7z x UAVHuman.7z
mv UAVHuman $UAVHumanPath/
rm UAVHuman.7z