# gz： 即gzip。通常仅仅能压缩一个文件。与tar结合起来就能够实现先打包，再压缩。
#
# tar： linux系统下的打包工具。仅仅打包。不压缩
#
# tgz：即tar.gz。先用tar打包，然后再用gz压缩得到的文件
#
# zip： 不同于gzip。尽管使用相似的算法，能够打包压缩多个文件。只是分别压缩文件。压缩率低于tar。
#
# rar：打包压缩文件。最初用于DOS，基于window操作系统。

import gzip
import tarfile
import zipfile
import os
import argparse

def batch_unzip(work_dir):
    unzip_str = os.path.join(work_dir, 'unzip')
    # if not os.listdir(unzip_str):
    #     os.rmdir(unzip_str)
    os.mkdir(unzip_str)
    for filename in os.listdir(work_dir):
        if not os.path.isdir(filename):
            # filename = work_dir + '/' + filename
            un_gz(work_dir, unzip_str, filename)


# gz
# 因为gz一般仅仅压缩一个文件，全部常与其它打包工具一起工作。比方能够先用tar打包为XXX.tar,然后在压缩为XXX.tar.gz
# 解压gz，事实上就是读出当中的单一文件
def un_gz(work_dir, unzip_str, file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    #获取文件的名称，去掉
    real_name = work_dir + '/' + file_name
    g_file = gzip.GzipFile(real_name)
    strs = g_file.read()
    #创建gzip对象
    b = open(unzip_str +'/'+ f_name,'wb')
    b.write(strs) #再写入
    #gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
    b.close()
    #关闭gzip对象


def un_tar(file_name):
       # untar zip file"""
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    #因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()

# zip
# 与tar类似，先读取多个文件名称，然后解压。例如以下：

def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
    zip_file.close()


def get_parser():
    parser = argparse.ArgumentParser(description='replace of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='work_dir')
    return parser 

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['work_dir'][0]
    # work_dir = "C:/Users/LIUBR/Desktop/New folder"

    batch_unzip(work_dir)
  

if __name__ == '__main__':
    main()

