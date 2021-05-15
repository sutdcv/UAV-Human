"""
Dataloader for UAVHuman dataset
Loads video files into RGB data, each instance contains
    (video-file-name: str, 
     image-tensor: torch.Tensor (shape B x C x N x H x W), 
     label: int)

Alternatively, labels can be in the form for binary classification:
    (video-file-name: str, 
     image-tensor: torch.Tensor (shape B x C x N x H x W), 
     label: torch.Tensor (shape B x classes x N))
"""

import re
import json
import os
import random

import numpy as np
import cv2

import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms


class Uavhuman(Dataset):

    def __init__(self, 
                 split_file: str, 
                 split: str, 
                 root: str, 
                 num_frames: int, 
                 transforms: transforms.Compose = None, 
                 num_classes: int = 155):

        self.split_file = split_file
        self.split = split
        self.root = root
        self.num_frames = num_frames
        self.transforms = transforms
        self.num_classes = num_classes

        self.split_name_conversion = {
            'training': 'train_fns',
            'testing': 'test_fns'
        }
        self.filename_regex = r'P\d+S\d+G\d+B\d+H\d+UC\d+LC\d+A(\d+)R\d+_\d+'

        self.videos = self.get_videos()

    def get_videos(self, binary_labels: bool = False) -> list(tuple((str, np.array))):
        """
        Obtains video names according to json file containing
        video names for training and testing 
        
        Args:
            binary_labels: set true if require binary labels (Batch x Classes x Frames)
        
        Returns:
            List containing Tuples, each with filename and corresponding label
        """
        dataset = []
        with open(self.split_file, 'r') as f:
            train_test_split = json.load(f)

        vids = sorted(train_test_split[self.split_name_conversion[self.split]])    
        vids = [os.path.basename(filename) for filename in vids]
        
        for basename in vids:
            filename = os.path.join(self.root, basename)
            if not os.path.exists(filename):
                raise ValueError('%s does not exist!' %filename)
            
            ann = int(re.match(self.filename_regex, basename).groups()[0])
            if binary_labels:
                label = np.zeros((self.num_classes, self.num_frames), np.float32)
                label[ann, :] = 1
            else:
                label = ann
            dataset.append((basename, label))
        
        print("Make dataset {}: {} video examples".format(self.split, len(vids)))

        return dataset
    
    def load_frames_from_video(self, video_path: str) -> np.array:
        """
        Load sequence of images from video, starting at a random point.

        Args:
            video_path: path to avi file
        
        Returns:
            RGB images, transformed (T x H x W x C)
        """

        capture = cv2.VideoCapture(video_path)
        frames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        
        # random start location
        start_frame = random.randint(0, frames - self.num_frames - 1) # both bounds inclusive
        for i in range(start_frame):
            _, _ = capture.read()

        frames = []
        for _ in range(self.num_frames):
            ret, frame = capture.read()
            frame = frame[:, :, [2, 1, 0]]
            frame = transforms.ToTensor()(frame)
            if self.transforms is not None:
                frame = self.transforms(frame)
            frames.append(frame)

        return torch.stack(frames, dim=1)

    def __getitem__(self, index):
        vid, label = self.videos[index]
        video_path = os.path.join(self.root, vid)
        imgs = self.load_frames_from_video(video_path)
        
        return vid, imgs, label

    def __len__(self):
        return len(self.videos)


if __name__ == "__main__":

    train_transforms = transforms.Compose([
        transforms.CenterCrop((224,224)),
        transforms.Normalize([0.5], [0.5])
    ])
    dataset = Uavhuman(split_file='../UAVHuman/nightvision/train_test_split.json',
                       split='training',
                       root='../UAVHuman/nightvision',
                       num_frames=64,
                       transforms=train_transforms)
    dataloader = DataLoader(dataset, batch_size=1)
    for cnt, (filename, images, labels) in enumerate(dataloader):
        import ipdb; ipdb.set_trace()
    import ipdb; ipdb.set_trace()
