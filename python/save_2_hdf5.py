# this file saves the files back to hdf5
import h5py
import numpy as np
import matplotlib.pyplot as plt
import datetime

#with h5py.File('data.h5','r') as hf:
#    print('List of arrays in this file: \n', hf.keys())
#    evap_total_rate_mmday=np.array(hf.get('evap_total_rate_mmday'))
#    rain_total_rate_mmday=np.array(hf.get('rain_total_rate_mmday'))
#    lats=np.array(hf.get('lats'))
#    lons=np.array(hf.get('lons'))
#    evap_yearly_raw=np.array(hf.get('evap_yearly_raw'))
#    rain_yearly_raw=np.array(hf.get('rain_yearly_raw'))
#    day_count_yearly=np.array(hf.get('day_count_yearly'))

with h5py.File('data.h5', 'w') as hf:
    hf.create_dataset('evap_total_rate_mmday', data=evap_total_rate_mmday)
    hf.create_dataset('rain_total_rate_mmday', data=rain_total_rate_mmday)
    hf.create_dataset('lats', data=lats)
    hf.create_dataset('lons', data=lons)
    hf.create_dataset('evap_yearly_raw', data=evap_yearly_raw)
    hf.create_dataset('rain_yearly_raw', data=rain_yearly_raw)
    hf.create_dataset('day_count_yearly', data=day_count_yearly)
