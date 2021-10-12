"""
Script to process raw data and generate dataset's binary files:
    - .npy skeleton data files: np.array of shape B x C x V x T x M
    - .pkl label files: (filename: str, label: list[int])
"""

import argparse
import pickle
import os
import glob
import re

import numpy as np
from tqdm import tqdm

from pose_data_tools.preprocess import pre_normalization

MAX_BODY_TRUE = 2
MAX_BODY_KINECT = 4
NUM_JOINT = 17
MAX_FRAME = 300

FILENAME_REGEX = r'P\d+S\d+G\d+B\d+H\d+UC\d+LC\d+A(\d+)R\d+_\d+'


def read_skeleton_filter(file):
    with open(file, 'r') as f:
        skeleton_sequence = {}
        skeleton_sequence['numFrame'] = int(f.readline())
        skeleton_sequence['frameInfo'] = []
        # num_body = 0
        for t in range(skeleton_sequence['numFrame']):
            frame_info = {}
            frame_info['numBody'] = int(f.readline())
            frame_info['bodyInfo'] = []

            for m in range(frame_info['numBody']):
                body_info = {}
                body_info_key = [
                    'bodyID', 'clipedEdges', 'handLeftConfidence',
                    'handLeftState', 'handRightConfidence', 'handRightState',
                    'isResticted', 'leanX', 'leanY', 'trackingState'
                ]
                body_info = {
                    k: float(v)
                    for k, v in zip(body_info_key, f.readline().split())
                }
                body_info['numJoint'] = int(f.readline())
                body_info['jointInfo'] = []
                for v in range(body_info['numJoint']):
                    joint_info_key = [
                        'x', 'y', 'z', 'depthX', 'depthY', 'colorX', 'colorY',
                        'orientationW', 'orientationX', 'orientationY',
                        'orientationZ', 'trackingState'
                    ]
                    joint_info = {
                        k: float(v)
                        for k, v in zip(joint_info_key, f.readline().split())
                    }
                    body_info['jointInfo'].append(joint_info)
                frame_info['bodyInfo'].append(body_info)
            skeleton_sequence['frameInfo'].append(frame_info)

    return skeleton_sequence


def get_nonzero_std(s):  # tvc
    index = s.sum(-1).sum(-1) != 0  # select valid frames
    s = s[index]
    if len(s) != 0:
        s = s[:, :, 0].std() + s[:, :, 1].std() + s[:, :, 2].std() # three channels
    else:
        s = 0
    return s


def read_xyz(file, max_body, num_joint):
    seq_info = read_skeleton_filter(file)
    data = np.zeros((max_body, seq_info['numFrame'], num_joint, 3))
    for n, f in enumerate(seq_info['frameInfo']):
        for m, b in enumerate(f['bodyInfo']):
            for j, v in enumerate(b['jointInfo']):
                if m < max_body and j < num_joint:
                    data[m, n, j, :] = [v['x'], v['y'], v['z']]
                else:
                    pass

    # select two max energy body
    energy = np.array([get_nonzero_std(x) for x in data])
    index = energy.argsort()[::-1][0:MAX_BODY_TRUE]
    data = data[index]

    data = data.transpose(3, 1, 2, 0)
    return data


def gendata(data_path,
            split):
    
    out_path = data_path
    data_path = os.path.join(data_path, split)

    skeleton_filenames = [os.path.basename(f) for f in 
        glob.glob(os.path.join(data_path, "**.txt"), recursive=True)]
    
    sample_name = []
    for basename in skeleton_filenames:
        filename = os.path.join(data_path, basename)
        if not os.path.exists(filename):
            raise OSError('%s does not exist!' %filename)
        sample_name.append(filename)

    data = np.zeros((len(sample_name), 3, MAX_FRAME, NUM_JOINT, MAX_BODY_TRUE), dtype=np.float32)
    for i, s in enumerate(tqdm(sample_name)):
        sample = read_xyz(s, max_body=MAX_BODY_KINECT, num_joint=NUM_JOINT)
        sample = sample[:, :MAX_FRAME, :, :]
        data[i, :, 0:sample.shape[1], :, :] = sample
    data = pre_normalization(data)

    np.save('{}/{}_data.npy'.format(out_path, split), data)

    if split != 'test':
        sample_label = []
        for basename in skeleton_filenames:
            label = int(re.match(FILENAME_REGEX, basename).groups()[0])
            sample_label.append(label)

        with open('{}/{}_label.pkl'.format(out_path, split), 'wb') as f:
            pickle.dump((sample_name, list(sample_label)), f)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='UAVHuman Data Converter.')
    parser.add_argument('--data_path', required=True)
    args = parser.parse_args()
    
    gendata(data_path=args.data_path,
            split='train')
    gendata(data_path=args.data_path,
            split='test')
