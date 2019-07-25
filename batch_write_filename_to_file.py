# -*- encoding: utf-8 -*-
'''
@File    :   batch_write_filename_to_file.py
@Time    :   2019/07/25 10:02:49
@Author  :   lby 
@Version :   1.0
@Desc    :   None
'''


import os
import argparse
from string import Template

def batch_write(work_dir, write_file_name, write_pattern):
    tmp=Template(write_pattern)
    writeFile = open(write_file_name, "w")  
    for filename in os.listdir(work_dir):
        output = tmp.substitute(sql_name1 = filename, sql_name2 = filename)
        writeFile.write(output)
        writeFile.write("\n")
    writeFile.close()



def get_parser():
    parser = argparse.ArgumentParser(
        description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('write_file_name', metavar='WRITE_FILE_NAME',
                        type=str, nargs=1, help='write file name')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args['work_dir'][0]
    write_file_name = args['write_file_name'][0]
    print(args['work_dir'][0])
    print(args['write_file_name'][0])

    write_pattern = "SPOOL ${sql_name1}.log\n@CS2Admin/scripts/${sql_name2}\nSPOOL OFF\n"
    batch_write(work_dir, write_file_name, write_pattern)


if __name__ == '__main__':
    main()