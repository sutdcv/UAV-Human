# Toolkit for UAV-Human Attribute Recognition

Extract the downloaded data into ``data`` folder.

Expected directory in `/path/to/attribute_data_root`
```
└───[attribute_data_root]
     |  
     uavhuman
     ├───train
         ├───P000S00G10B10H10UC022000LC021000A000R0_08241716_170.jpg
         ├───P000S00G10B10H10UC022000LC021000A005R0_08241716_011.jpg
         └───...
     ├───test
         ├───P001S00G20B40H20UC072000LC021000A000R0_08241838_004.jpg
         ├───P001S00G20B40H20UC072000LC021000A002R0_08241838_090.jpg
         └───...
```

A Possible Quick Start:

```python
train_dataset, test_dataset = get_uavhuman(root='data/uavhuman',
                                           transforms=transforms.Compose([
                                               transforms.Resize((Hight,Width)),
                                               transforms.ToTensor()
                                               ]))
```
