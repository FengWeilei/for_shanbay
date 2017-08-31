# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:43:54 2017

@author: Administrator
"""
import h5py
import numpy as np

import os
file_name=[]
#str_file=os.getcwd()#当前脚本路径
str_file = 'F:\\201501\\002'
for dirpaths, dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        if ".h5.xml" in filename:
            filename=filename.split(".h5.xml")[0]#以“.”为分割点获取文件名
            file_name.append(str_file+"\\"+filename+'.h5')
#print file_name

sub_xco2 = []
for j in file_name:
    f = h5py.File(j,"r")
    retrieval_result = f["RetrievalResults"]
    xco2 = retrieval_result["xco2"][:]    ## xco2数组
#    print len(xco2)
    retrieval_geometry = f['RetrievalGeometry']
    latitude = retrieval_geometry['retrieval_latitude'][:]
    longitude = retrieval_geometry['retrieval_longitude'][:]

    
    for i in range(0,len(xco2)):
        
        
        
#        print 'len(xco2) are',len(xco2)
#        print longitude[i]
    
        if 32.2 < latitude[i] < 36.2 and -120.18 < longitude[i] < -116.18 :
            sub_xco2.append(xco2[i])
        
    else:
        print 'oops'
#print i
#print sub_xco2        
def ave(haha):
    x= sum(haha)/len(haha)
    return x
print ave(sub_xco2)

















#t_xco2 = []
#for i in file_name:
#    f = h5py.File(i,"r")
#    f.keys()
#    ret_result = f["RetrievalResults"]
#    xco2 = ret_result["xco2"][:]    ## xco2数组
#    t_xco2.append(xco2)
#print t_xco2
    