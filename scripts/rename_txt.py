'''
code by zzg@2021/05/10
'''
import os.path as osp
import os
import numpy as np
import shutil
import re
import sys


for FLAG in range(2):
    if FLAG == 0:
        ##train
        src_dir = "/content/train_detrac_txt"    # labels
        dst_dir = "/content/dataset/labels/train/"    # satisfy the folder structure of YOLOv5 for training
    else:
        ##test
        src_dir = "/content/test_detrac_txt"    # labels
        dst_dir = "/content/dataset/labels/val/"    # satisfy the folder structure of YOLOv5 for training

    if not osp.exists(dst_dir):
        os.makedirs(dst_dir)

    seqs = [s for s in os.listdir(src_dir)]

    # rename txts
    for seq in seqs:
        path = osp.join(src_dir, seq)
        # print(path)
        fileList = os.listdir(path)
        os.chdir(path)

        for fileName in fileList:
            pat = ".+\.(txt|xml|json)"
            pattern = re.findall(pat, fileName)
            image_name = fileName.split(".")[0]
            os.rename(fileName, ('{}_{}.txt'.format(image_name, str(seq))))

        sys.stdin.flush()
        print("after rename：" + str(os.listdir(path)))
    print("txt rename finished!-----")

    # select txts
    j = 0
    for seq in seqs:
        path = osp.join(src_dir, seq)

        for root, dirs, files in os.walk(path):
            files = sorted(files)
            for i in range(len(files)):
                if i % 10 == 0:    # only pick 1/10 images
                    j += 1
                    if files[i][-3:] == 'txt':
                        file_path = path + '/' + files[i]
                        new_file_path = dst_dir + '/' + files[i]
                        shutil.copy(file_path, new_file_path)

                    if i % 100 == 0:
                        print(j)
    print("txt selection finished!------")
    # print(str(os.listdir(dst_dir)))