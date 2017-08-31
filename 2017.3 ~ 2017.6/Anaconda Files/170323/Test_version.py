# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:21:15 2017

@author: Administrator
"""

import h5py
import numpy as np

import os
file_name=[]
#str_file=os.getcwd()#当前脚本路径
str_file = 'H:\\save\\201502\\050'
for dirpaths, dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        if ".h5.xml" in filename:
            filename=filename.split(".h5.xml")[0]#以“.h5,xml”为分割点获取文件名
            file_name.append(str_file+"\\"+filename+'.h5')
print file_name