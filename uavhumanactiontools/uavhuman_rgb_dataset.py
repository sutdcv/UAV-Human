"""
Dataloader for UAVHuman rgb dataset
Loads video files into RGB data, each instance contains
    (video-file-name: str, 
     image-tensor: torch.Tensor (shape B x C x N x H x W), 
     label: int)

Alternatively, labels can be in the form for binary classification:
    (video-file-name: str, 
     image-tensor: torch.Tensor (shape B x C x N x H x W), 
     label: torch.Tensor (shape B x classes x N))

Note:
    Runtime for single worker is same as loading using image on average.
    However, loading of one video instance is not done by more than one worker.
    Preprocess into images and use the other loader if more workers is available.
"""

import re
import os
import glob
import random

import numpy as np
import cv2

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

        self.filename_regex = r'P\d+S\d+G\d+B\d+H\d+UC\d+LC\d+A(\d+)R\d+_\d+'

        self.videos = self.get_videos()

    def get_videos(self, binary_labels: bool = False) -> list(tuple((str, np.array))):
        """
        Obtain video names and corresponding label in directory recursively.
        
        Args:
            binary_labels: set true if require binary labels (Batch x Classes x Frames)
        
        Returns:
            List containing Tuples, each with filename and corresponding label
        """
        dataset = []
        vids = [f for f in glob.glob(os.path.join(self.root, "*"), recursive=True) 
            if f.endswith('avi')]
        
        for filename in vids:
            basename = os.path.basename(filename)
            if not os.path.exists(filename):
                raise ValueError('%s does not exist!' %filename)
            
            ann = int(re.match(self.filename_regex, basename).groups()[0])
            if binary_labels:
                label = np.zeros((self.num_classes, self.num_frames), np.float32)
                label[ann, :] = 1
            else:
                label = ann
            dataset.append((basename, label))
        
        print("Found %s video examples" %(len(vids)))

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

    import argparse
    from tqdm import tqdm
    from torch.utils.data import DataLoader
    from torchvision.utils import save_image

    parser = argparse.ArgumentParser(description='UAVHuman Action Data Loader.')
    parser.add_argument('--data_path', required=True)
    args = parser.parse_args()

    train_transforms = transforms.Compose([
        transforms.Normalize([0.5], [0.5])
    ])
    dataset = UavhumanRgb(root=os.path.join(args.data_path, 'train'),
                          num_frames=64,
                          transforms=train_transforms)
    dataloader = DataLoader(dataset, batch_size=1, num_workers=1)
    for cnt, (filename, images, labels) in enumerate(tqdm(dataloader)):
        assert(isinstance(filename[0], str))
        assert(len(filename) == 1)
        assert(images.shape == torch.Size([1, 3, 64, 1080, 1920]))
        assert(labels.shape == torch.Size([1]))

    save_image(images[:, :, 0, :, :], '../uavhuman_rgb_sample.png')
    print("Dataloader test complete")
