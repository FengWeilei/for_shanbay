# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:29:07 2017

@author: Administrator
"""

import h5py
import numpy as np

f = h5py.File('C:\Users\Administrator\Desktop\oco2_L2StdND_00958a_140906_B7000r_150715102321.h5',"r")
f.keys()
ret_result = f["RetrievalResults"]
xco2 = ret_result["xco2"][:]    ## xco2数组
import pylab
pylab.figure(1)
pylab.plot(xco2)
pylab.show()