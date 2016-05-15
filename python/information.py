# http://apps.ecmwf.int/codes/grib/param-db/?id=228

#Convective precipitation + stratiform precipitation (CP +LSP). Accumulated field.


a=np.array([[1,2,3],[4,5,6]])



In [164]: a
Out[164]: 
array([[1, 2, 3],
       [4, 5, 6]])


In [177]: a[:,0:2]
Out[177]: 
array([[1, 2],
       [4, 5]])

# warning: lons[mask_ge_180] lost its shape 
#http://stackoverflow.com/questions/29046162/numpy-array-loss-of-dimension-when-masking
a=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

