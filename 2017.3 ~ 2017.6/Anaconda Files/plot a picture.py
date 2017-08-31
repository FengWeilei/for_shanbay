# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:47:42 2017

@author: Administrator
"""


import numpy as np
import pylab as pl
import pandas as pd  
from sklearn import datasets, linear_model 

# Use numpy to load the data contained in the file
# 'SITE1.txt' into a 2-D array called data
#data = np.loadtxt('SITE1.txt')
#x = data[:,0]
#y = data[:,1]

from scipy import stats
import numpy as np
import pylab

## Function to get data  
def get_data(file_name):  
    data = pd.read_csv(file_name)  #here ,use pandas to read cvs file.  
    X_parameter = []  
    Y_parameter = []  
    for XCO2_HDF5 ,XCO2_TCCON in zip(data['HDF5'],data['TCCON']):
        X_parameter.append(XCO2_HDF5)#存储在相应的list列表中  
        Y_parameter.append(XCO2_TCCON) 
    return X_parameter,Y_parameter  

f = 'C:\Users\Administrator\Desktop\csv_SITE5.csv'
get_data(f)
df = pd.read_csv(f)
x = df['HDF5']
y = df['TCCON']

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)

predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)


X = [380,420]
Y = [380,420]
pylab.plot(X, Y)
# Plotting
pylab.plot(x, y, 'o')

pylab.plot(x, predict_y, 'k-')
pl.xlim(380, 420)# set axis limits
pl.ylim(380,420)
pylab.show()


#import pylab 
#import matplotlib.pyplot as plt  
#import numpy as np  
#import pandas as pd  
#from sklearn import datasets, linear_model  
#
### Function to get data  
##def get_data(file_name):  
##    data = pd.read_csv(file_name)  #here ,use pandas to read cvs file.  
##    X_parameter = []  
##    Y_parameter = []  
##    for XCO2_HDF5 ,XCO2_TCCON in zip(data['HDF5'],data['TCCON']):
##        X_parameter.append(XCO2_HDF5)#存储在相应的list列表中  
##        Y_parameter.append(XCO2_TCCON) 
##    return X_parameter,Y_parameter  
#
#f = 'C:\Users\Administrator\Desktop\csv_SITE5.csv'
##get_data(f)
#df = pd.read_csv(f)
##print(df)
#
#regr = linear_model.LinearRegression()
## 拟合
#regr.fit(df['HDF5'].reshape(-1, 1), df['TCCON'])
# # 注意此处.reshape(-1, 1)，因为X是一维的！
#
## 不难得到直线的斜率、截距
#a, b = regr.coef_, regr.intercept_
#
## 1.真实的点
##plt.scatter(df['HDF5'], df['TCCON'], color='blue')
#pl.plot(df['HDF5'], df['TCCON'], 'bo')
#
##plt.plot(df['HDF5'], regr.predict(df['HDF5'].reshape(-1,1)), color='red', linewidth=2)
#plt.xlim(380, 420)# set axis limits
#plt.ylim(380,420)
#X = [380,420]
#Y = [380,420]
#pylab.plot(X, Y)
#pl.title('SITE5')# give plot a title
#pl.xlabel('HDF5')# make axis labels
#pl.ylabel('TCCON')
#plt.show()










