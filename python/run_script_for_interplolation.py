import os

execfile(os.path.expanduser('~')+"/Dropbox/scripts/github/ecmwf_reader/python/read_hdf5.py")
execfile(os.path.expanduser('~')+"/Dropbox/scripts/github/ecmwf_reader/python/translate_longititude.py")
execfile(os.path.expanduser('~')+"/Dropbox/scripts/github/ecmwf_reader/python/class_station.py")
a=Station('asdf')
a.find_lats_lons_idx_from_mtx(lats,lons) 
a.extract_value_at_stations(evap_yearly_raw,rain_yearly_raw,lats,lons,day_count_yearly
        ,evap_total_rate_mmday,rain_total_rate_mmday)
a.interpolate_values_as_mtx(lats,lons)
#a.plot_interpolated_annual_avg_result()
a.plot_interpolated_total_avg_result()
a.output_csv_for_station()




#aaa=[np.array([1,2,3]),np.array([4,5,6])]
