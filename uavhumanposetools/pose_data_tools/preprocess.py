"""
Utility script containing pre-processing logic.
Main call is pre_normalization: 
    Pads empty frames, 
    Centers human, 
    Align joints to axes.
"""

import math

import numpy as np
from tqdm import tqdm


def pre_normalization(data, center_joint=1, zaxis=[11, 5], xaxis=[]):
    """
    Normalization steps:
        1) Pad empty frames with last frame
        2) Center the human at origin
        3) Rotate human to align specified joints to z-axis: ntu [0,1], uav [11,5]
        4) Rotate human to align specified joints to x-axis: ntu [8,4], uav []
    
    Args:
        data: tensor with skeleton data of shape N x C x T x V x M
        center_joint: body joint index indicating center of body
        zaxis: list containing 0 or 2 body joint indices (0 skips the alignment)
        xaxis: list containing 0 or 2 body joint indices (0 skips the alignment)
    """

    N, C, T, V, M = data.shape
    s = np.transpose(data, [0, 4, 2, 3, 1])  # N, C, T, V, M  to  N, M, T, V, C

    print('pad the null frames with the previous frames')
    for i_s, skeleton in enumerate(tqdm(s)):  # pad
        if skeleton.sum() == 0:
            print(i_s, ' has no skeleton')
        for i_p, person in enumerate(skeleton):
            if person.sum() == 0:
                continue
            if person[0].sum() == 0:
                index = (person.sum(-1).sum(-1) != 0)
                tmp = person[index].copy()
                person *= 0
                person[:len(tmp)] = tmp
            for i_f, frame in enumerate(person):
                if frame.sum() == 0:
                    if person[i_f:].sum() == 0:
                        rest = len(person) - i_f
                        num = int(np.ceil(rest / i_f))
                        pad = np.concatenate([person[0:i_f] for _ in range(num)], 0)[:rest]
                        s[i_s, i_p, i_f:] = pad
                        break

    print('sub the center joint #1 (spine joint in ntu and neck joint in kinetics)')
    for i_s, skeleton in enumerate(tqdm(s)):
        if skeleton.sum() == 0:
            continue
        main_body_center = skeleton[0][:, center_joint:center_joint+1, :].copy()
        for i_p, person in enumerate(skeleton):
            if person.sum() == 0:
                continue
            mask = (person.sum(-1) != 0).reshape(T, V, 1)
            s[i_s, i_p] = (s[i_s, i_p] - main_body_center) * mask

    def align_human_to_vector(joint_idx1: int, joint_idx2: int, target_vector: list):
        for i_s, skeleton in enumerate(tqdm(s)):
            if skeleton.sum() == 0:
                continue
            joint1 = skeleton[0, 0, joint_idx1]
            joint2 = skeleton[0, 0, joint_idx2]
            axis = np.cross(joint2 - joint1, target_vector)
            angle = angle_between(joint2 - joint1, target_vector)
            matrix = rotation_matrix(axis, angle)
            for i_p, person in enumerate(skeleton):
                if person.sum() == 0:
                    continue
                for i_f, frame in enumerate(person):
                    if frame.sum() == 0:
                        continue
                    for i_j, joint in enumerate(frame):
                        s[i_s, i_p, i_f, i_j] = np.dot(matrix, joint)

    if zaxis:
        print('parallel the bone between hip(jpt %s)' %zaxis[0] + \
            'and spine(jpt %s) of the first person to the z axis' %zaxis[1])
        align_human_to_vector(zaxis[0], zaxis[1], [0, 0, 1])
    if xaxis:
        print('parallel the bone between right shoulder(jpt %s)' %xaxis[0] + \
            'and left shoulder(jpt %s) of the first person to the x axis' %xaxis[1])
        align_human_to_vector(xaxis[0], xaxis[1], [1, 0, 0])

    data = np.transpose(s, [0, 4, 2, 3, 1])
    return data


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    if np.abs(axis).sum() < 1e-6 or np.abs(theta) < 1e-6:
        return np.eye(3)
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    if np.abs(v1).sum() < 1e-6 or np.abs(v2).sum() < 1e-6:
        return 0
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def x_rotation(vector, theta):
    """Rotates 3-D vector around x-axis"""
    R = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    return np.dot(R, vector)


def y_rotation(vector, theta):
    """Rotates 3-D vector around y-axis"""
    R = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(R, vector)


def z_rotation(vector, theta):
    """Rotates 3-D vector around z-axis"""
    R = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    return np.dot(R, vector)


if __name__ == '__main__':
    data = np.load('../nturgb+d_skeletons_processed/testing_data.npy')
    pre_normalization(data)
    np.save('../nturgb+d_skeletons_processed/testing_data_prenormalized.npy', data)
