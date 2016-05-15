# this script translates the latitude greater than 180 to the left hand side of
# the matrix. by this way the data becomes consistent with Tao's data.
mask_ge_180=lons>=180
mask_lt_180=lons<180

lons[mask_ge_180]=lons[mask_ge_180]-360

# warning: lons[mask_ge_180] lost its shape 
#http://stackoverflow.com/questions/29046162/numpy-array-loss-of-dimension-when-masking

split_idx=257
lons=np.column_stack((lons[:,split_idx:],  lons[:,:split_idx] ))


evap_total_rate_mmday=np.column_stack((evap_total_rate_mmday[:,split_idx:],
    evap_total_rate_mmday[:,:split_idx]))
rain_total_rate_mmday=np.column_stack((rain_total_rate_mmday[:,split_idx:],
    rain_total_rate_mmday[:,:split_idx]))

for n in np.arange(rain_yearly_raw.shape[2]):
    rain_yearly_raw[:,:,n]=np.column_stack((rain_yearly_raw[:,split_idx:,n],rain_yearly_raw[:,:split_idx,n]))
    evap_yearly_raw[:,:,n]=np.column_stack((evap_yearly_raw[:,split_idx:,n],evap_yearly_raw[:,:split_idx,n]))

with h5py.File('data_trans.h5', 'w') as hf:
    hf.create_dataset('evap_total_rate_mmday', data=evap_total_rate_mmday)
    hf.create_dataset('rain_total_rate_mmday', data=rain_total_rate_mmday)
    hf.create_dataset('lats', data=lats)
    hf.create_dataset('lons', data=lons)
    hf.create_dataset('evap_yearly_raw', data=evap_yearly_raw)
    hf.create_dataset('rain_yearly_raw', data=rain_yearly_raw)
    hf.create_dataset('day_count_yearly', data=day_count_yearly)



    
