"""
Dataloader for UAVHuman rgb dataset
Loads RGB data from preprocessed files, each instance contains
    (video-file-name: str, 
     image-tensor: torch.Tensor (shape B x C x N x H x W), 
     label: int)

Alternatively, labels can be in the form for binary classification:
    (video-file-name: str, 
     image-tensor: torch.Tensor (shape B x C x N x H x W), 
     label: torch.Tensor (shape B x classes x N))
"""

import re
import os
import glob
import random

import numpy as np
from PIL import Image

import torch
from torch.utils.data import Dataset
from torchvision import transforms


class UavhumanRgb(Dataset):

    def __init__(self, 
                 root: str, 
                 num_frames: int, 
                 transforms: transforms.Compose = None, 
                 num_classes: int = 155):

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
        Obtain video names and corresponding label in data directory.
        Expects video folders to be of depth=2.
        
        Args:
            binary_labels: set true if require binary labels (Batch x Classes x Frames)
        
        Returns:
            List containing Tuples, each with filename and corresponding label
        """
        dataset = []
        vids = [f for f in glob.glob(os.path.join(self.root, "*.avi"), recursive=True) 
            if os.path.isdir(f)]
        
        for filename in vids:
            basename = os.path.basename(filename)
            
            ann = int(re.match(self.filename_regex, basename).groups()[0])
            if binary_labels:
                label = np.zeros((self.num_classes, self.num_frames), np.float32)
                label[ann, :] = 1
            else:
                label = ann
            dataset.append((filename, label))
        
        print("Found %s video examples" %(len(vids)))

        return dataset
    
    def load_frames_from_video(self, video_path: str) -> np.array:
        """
        Load sequence of images from folder, starting at a random point.

        Args:
            video_path: path to folder of frames
        
        Returns:
            RGB images, transformed (T x H x W x C)
        """

        filenames = [f for f in glob.glob(os.path.join(video_path, '*.png'))]
        frames = len(filenames)
        
        # random start location
        start_frame = random.randint(0, frames - self.num_frames - 1) # both bounds inclusive
        
        data_array = []
        for i in range(start_frame, start_frame + 64):
            image = Image.open(filenames[i]).convert('RGB')
            if self.transforms is not None:
                image = self.transforms(image)
            else:
                image = transforms.ToTensor()(image)
            data_array.append(image)

        return torch.stack(data_array, dim=1)

    def __getitem__(self, index):
        video_path, label = self.videos[index]
        imgs = self.load_frames_from_video(video_path)
        
        return video_path, imgs, label

    def __len__(self):
        return len(self.videos)


if __name__ == "__main__":

    import argparse
    from tqdm import tqdm
    from torch.utils.data import DataLoader
    from torchvision.utils import save_image

    parser = argparse.ArgumentParser(description='UAVHuman Action Data Loader.')
    parser.add_argument('--data_path', required=True)
    args = parser.parse_args()

    train_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.5], [0.5])
    ])
    dataset = UavhumanRgb(root=os.path.join(args.data_path, 'train'),
                          num_frames=64,
                          transforms=train_transforms)
    dataloader = DataLoader(dataset, batch_size=1, num_workers=4)
    for cnt, (filename, images, labels) in enumerate(tqdm(dataloader)):
        assert(isinstance(filename[0], str))
        assert(len(filename) == 1)
        assert(images.shape == torch.Size([1, 3, 64, 1080, 1920]))
        assert(labels.shape == torch.Size([1]))
    
    save_image(images[:, :, 0, :, :], 'uavhuman_rgb_sample.png')
    print("Dataloader test complete")
