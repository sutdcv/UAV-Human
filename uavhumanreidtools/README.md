# Toolkit for UAV-Human Person Re-Identification

Extract the downloaded data into ``data`` folder.

Run the reader script to obtain dataloader:
```
python UAVReader.py --data_path /path/to/reid_data_root
```

Expected directory in `/path/to/reid_data_root`
```
└───[reid_data_root]
    ├───bounding_box_train
        ├───P000S00G10B10H10UC022000LC021000A000R0_08241716_170_bbx.jpg
        ├───P000S00G10B10H10UC022000LC021000A001R0_08241716_216_bbx.jpg
        └───...
    ├───bounding_box_test
        ├───00000.jpg
        ├───00001.jpg
        └───...
    └───query
        ├───00000.jpg
        ├───00001.jpg
        └───...
```

During the competition, we only provide a simple training split reader for your reference, if you would like to read test and query data, please wait for further notice to access the testing and query data.