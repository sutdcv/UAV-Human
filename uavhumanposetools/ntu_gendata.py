import argparse
import pickle
import os
import sys
import json
import re

import numpy as np
from tqdm import tqdm

from preprocess import pre_normalization

max_body_true = 2
max_body_kinect = 4
num_joint = 25
max_frame = 601

split_name_conversion = {
    'training': 'train_fns',
    'testing': 'test_fns'
}
filename_regex = r'P\d+S\d+G\d+B\d+H\d+UC\d+LC\d+A(\d+)R\d+_\d+'


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
    index = energy.argsort()[::-1][0:max_body_true]
    data = data[index]

    data = data.transpose(3, 1, 2, 0)
    return data


def gendata(data_path,
            out_path,
            split,
            split_file,
            ignored_sample_path=None):
    
    if ignored_sample_path is not None:
        with open(ignored_sample_path, 'r') as f:
            ignored_samples = [line.strip() + '.skeleton' for line in f.readlines()]
    else:
        ignored_samples = []
    
    with open(split_file, 'r') as f:
        split_file = json.load(f)
    
    skeleton_filenames = sorted(split_file[split_name_conversion[split]])
    skeleton_filenames = [os.path.basename(filename)[:-8]+'.txt' for filename in skeleton_filenames]
    
    sample_name = []
    sample_label = []
    
    for basename in skeleton_filenames:
        filename = os.path.join(data_path, basename)
        if filename in ignored_samples:
            continue
        if not os.path.exists(filename):
            print('%s does not exist!' %filename)
            continue
        
        sample_name.append(filename)
        
        label = int(re.match(filename_regex, basename).groups()[0])
        sample_label.append(label)

    with open('{}/{}_label.pkl'.format(out_path, split), 'wb') as f:
        pickle.dump((sample_name, list(sample_label)), f)

    fp = np.zeros((len(sample_label), 3, max_frame, num_joint, max_body_true), dtype=np.float32)
    max_data_c1 = 0
    max_sample_name = ''

    for i, s in enumerate(tqdm(sample_name)):
        data = read_xyz(os.path.join(data_path, s), max_body=max_body_kinect, num_joint=num_joint)
        fp[i, :, 0:data.shape[1], :, :] = data
        if data.shape[1] > max_data_c1:
            max_data_c1 = data.shape[1]
            max_sample_name = s

    fp = pre_normalization(fp)
    np.save('{}/{}_data_joint.npy'.format(out_path, split), fp)

    import ipdb
    ipdb.set_trace()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='UAVHuman Data Converter.')
    parser.add_argument('--data_path', default='../nturgb+d_skeletons')
    parser.add_argument('--ignored_sample_path', default=None)
    parser.add_argument('--out_folder', default='../nturgb+d_skeletons_processed')
    parser.add_argument('--train_test_split', default='D:/Downloads/train_test_split.json')
    arg = parser.parse_args()

    if not os.path.exists(arg.out_folder):
        os.makedirs(arg.out_folder)
    
    gendata(data_path=arg.data_path,
            out_path=arg.out_folder,
            split='training',
            split_file=arg.train_test_split,
            ignored_sample_path=arg.ignored_sample_path)
    gendata(data_path=arg.data_path,
            out_path=arg.out_folder,
            split='testing',
            split_file=arg.train_test_split,
            ignored_sample_path=arg.ignored_sample_path)
