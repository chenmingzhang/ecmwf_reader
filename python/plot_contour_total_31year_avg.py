# this file saves average result for the grb file requires
# tricks for evaporation data: the evaporation data is given at 3/6/9/12/18/24 hour time of the day,
# each value at the point is the cumulative evaporation 
import numpy as np
import matplotlib.pyplot as plt
import datetime
#for n in [0,1,2,3,4,5]:

#grbs_evap.seek(0)
#grbs_rain.seek(0)
#no_evap=0
#evp_max=0
#evp_min=0
#f  = ('output_file_test.txt','w')
#for n in grbs_evap:
#    no_evap+=1
#    grb_evap_current = grbs_evap.read(1)[0]
#    print str(no_evap) , str(grb_evap_current)
#    f.write( str(no_evap ), grb_evap_current)
#    evap= grb_evap_current.values
#    evp_max=np.amin([np.amax(evap),evp_min])
#    evp_min=np.amin([np.amin(evap),evp_min])
#
#print 'Total evaporation data numer is',str(no_evap)
#
#no_rain=0
#for n in grbs_rain:
#    no_rain+=1
#    grb_evap_current = grbs_rain.read(1)[0]
#    evap= grb_evap_current.values
#    evp_max=np.amin([np.amax(evap),evp_min])
#    evp_min=np.amin([np.amin(evap),evp_min])
#print 'Total evaporation data numer is',str(no_rain)


grbs_evap.seek(0)
grbs_rain.seek(0)


month_previous=1
evap_total_raw=0
rain_total_raw=0
#for n in grbs_evap:
#for n in [0,1,2,3,4,5,6,7]:
# it is found that using the previous method can not get the size of the each grib object.
no_years=32
no_evap=2190*no_years
no_rain=2190*no_years
year_initial=1979
#for n in np.arange(no_evap):
#for n in np.arange(186):
day_count_all=0
evap_yearly_raw  = np.empty([256,512,no_years],dtype=float)
rain_yearly_raw  = np.empty([256,512,no_years],dtype=float)
day_count_yearly = np.empty(no_years,dtype=float)

datetime_ay=np.empty(no_evap,dtype=object)

for n in np.arange(no_evap):
    grb_evap_current = grbs_evap.read(1)[0]
    data_date=grb_evap_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_evap_current.__getattribute__('endStep'))
    datetime_ay[n]=data_date
    grb_rain_current = grbs_rain.read(1)[0]
    data_date_rain=grb_rain_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_rain_current.__getattribute__('endStep'))
    date_current=int(data_date.strftime("%d"))
    month_current=int(data_date.strftime("%m"))
    year_current=int(data_date.strftime("%Y"))
    evap= grb_evap_current.values  # (256, 512)
    rain= grb_rain_current.values  # (256, 512)
    if grb_rain_current.__getattribute__('endStep') ==24:
        day_count_all+=1
        print 'n='+str(n)+', day_count_all= '+str(day_count_all)+', year_month='+data_date.strftime("%y_%m")+', month='+str(month_current)
        evap_total_raw=evap_total_raw+evap
        rain_total_raw=rain_total_raw+rain
        evap_yearly_raw[:,:,year_current-year_initial]=evap_yearly_raw[:,:,year_current-year_initial]+evap
        rain_yearly_raw[:,:,year_current-year_initial]=rain_yearly_raw[:,:,year_current-year_initial]+rain
        day_count_yearly[year_current-year_initial]+=1

evap_total_rate_mmday=-evap_total_raw*1000/day_count_all    # convert from negative m per day to positive mm per day
rain_total_rate_mmday=rain_total_raw*1000/day_count_all    # convert from negative m per day to positive mm per day

lats, lons = grb_evap_current.latlons()  # (256, 512)
lons=lons
fig=plt.figure(figsize=(20,25))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
#
im=ax1.contourf(lons,lats,evap_total_rate_mmday) #,levels=v)
ax1.set_ylabel('latitude')
ax1.set_title('Average Evaporation (mm/day) over 32 years')
fig.colorbar(im,ax=ax1) #,ticks=v)
#
im=ax2.contourf(lons,lats,rain_total_rate_mmday)
ax2.set_ylabel('latitude')
ax2.set_title('Average Precipitation (mm/day) over 32 years')
fig.colorbar(im,ax=ax2)
#print 'the max rain is: '+str(np.max(rain_total))+'m, minimum evap is: '+ str(np.min(rain_total))+' m'
#
im=ax3.contourf(lons,lats,evap_total_rate_mmday-rain_total_rate_mmday)
ax3.set_title('Average Evaporation-precipitation (mm/day) over 32 years')
ax3.set_ylabel('latitude')
ax3.set_xlabel('longitude')
#ax3.set_title('Precipitation + evaporation (m) at UTC time: '
#    +unicode(data_date)+ ' or Beijing time:'
#    +unicode(data_date+datetime.timedelta(hours=+8) ))
fig.colorbar(im,ax=ax3)
#fig.show()
#
fig_name='average_evaporatoin_rain_for_all.png'
fig.savefig(fig_name,format='png')
plt.close(fig)


#with h5py.File('data.h5', 'w') as hf:
#    hf.create_dataset('evap_total_rate_mmday', data=evap_total_rate_mmday)
#    hf.create_dataset('rain_total_rate_mmday', data=rain_total_rate_mmday)
#    hf.create_dataset('lats', data=lats)
#    hf.create_dataset('lons', data=lons)
#    hf.create_dataset('evap_yearly_raw', data=evap_yearly_raw)
#    hf.create_dataset('rain_yearly_raw', data=rain_yearly_raw)
#    hf.create_dataset('day_count_yearly', data=day_count_yearly)

#evap_total_rate_mmday=-rain_total_raw*1000/day_count_all    # convert from negative m per day to positive mm per day
#rain_total_rate_mmday=evap_total_raw*1000/day_count_all    # convert from negative m per day to positive mm per day


np.savetxt('total_32_avg_evap_mmday.csv',evap_total_rate_mmday , delimiter=",")
np.savetxt('total_32_avg_rain_mmday.csv', rain_total_rate_mmday, delimiter=",")
np.savetxt('total_32_avg_net_evap_mmday.csv',
    evap_total_rate_mmday-rain_total_rate_mmday, delimiter=",")
