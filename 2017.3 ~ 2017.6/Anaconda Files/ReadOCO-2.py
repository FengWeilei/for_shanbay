# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:36:10 2017

@author: Administrator
"""

import h5py
import os

#获取文件夹下后缀为.h5的文件名
file_name=[]
str_file = 'H:\\save\\201602\\048'
print str_file
for dirpaths, dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        if ".h5.xml" in filename:
            filename=filename.split(".h5.xml")[0]#以“.h5,xml”为分割点获取文件名
            file_name.append(str_file+"\\"+filename+'.h5')


sub_xco2 = []
sub_time = []
for j in file_name:
    f = h5py.File(j,"r")
    retrieval_result = f["RetrievalResults"]
    xco2 = retrieval_result["xco2"][:]    ## xco2数组
    
    retrieval_geometry = f['RetrievalGeometry']
    latitude = retrieval_geometry['retrieval_latitude'][:]
    longitude = retrieval_geometry['retrieval_longitude'][:]
    
    retrival_header = f['RetrievalHeader']
    time_string = retrival_header['retrieval_time_string'][:]

    
    for i in range(0,len(xco2)):
    
        if -17.98 < longitude[i] < -14.98 and 26.8 < latitude[i] < 29.8 :
            sub_xco2.append(xco2[i])
            sub_time.append(time_string[i])
      
        
    else:
        print '○○○'



try:
    print min(sub_time)
    print max(sub_time)
    print (sum(sub_xco2)/len(sub_xco2))*1000000
    print len(sub_xco2)
except:
    ZeroDivisionError
