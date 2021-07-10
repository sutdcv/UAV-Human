"""
Dataloader for UAVHuman pose dataset
Loads skeleton data from preprocessed files, each instance contains
    (index: int
     skeleton-tensor: torch.Tensor (shape B x C x V x T x M), 
     label: int)

Normalisation seems to cause an issue currently.
"""

import os
import pickle

import numpy as np
from torch.utils.data import DataLoader, Dataset

from pose_data_tools import tools


class UavhumanPose(Dataset):
    def __init__(self, data_path, label_path,
                 random_choose=False, random_shift=False, random_move=False,
                 window_size=-1, normalization=False, debug=False, use_mmap=True):
        """
        Args:
            data_path: path to npy file containing skeleton data
            label_path: path to pkl file containing labels
            random_choose: If true, randomly choose a portion of the input sequence
            random_shift: If true, randomly pad zeros at the begining or end of sequence
            random_move: If true, randomly scale, rotate and translate by small amount
            window_size: The length of the output sequence
            normalization: If true, normalize input sequence
            debug: If true, only use the first 100 samples
            use_mmap: If true, use mmap mode to load data, which can save the running memory
        """

        self.data_path = data_path
        self.label_path = label_path
        self.random_choose = random_choose
        self.random_shift = random_shift
        self.random_move = random_move
        self.window_size = window_size
        self.normalization = normalization
        self.debug = debug
        self.use_mmap = use_mmap
        
        self.load_data()
        if normalization:
            self.get_mean_map()

    def load_data(self):
        """
        Obtain skeleton data and corresponding labels from preprocessed files
        """

        try:
            with open(self.label_path) as f:
                self.sample_name, self.label = pickle.load(f)
        except:
            # for pickle file from python2
            with open(self.label_path, 'rb') as f:
                self.sample_name, self.label = pickle.load(f, encoding='latin1')

        if self.use_mmap:
            self.data = np.load(self.data_path, mmap_mode='r')
        else:
            self.data = np.load(self.data_path)
        
        if self.debug:
            self.label = self.label[0:100]
            self.data = self.data[0:100]
            self.sample_name = self.sample_name[0:100]

    def get_mean_map(self):
        """
        Get mean and standard deviation for normalization
        """
        
        data = self.data
        N, C, T, V, M = data.shape
        self.mean_map = data.mean(axis=2, keepdims=True).mean(axis=4, keepdims=True).mean(axis=0)
        self.std_map = data.transpose((0, 2, 4, 1, 3)).reshape((N * T * M, C * V)).std(axis=0).reshape((C, 1, V, 1))

    def __len__(self):
        return len(self.label)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        data_numpy = np.array(self.data[index])

        if self.normalization:
            data_numpy = (data_numpy - self.mean_map) / self.std_map
            data_numpy = np.nan_to_num(data_numpy)
        if self.random_shift:
            data_numpy = tools.random_shift(data_numpy)
        if self.random_choose:
            data_numpy = tools.random_choose(data_numpy, self.window_size)
        elif self.window_size > 0:
            data_numpy = tools.auto_pading(data_numpy, self.window_size)
        if self.random_move:
            data_numpy = tools.random_move(data_numpy)

        return self.sample_name[index], data_numpy, self.label[index]

    def top_k(self, score, top_k):
        rank = score.argsort()
        hit_top_k = [l in rank[i, -top_k:] for i, l in enumerate(self.label)]
        return sum(hit_top_k) * 1.0 / len(hit_top_k)


if __name__ == "__main__":
    
    import torch
    import argparse

    from pose_data_tools.visualise import visualise
    from pose_data_tools.graph import Graph
    from tqdm import tqdm

    parser = argparse.ArgumentParser(description='UAVHuman Pose Data Loader.')
    parser.add_argument('--data_path', required=True)
    args = parser.parse_args()

    dataset = UavhumanPose(data_path=os.path.join(args.data_path, 'train_data.npy'), 
                           label_path=os.path.join(args.data_path, 'train_label.pkl'),
                           random_choose=False, 
                           random_shift=False, 
                           random_move=False,
                           window_size=-1, 
                           normalization=False, 
                           debug=False, 
                           use_mmap=True)
    dataloader = DataLoader(dataset, batch_size=1)
    for cnt, (filename, images, labels) in enumerate(tqdm(dataloader)):
        assert(len(filename) == 1)
        assert(isinstance(filename[0], str))
        assert(images.shape == torch.Size([1, 3, 300, 17, 2])), filename
        assert(labels.shape == torch.Size([1]))
    visualise(images, graph=Graph(), is_3d=True)
    print("Dataloader test complete.")
