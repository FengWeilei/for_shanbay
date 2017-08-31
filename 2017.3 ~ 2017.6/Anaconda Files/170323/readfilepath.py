# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:09:07 2017

@author: Administrator
"""

#import os
#file_name=[]
##str_file=os.getcwd()#当前脚本路径
#str_file = 'F:\\170114\\249'
#for dirpaths, dirnames, filenames in os.walk(str_file):
#    for filename in filenames:
#        if ".h5.xml" in filename:
#            filename=filename.split(".h5.xml")[0]#以“.”为分割点获取文件名
#            file_name.append(filename+'.h5')
#print file_name


import os
file_name = []
str_file = 'F:\\tccon'
for dirpaths,dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        file_name.append(str_file + '\\' + filename)
print file_name





#import os
#file_name = []
#file_path = 'F:\\170114\\249'
#for dirpaths, dirnames, filenames in os.walk(file_path):
#    for filename in filenames: 
#        file_name.append(filename)
#print file_name