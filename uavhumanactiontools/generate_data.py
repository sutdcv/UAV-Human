"""
Script to process raw data and generate frames
    - .jpg files
"""
import os
import glob
import re
import argparse

import cv2
from torchvision import transforms


def gendata(data_path: str,
            out_path: str,
            transforms: transforms.Compose = None):

    vids = [f for f in glob.glob(os.path.join(data_path, "**"), recursive=True) 
        if f.endswith('avi')]
    
    print('Total of %s videos found.' %(len(vids)))
    
    for filename in vids:
        basename = os.path.basename(filename)
        if not os.path.exists(filename):
            raise FileNotFoundError('%s does not exist!' %filename)
        
        print('Decomposing %s.' %filename)
        capture = cv2.VideoCapture(filename)
        ret, frame = capture.read()
        frame_no = 0

        while ret:
            save_path = os.path.splitext(filename.replace(data_path, out_path))[0]
            save_path = os.path.join(save_path, '%s.png' %frame_no)
            save_dir = os.path.dirname(save_path)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            if transforms is not None:
                frame = transforms(frame)
                frame = frame.permute(1, 2, 0).numpy()

            cv2.imwrite(save_path, frame)
            frame_no += 1
            ret, frame = capture.read()


if __name__ == '__main__':

    preprocess_transforms = None
    # preprocess_transforms = transforms.Compose([
    #     transforms.ToTensor(),
    #     transforms.CenterCrop((224, 224))
    # ])

    parser = argparse.ArgumentParser(description='UAVHuman Data Converter.')
    parser.add_argument('--data_path', default='../UAVHuman')
    parser.add_argument('--out_folder', default='../UAVHuman_processed')
    arg = parser.parse_args()

    if not os.path.exists(arg.out_folder):
        os.makedirs(arg.out_folder)
    
    gendata(data_path=arg.data_path,
            out_path=arg.out_folder,
            transforms=preprocess_transforms)
