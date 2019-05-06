# -*- encoding: utf-8 -*-
'''
@File    :   batch_file_replace.py
@Time    :   2019/05/06 09:50:16
@Author  :   lby 
@Version :   1.0
@Desc    :   None
'''

import os
import argparse

def batch_replace(work_dir, old_str, new_str):
    
    for filename in os.listdir(work_dir):
        filename = work_dir + '/' + filename
        a = open(filename,'r') #打开所有文件
        str = a.read()
        print(str)
        str = str.replace(old_str , new_str)
        b = open(filename,'w')
        b.write(str) #再写入
        print(str)
        b.close() #关闭文件

def get_parser():
    parser = argparse.ArgumentParser(description='replace of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='work_dir')
    parser.add_argument('old', metavar='old', type=str, nargs=1, help='old_str')
    parser.add_argument('new', metavar='new', type=str, nargs=1, help='new_str')
    return parser 

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args['work_dir'][0]
    old_str = args['old'][0]
    new_str = args['new'][0]

    batch_replace(work_dir, old_str, new_str)

if __name__ == '__main__':
    main()