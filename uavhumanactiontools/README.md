# Toolkit for UAV-Human Action Recognition

Extract the downloaded data into ``data`` folder.

Expected directory in `/path/to/action_data_root`
```
└───[action_data_root]
    ├───train
        ├───P000S00G10B10H10UC022000LC021000A000R0_08241716.avi
        ├───P000S00G10B10H10UC022000LC021000A001R0_08241716.avi
        └───...
    ├───test
        ├───0000.avi
        ├───0001.avi
        └───...
```

Run the following script to preprocess the videos into images (optional, but can yield speedups in data loading during batch training)
```
python generate_data.py --data_path /path/to/action_data_root --out_folder /path/to/action_processed_data_root --num_workers 32
```

Expected directory in `/path/to/action_processed_data_root`
```
└───[action_processed_data_root]
    ├───train
        ├───P000S00G10B10H10UC022000LC021000A000R0_08241716.avi
            ├───0.png
            ├───1.png
            └───...    
        ├───P000S00G10B10H10UC022000LC021000A001R0_08241716.avi
            ├───0.png
            ├───1.png
            └───...
        └───...
    ├───test
        ├───0000.avi
            ├───0.png
            ├───1.png
            └───...    
        ├───0001.avi
            ├───0.png
            ├───1.png
            └───...    
        └───...
```

Check the shapes of images and labels, and visualise a sample image using the corresponding sample dataloader test (optional).
```
python uavhuman_rgb_dataset.py --data_path /path/to/action_data_root
python uavhuman_rgbprocessed_dataset.py --data_path /path/to/action_processed_data_root
```

Feel free to use or adapt the sample dataloaders.
* `uavhuman_rgb_dataset.py` reads off videos and is less parallelizable.
* `uavhuman_rgbprocessed_dataset.py` reads off images and is more parallelizable but need to run preprocessing first.
