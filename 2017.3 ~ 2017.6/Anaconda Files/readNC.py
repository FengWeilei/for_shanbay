# -*- coding: cp936 -*-
#import netCDF4 as nc  
from netCDF4 import Dataset
import pylab
nc_obj=Dataset("F:\\tccon\\iz20070518_20160217.public.nc") 

xco2 = nc_obj.variables['xco2_ppm'][:]
day = nc_obj.variables["day"][:]
year = nc_obj.variables['year'][:]
long_deg = nc_obj.variables["long_deg"][:]
lat_deg = nc_obj.variables['lat_deg'][:]
hour = nc_obj.variables["hour"][:]  ## create a list and store the nc_data

                       
## find the xco2 fit the day. and the hour 13:00??

Sub_xco2 = []
Sub_hour = []
for i in range(0,len(day)):
    if 2015 < year[i] <= 2016 \
                   and 47 < day[i] <= 48 and 13.75 < hour[i] < 14.76:
        Sub_xco2.append(xco2[i])
        Sub_hour.append(hour[i])
        
                      

#ave_xco2 = sum(xco2)/len(xco2)  ## write a function
def ave(haha):
    x= sum(haha)/len(haha)
    return x
try:
    print Sub_hour
    print ave(Sub_xco2)    
    print len(Sub_hour)
except:
    ZeroDivisionError


#print ave(long_deg)
#print ave(lat_deg)
#
#pylab.figure(1)
#pylab.plot(year)
#pylab.show()



