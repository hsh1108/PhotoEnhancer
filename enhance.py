from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os, glob 
from TF import *

def main():
    input_dir = 'images/input/'
    for img_name in os.listdir(input_dir):
        file_out_no_ext = img_name[:-4]
        file_name = getInputPhoto(img_name)
        processImg(file_name , file_out_no_ext)

if __name__ == '__main__':
    main()
