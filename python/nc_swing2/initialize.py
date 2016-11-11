import os
import numpy as np
import py_compile
import sys
import matplotlib.pyplot as plt
a=1
del a
#os.path.dirname(os.path.realpath(__file__))
current_path=os.getcwd()
#path_column_roof='/home/chenming/Dropbox/tailing_column/data/column_on_roof/'
#file_list_column_roof=os.listdir(current_path+'/data/column_on_roof/')
path_data_column_roof=current_path+'/data/column_on_roof/'
#execfile('class_scale.py')
sys.path.append(current_path+'/python/')
sys.path.append(current_path+'/python/')
py_compile.compile(current_path+'/class_cam2.py')
import class_cam2
reload(class_cam2)
a=class_cam2.cam2('/home/chenming/gis_swing_nasa/free.cam2.h0.exp0.2002.nc')


a.plot_vapor_contour()


a.get_coastlines(npts_min=80) # the minimum points in the system
#for i in len(a.coastal_segments):
a.plot_continent(continent_id=1)

a.find_city_locations()
a.append_nc_files( '/home/chenming/gis_swing_nasa/'    )
a.extracting_city_variable_over_time()
a.plot_wind_rose_at_cities(datatype=['UINT','VINT'])


self=a

#a=class_scale.scale(path_data_column_roof+'scale_2016_Jul_03.dat')
#a.surf_area1=np.pi*(0.265/2)**2
#self=a


#for n in np.arange(len(file_list_column_roof)):
#    a.append_file(path_data_column_roof+file_list_column_roof[n])
#
#a.export_data_as_csv('2016-06-25_2016-07-11.dat')
##a.spline_scale_readings(coef=0.001,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=0.0000001,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-8,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-10,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-13,time_interval_sec_sp=600)
#a.spline_scale_readings(coef=1e-14,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-15,time_interval_sec_sp=600)







####################################################################################################
#a.cities['los angeles']['latlon_idx']   #5718
#a.cities['los angeles']['latitude'] #34.0543942
#a.cities['los angeles']['longitude']  #241.75605919999998
#bb = a.file_lists['2002']['fn'].variables['UINT'][-1,:,:]
#a.lats_mtx.flat[5718]   #  34.882520993773461
#a.lons_mtx.flat[5718]   #  241.875
# # it is very close to losangeles
#
#a.lats_mtx.shape  #  (64, 128)
#len(a.lats_mtx[1])  # 128 which means rows first
#5718/128    # 44 row number
#np.remainder(5718,128)  # 86 column number
#
#a.lats_mtx[44,86]   # 34.882520993773461
# a.lons_mtx[44,86]  #  241.875
#
#
## the above are all correct
#
##  a.file_lists['1999']['fn'].variables['VINT'][2,44,86]
#
#
#bb.flat[5718]   #  340.77967443317175
#cc=np.array([[1,2,3,4],[5,6,7,8]])
#cc.flat[3]  # 4
#

