import h5py
import numpy as np
import matplotlib.pyplot as plt
import datetime

with h5py.File('data.h5','r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    evap_total_rate_mmday=np.array(hf.get('evap_total_rate_mmday'))
    rain_total_rate_mmday=np.array(hf.get('rain_total_rate_mmday'))
    lats=np.array(hf.get('lats'))
    lons=np.array(hf.get('lons'))
    evap_yearly_raw=np.array(hf.get('evap_yearly_raw'))
    rain_yearly_raw=np.array(hf.get('rain_yearly_raw'))
    day_count_yearly=np.array(hf.get('day_count_yearly'))

#fig=plt.figure(figsize=(20,25))
#ax1 = fig.add_subplot(311)
#ax2 = fig.add_subplot(312)
#ax3 = fig.add_subplot(313)
##
#im=ax1.contourf(lons,lats,evap_total_rate_mmday) #,levels=v)
#ax1.set_ylabel('latitude')
#ax1.set_title('Average Evaporation (mm/day) over 32 years')
#fig.colorbar(im,ax=ax1) #,ticks=v)
##
#im=ax2.contourf(lons,lats,rain_total_rate_mmday)
#ax2.set_ylabel('latitude')
#ax2.set_title('Average Precipitation (mm/day) over 32 years')
#fig.colorbar(im,ax=ax2)
##print 'the max rain is: '+str(np.max(rain_total))+'m, minimum evap is: '+ str(np.min(rain_total))+' m'
##
#v = np.linspace(-15,8, 24, endpoint=True)
#im=ax3.contourf(lons,lats,evap_total_rate_mmday-rain_total_rate_mmday,levels=v)
#ax3.set_title('Average Evaporation-precipitation (mm/day) over 32 years')
#ax3.set_ylabel('latitude')
#ax3.set_xlabel('longitude')
##ax3.set_title('Precipitation + evaporation (m) at UTC time: '
##    +unicode(data_date)+ ' or Beijing time:'
##    +unicode(data_date+datetime.timedelta(hours=+8) ))
#fig.colorbar(im,ax=ax3,ticks=v)
##fig.show()
##
#fig_name='average_evaporatoin_rain_for_all.png'
#fig.savefig(fig_name,format='png')
#plt.close(fig)
#
#
#
#
#for n in np.arange(32): 
#    evap_yearly_mmday=-evap_yearly_raw[:,:,n]*1000/day_count_yearly[1,1,n]
#    rain_yearly_mmday=-rain_yearly_raw[:,:,n]*1000/day_count_yearly[1,1,n]
#    print 'now it is year'+str(n+1979)
#
#    fig=plt.figure(figsize=(20,25))
#    ax1 = fig.add_subplot(311)
#    ax2 = fig.add_subplot(312)
#    ax3 = fig.add_subplot(313)
#    #
#    im=ax1.contourf(lons,lats,evap_yearly_mmday) #,levels=v)
#    ax1.set_ylabel('latitude')
#    ax1.set_title('Average Evaporation (mm/day) for year'+str(n+1979))
#    fig.colorbar(im,ax=ax1) #,ticks=v)
#    #
#    im=ax2.contourf(lons,lats,rain_yearly_mmday)
#    ax2.set_ylabel('latitude')
#    ax2.set_title('Average Precipitation (mm/day) for year'+str(n+1979))
#    fig.colorbar(im,ax=ax2)
#    #print 'the max rain is: '+str(np.max(rain_total))+'m, minimum evap is: '+ str(np.min(rain_total))+' m'
#    #
#    v = np.linspace(-15,8, 24, endpoint=True)
#    im=ax3.contourf(lons,lats,evap_yearly_mmday-rain_yearly_mmday)
#    ax3.set_title('Average Evaporation-precipitation (mm/day) for year'+str(n+1979))
#    ax3.set_ylabel('latitude')
#    ax3.set_xlabel('longitude')
#    #ax3.set_title('Precipitation + evaporation (m) at UTC time: '
#    #    +unicode(data_date)+ ' or Beijing time:'
#    #    +unicode(data_date+datetime.timedelta(hours=+8) ))
#    fig.colorbar(im,ax=ax3,ticks=v)
#    #fig.colorbar(im,ax=ax3)
#    #fig.show()
#    #
#    fig_name='average_evap_rain_for_'+str(n+1979)+'.png'
#    fig.savefig(fig_name,format='png')
#    plt.close(fig)
