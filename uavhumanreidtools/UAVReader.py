import argparse

from datasets import UAVHuman 


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='UAVHuman Data Reader.')
    parser.add_argument('--data_path', required=True, default='./data')
    args = parser.parse_args()

    dset = UAVHuman(root=args.data_path)
    