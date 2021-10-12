##########################################
#
#  author : Li Tianjiao
#  email  : tianjiao_li@mymail.sutd.edu.sg
# 
#

from glob import glob
import os
from os.path import join as opj
from os.path import basename as opb

from moviepy.editor import VideoFileClip

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--videos', required=True, default=None, type=str, help='path to the folder containing all video clips')
    parser.add_argument('--frames', required=True, default=None, type=str, help='path to the folder saving cropped frames')
    args = parser.parse_args()

    out_root = args.frames
    if os.path.exists(out_root):
        print('Output folder exists! Please check!')
        exit(0)
    else:
        os.makedirs(out_root)
    videos = sorted(glob(opj(args.videos, '*.avi')))
    for cnt, video in enumerate(videos):
        clip = VideoFileClip(video)
        video_dir = opj(out_root, opb(video).strip('.avi'))
        if os.path.exists(video_dir):
            pass
        else:
            os.makedirs(video_dir)
        clip.write_images_sequence(opj(video_dir, '%03d.jpg'), fps=30, verbose=False, logger=None)
        print('[{}/{}] Finishing cropping for {}...'.format(cnt+1, len(videos), video))
    