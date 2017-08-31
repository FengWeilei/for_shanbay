# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:58:36 2017

@author: Administrator
"""

import os
dir="e:\\"
for root,dirs,files in os.walk(dir):
    for file in files:
        print os.path.join(root,file)

#import os  ,sys
#path = 'F:\170114\249' #文件夹目录  
#files= os.listdir(path) #得到文件夹下的所有文件名称  
#s = []  
#for file in files: #遍历文件夹  
#     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
#          f = open(path+"/"+file); #打开文件  
#          iter_f = iter(f); #创建迭代器  
#          str = ""  
#          for line in iter_f: #遍历文件，一行行遍历，读取文本  
#              str = str + line  
#          s.append(str) #每个文件的文本存到list中  
#print s #打印结果  

#>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符 
 #>>>FileList=GetFileList(FindPath,FlagStr) # 
 ''' 
 import os 
 FileList=[] 
 FileNames=os.listdir(FindPath) 
 if (len(FileNames)>0): 
  for fn in FileNames: 
   if (len(FlagStr)>0): 
    #返回指定类型的文件名 
    if (IsSubString(FlagStr,fn)): 
     fullfilename=os.path.join(FindPath,fn) 
     FileList.append(fullfilename) 
   else: 
    #默认直接返回所有文件名 
    fullfilename=os.path.join(FindPath,fn) 
    FileList.append(fullfilename) 