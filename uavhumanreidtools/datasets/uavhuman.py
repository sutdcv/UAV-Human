# encoding: utf-8
"""
@author:  sherlock
@contact: sherlockliao01@gmail.com

@author: Li Tianjiao
@contact: tianjiao_li@mymail.sutd.edu.sg
"""

import glob
import re

import os.path as osp

from .bases import BaseImageDataset


class UAVHuman(BaseImageDataset):
    
    def __init__(self, root='./data', 
            verbose=True, **kwargs):
        super(UAVHuman, self).__init__()
        self.dataset_dir = root
        self.train_dir = osp.join(self.dataset_dir, 'bounding_box_train')
        
        """Comment for Competition Splits
        self.query_dir = osp.join(self.dataset_dir, 'query')
        self.gallery_dir = osp.join(self.dataset_dir, 'bounding_box_test')
        """

        self._check_before_run()

        train = self._process_dir(self.train_dir, relabel=True)
        
        """Comment for Competition Splits
        query = self._process_dir(self.query_dir, relabel=False)
        gallery = self._process_dir(self.gallery_dir, relabel=False)
        """

        if verbose:
            print("=> UAVHuman loaded")
            
            """Comment for Competition Split
            self.print_dataset_statistics(train, query, gallery)
            """
            
            self.print_dataset_statistics_for_train_only(train)

        self.train = train
        
        """Comment for Competition Splits
        self.query = query
        self.gallery = gallery
        """

        self.num_train_pids, self.num_train_imgs, self.num_train_cams = self.get_imagedata_info(self.train)
        
        """Comment for Competition Splits
        self.num_query_pids, self.num_query_imgs, self.num_query_cams = self.get_imagedata_info(self.query)
        self.num_gallery_pids, self.num_gallery_imgs, self.num_gallery_cams = self.get_imagedata_info(self.gallery)
        """

    def _check_before_run(self):
        """Check if all files are available before going deeper"""
        if not osp.exists(self.dataset_dir):
            raise RuntimeError("'{}' is not available".format(self.dataset_dir))
        if not osp.exists(self.train_dir):
            raise RuntimeError("'{}' is not available".format(self.train_dir))

        """Comment for Competition Splits
        if not osp.exists(self.query_dir):
            raise RuntimeError("'{}' is not available".format(self.query_dir))
        if not osp.exists(self.gallery_dir):
            raise RuntimeError("'{}' is not available".format(self.gallery_dir))
        """

    def _process_dir(self, dir_path, relabel=False):
        img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
        pattern_pid = re.compile(r'P([-\d]+)S([-\d]+)')
        pattern_camid = re.compile(r'A([-\d]+)R([-\d])_([-\d]+)_([-\d]+)')
        distractor_pid = 50000

        pid_container = set()
        for img_path in img_paths:
            fname = osp.split(img_path)[-1]
            if fname.startswith('D'):
                pid = int(distractor_pid)
            else:
                pid_part1, pid_part2 = pattern_pid.search(fname).groups()
                pid = int(pid_part1 + pid_part2)
            
            if pid == -1: continue  # junk images are just ignored
            if pid == 3109 or pid == 8405: 
                import ipdb; ipdb.set_trace()
                continue

            pid_container.add(pid)
        pid2label = {pid: label for label, pid in enumerate(pid_container)}

        dataset = []
        for img_path in img_paths:
            fname = osp.split(img_path)[-1]
            if fname.startswith('D'):
                pid = int(distractor_pid)
                camid = int(fname[-13:-8])
            else:
                pid_part1, pid_part2 = pattern_pid.search(fname).groups()
                pid = int(pid_part1 + pid_part2)
                camid_part1, _, _, camid_part2 = pattern_camid.search(fname).groups()
                camid = int(camid_part1 + camid_part2)
            if pid == -1: continue  # junk images are just ignored
            if relabel: pid = pid2label[pid]
            dataset.append((img_path, pid, camid))

        return dataset
