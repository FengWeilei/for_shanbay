
import numpy as np
temperature = np.random.random(1024)
#
#dt = 10.0   ##delta T  record temperature every 10.0 second
#start_time = 1375204299  ## in Unix time
#station = 15

## Use built-in function np.savez to store these values on disk

#np.savez("weather.npz",data = temperature,start_time = start_time,station = station)

#out = np.load("weather.npz")

#print out["data"]
#print out["start_time"]
#print out["station"]

#wind = np.random.random(2048)
#dt_wind = 5.0

import h5py
f = h5py.File("Weather.hdf5")
f["/15/temperature"] = temperature
f["/15/temperature"].attrs["dt"] = 10.0
f["/15/temperature"].attrs["start_time"] = 1375204299
#f["/15/wind"] = wind
#f["/15/wind"].attrs["dt"] = 5.0
 
#f["/20/temperature"] = temperature_fromstation_20 and so on"
dateset = f["/15/temperature"]
for key,value in dateset.attrs.iteritems():
    print "%s: %s" % (key,value)
     
 
 
