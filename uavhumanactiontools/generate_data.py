"""
Script to process raw data and generate frames
    - .jpg files
"""
import os
import glob
import re
import argparse
from multiprocessing import Pool
from itertools import repeat

import cv2
from torchvision import transforms


def extract_frames(filename: str, 
                   save_dir: str, 
                   transforms: transforms.Compose = None) -> None:
    """
    Extract frames given path to video. 

    Args:
        filename: path to video
        save_dir: path to frame output directory
        transforms: torchvision transformations
    """

    basename = os.path.basename(filename)
    if not os.path.exists(filename):
        raise FileNotFoundError('%s does not exist!' %filename)

    print('Decomposing %s.' %filename)
    capture = cv2.VideoCapture(filename)
    ret, frame = capture.read()
    frame_no = 0

    while ret:
        save_path = os.path.join(save_dir, '%s.png' %frame_no)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        if transforms is not None:
            frame = transforms(frame)
            frame = frame.permute(1, 2, 0).numpy()

        cv2.imwrite(save_path, frame)
        frame_no += 1
        ret, frame = capture.read()


def gendata(data_path: str,
            out_path: str,
            num_workers: int,
            transforms: transforms.Compose = None):

    vids = [f.replace('\\', '/') for f in 
        glob.glob(os.path.join(data_path, '**/*.avi'), recursive=True)]
    print('Total of %s videos found.' %(len(vids)))

    def get_save_dir(vid_filename):
        video_base_path = vid_filename.split(data_path)[1]
        return os.path.join(out_path, video_base_path)
    save_dirs = [get_save_dir(f) for f in vids]

    Pool(num_workers).starmap(
        extract_frames, zip(vids, save_dirs, repeat(transforms)))


if __name__ == '__main__':

    preprocess_transforms = None
    # preprocess_transforms = transforms.Compose([
    #     transforms.ToTensor(),
    #     transforms.CenterCrop((224, 224))
    # ])

    parser = argparse.ArgumentParser(description='UAVHuman Data Converter.')
    parser.add_argument('--data_path', required=True)
    parser.add_argument('--out_folder', required=True)
    parser.add_argument('--num_workers', default=4)
    args = parser.parse_args()

    if not os.path.exists(args.out_folder):
        os.makedirs(args.out_folder)

    gendata(data_path=args.data_path,
            out_path=args.out_folder,
            transforms=preprocess_transforms,
            num_workers=args.num_workers)
