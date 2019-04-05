# -*- coding: GBK -*-
# batch_file_split_rename.py

import os
import argparse


def batch_rename(work_dir, split_name):

    for filename in os.listdir(work_dir):
        split_file = filename.split(split_name)
        tupleToList = list(split_file)
        tupleToList.remove(tupleToList.index(split_name))

        os.rename(
            os.path.join(work_dir, filename),
            os.path.join(work_dir, tupleToList[0])
        )



def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('split_name', metavar='SPLIT_NAME', type=str, nargs=1, help='split name')
    return parser 

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args['work_dir'][0]
    split_name = args['split_name'][0]

    batch_rename(work_dir, split_name)


if __name__ == '__main__':
    main()