# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 22:54:08 2017

@author: Administrator
"""

import h5py
import numpy as np

f = h5py.File('C:\Users\Administrator\Desktop\oco2_L2StdND_00958a_140906_B7000r_150715102321.h5',"r")
f.keys()
ret_result = f["RetrievalResults"]
xco2 = ret_result["xco2"][:]    ## xco2数组



#for i in xco2:
#    print i

f.close()


import os
 
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList
 
list = GetFileList('F:\170114\249', [])
for e in list:
    print e







#f.close()
##dataset = file["RetrievalResults"]
##for co2 in dataset.attr.iteritems():
##    print xco2
#

#xco2 = File.attrs.iteritems(xco2)
#print xco2                   
#file.close()
#
##table=tables.open_file('QTSQuotationTicks-20150304.h5','r')
##tick=table.root.TblMarket
#
#f = h5py.File('HDF5_FILE.h5','r')   #打开h5文件  
#f.keys()                            #可以查看所有的主键  
#a = f['data'][:]                    #取出主键为data的所有的键值  
#f.close()  