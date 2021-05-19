# Toolkit for UAV-Human Action Recognition

### Quick setup
1) Edit `download.sh`, specify path to store dataset
2) Run `download.sh`
3) Run `generate_data.py` to split into frames (if reading from frames instead of videos)
You are ready to go!

See sample dataloaders to get started quick. 
* `uavhuman_rgb_dataset.py` reads off videos and is less parallelizable.
* `uavhuman_rgbprocessed_dataset.py` reads off images and is more parallelizable but need to run preprocessing first.
