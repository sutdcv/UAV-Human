# Toolkit for UAV-Human Pose Estimation

Extract the downloaded data into ``data`` folder.

Run the following script to preprocess the files:
```
python generate_data.py --data_path /path/to/pose_data_root
```

Expected directory in `/path/to/pose_data_root`
```
└───[pose_data_root]
    ├───train
        ├───P000S00G10B10H10UC022000LC021000A000R0_08241716.txt
        ├───P000S00G10B10H10UC022000LC021000A001R0_08241716.txt
        └───...
    ├───test
        ├───0000.txt
        ├───0001.txt
        └───...
    ├───train_label.pkl
    ├───train_data.npy
    └───test_label.pkl
```

Check the shapes of images and labels, and visualise a sample using the sample dataloader test (optional).
```
python uavhuman_pose_dataset.py --data_path /path/to/pose_data_root
```

Feel free to use or adapt the sample dataloaders and visualising tools.
