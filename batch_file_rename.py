# -*- coding: GBK -*-
# batch_file_rename.py

import os
import argparse


def batch_rename(work_dir, replace_name):

    for filename in os.listdir(work_dir):
        newFileName = filename.replace(replace_name, "_")

        os.rename(
            os.path.join(work_dir, filename),
            os.path.join(work_dir, newFileName)
        )


def get_parser():
    parser = argparse.ArgumentParser(
        description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('replace_name', metavar='REPLACE_NAME',
                        type=str, nargs=1, help='replace name')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args['work_dir'][0]
    replace_name = args['replace_name'][0]
    print(args['work_dir'][0])
    print(args['replace_name'][0])

    batch_rename(work_dir, replace_name)


if __name__ == '__main__':
    main()
