# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 20:38:25 2017

@author: Administrator
"""

def isPal(x):
    temp = x[:]
    temp.reverse()
    
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = raw_input("Enter element:")
        result.append(elem)
    if isPal(result):
        print "Yes"
    else:
        print "No"
    