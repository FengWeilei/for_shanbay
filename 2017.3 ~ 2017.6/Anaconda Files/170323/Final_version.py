# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:37:40 2017

@author: Administrator
"""

import netCDF4 as nc  
from netCDF4 import Dataset

#import os
#file_name = []
#str_file = 'F:\\tccon'
#for dirpaths,dirnames, filenames in os.walk(str_file):
#    for filename in filenames:
#        file_name.append(str_file + '\\' + filename)
#print file_name





#for i in file_name:
#    nc_obj=Dataset(i)
#    long_deg = nc_obj.variables["long_deg"][:]
#    lat_deg = nc_obj.variables['lat_deg'][:]
#    print 'The site', i , 'has a longitude' , str(sum(long_deg)/len(long_deg))
#    print 'The site', i , 'has a latitude' , str(sum(lat_deg)/len(lat_deg))
#    print '--'*30
    

import h5py
import numpy as np

import os
file_name=[]
#str_file=os.getcwd()#当前脚本路径
str_file = 'H:\\save\\201603\\080'
print str_file
for dirpaths, dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        if ".h5.xml" in filename:
            filename=filename.split(".h5.xml")[0]#以“.h5,xml”为分割点获取文件名
            file_name.append(str_file+"\\"+filename+'.h5')
#print file_name

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
    
        if -119.63 < longitude[i] < -116.63 and 32.64 < latitude[i] < 35.64 :
            sub_xco2.append(xco2[i])
            sub_time.append(time_string[i])
            
        
    else:
        print 'oops'



try:
    print sub_time[0]
    print sub_time[-1]
    print (sum(sub_xco2)/len(sub_xco2))*1000000
    print len(sub_xco2)
except:
    ZeroDivisionError

