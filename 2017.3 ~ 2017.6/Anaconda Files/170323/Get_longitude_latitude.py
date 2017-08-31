# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:45:28 2017

@author: Administrator
"""

#import netCDF4 as nc  
from netCDF4 import Dataset

import os
file_name = []
str_file = 'F:\\tccon'
for dirpaths,dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        file_name.append(str_file + '\\' + filename)
#print file_name


for i in file_name:
    nc_obj=Dataset(i)
    long_deg = nc_obj.variables["long_deg"][:]
    lat_deg = nc_obj.variables['lat_deg'][:]
    year = nc_obj.variables['year'][:]
    print 'The site', i , 'has a longitude' , str(sum(long_deg)/len(long_deg))
    print str((sum(long_deg)/len(long_deg))-1.5)
    print ((sum(long_deg)/len(long_deg))+1.5)
    print 'The site ', i , 'has a latitude' , str(sum(lat_deg)/len(lat_deg))
    print str((sum(lat_deg)/len(lat_deg))-1.5)
    print str((sum(lat_deg)/len(lat_deg))+1.5)
    print 'max(year):',max(year)
    print 'min(year):',min(year)
    print '--'*30
    
