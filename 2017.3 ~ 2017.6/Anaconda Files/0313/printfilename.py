# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:58:36 2017

@author: Administrator
"""

#import os
# 
#def GetFileList(dir, fileList):
#    newDir = dir
#    if os.path.isfile(dir):
#        fileList.append(dir.decode('gbk'))
#    elif os.path.isdir(dir):  
#        for s in os.listdir(dir):
#            #如果需要忽略某些文件夹，使用以下代码
#            #if s == "xxx":
#                #continue
#            newDir=os.path.join(dir,s)
#            GetFileList(newDir, fileList)  
#    return fileList
# 
#list = GetFileList('F:\170114\249', [])
#
#for e in list:
#    print e
#

#import os
#
## 遍历指定目录，显示目录下的所有文件名
#def eachFile(filepath):
#    pathDir =  os.listdir(filepath)
#    for allDir in pathDir:
#        child = os.path.join('%s%s' % (filepath, allDir))
#        print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
#
## 读取文件内容并打印
#def readFile(filename):
#    fopen = open(filename, 'r') # r 代表read
#    for eachLine in fopen:
#        print "读取到得内容如下：",eachLine
#    fopen.close()
#    
#    
#filepath = 'F:\170114\249'
#readFile(filepath)



import os  
path = 'F:\170114\249' #文件夹目录  
files= os.listdir(path) #得到文件夹下的所有文件名称  
s = []  
for file in files: #遍历文件夹  
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
          f = open(path+"/"+file); #打开文件  
          iter_f = iter(f); #创建迭代器  
          str = ""  
          for line in iter_f: #遍历文件，一行行遍历，读取文本  
              str = str + line  
          s.append(str) #每个文件的文本存到list中  
print s #打印结果  