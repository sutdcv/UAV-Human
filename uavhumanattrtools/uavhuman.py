import torch
from torch.utils.data import Dataset

import os
from glob import glob

import re

from PIL import Image

def get_uavhuman(root, transforms):

    train_split = UAVHuman(os.path.join(root, 'train'), transforms=transforms, split='train', verbose=False)
    test_split = UAVHuman(os.path.join(root, 'test'), transforms=transforms, split='test', verbose=False)

    return train_split, test_split

class UAVHuman(Dataset):
    def __init__(self, root, transforms=None, split='train', verbose=True):
        super().__init__()
        assert split == 'train' or split == 'test'
        self.root = root
        self.split = split
        self.verbose = verbose

        self.transforms = transforms

        self.pattern = r'P\d+S\d+G(\d+)B(\d+)H(\d+)UC(\d+)LC(\d+)A\d+R\d+_\d+'

        self.fns = sorted(glob(os.path.join(self.root, '*.jpg')))

    def parse_label(self, fn):
        genders, backpacks, hats, upper_clothes, lower_clothes = re.match(self.pattern, os.path.basename(fn)).groups()
        gender = genders[0]
        backpack = backpacks[0]
        hat = hats[0]
        upper_clothes_color, upper_clothes_style = upper_clothes[0:2], upper_clothes[2:3]
        lower_clothes_color, lower_clothes_style = lower_clothes[0:2], lower_clothes[2:3]

        return gender, backpack, hat, upper_clothes_color, upper_clothes_style, lower_clothes_color, lower_clothes_style
    
    def __getitem__(self, index):
        """
        Labels:
            g   : gender
            b   : backpack
            h   : hat
            ucc : upper_clothes_color
            ucs : upper_clothes_style
            lcc : lower_clothes_color
            lcs : lower_clothes_style
        """
        fn = self.fns[index]
        g, b, h, ucc, ucs, lcc, lcs = self.parse_label(fn)
        
        im = Image.open(fn)
        
        if self.transforms is not None:
            im = self.transforms(im)        

        return im, int(g), int(b), int(h), int(ucc), int(ucs), int(lcc), int(lcs)

    def __len__(self):
        return len(self.fns)

