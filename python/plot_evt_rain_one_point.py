# this script plots evaporation and rainfall in brisbane
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime
import operator


ms2mmday=1000*3600*24

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

# go to the beginning
grbs_evap.seek(0)
grbs_rain.seek(0)

# find out the location where brisbane is.
brisbane_lat=-27.4710
brisbane_lon=153.0234 
grb_evap_current = grbs_evap.read(1)[0]
lats, lons = grb_evap_current.latlons()  # (256, 512)

brisbane_lat_idx, min_value = min(enumerate(abs(lats[:,1]-(brisbane_lat))), key=operator.itemgetter(1))
brisbane_lon_idx, min_value = min(enumerate(abs(lons[1,:]-(brisbane_lon))), key=operator.itemgetter(1))

fig=plt.figure(figsize=(20,15))
plt.plot(brisbane_lon,brisbane_lat,'ro')
plt.plot(lons[brisbane_lat_idx,brisbane_lon_idx],lats[brisbane_lat_idx,brisbane_lon_idx],'go')
plt.plot(lons[brisbane_lat_idx,brisbane_lon_idx-1],lats[brisbane_lat_idx,brisbane_lon_idx-1],'bo')
#fig.show()

# to ensure this is a land evaporation
brisbane_lon_idx=brisbane_lon_idx-1;


grbs_evap.seek(0)
grbs_rain.seek(0)

date_previous=1
evap_daily=0
rain_daily=0
no_evap=2189  # this is a hard coding point
no_rain=2189 # this is also a hard coding point
#for n in np.arange(no_evap):
brisbane_evap_rate=np.empty(no_evap,dtype=float)
brisbane_rain_rate=np.empty(no_evap,dtype=float)
time_digi_ay      =np.empty(no_evap,dtype=float)
brisbane_evap_raw =np.empty(no_evap,dtype=float)
brisbane_rain_raw =np.empty(no_evap,dtype=float)
brisbane_datetime =np.empty(no_evap,dtype=object)


for n in np.arange(100):

    print str(n)
    grb_evap_current = grbs_evap.read(1)[0]
    data_date_evap=grb_evap_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_evap_current.__getattribute__('endStep'))
    #date_current=int(data_date_evap.strftime("%d"))

    grb_rain_current = grbs_rain.read(1)[0]
    data_date_evap_rain=grb_rain_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_rain_current.__getattribute__('endStep'))
    
    brisbane_evap_previous_step =grb_evap_current.values[brisbane_lat_idx,brisbane_lon_idx]
    brisbane_rain_previous_step =grb_rain_current.values[brisbane_lat_idx,brisbane_lon_idx]

    brisbane_evap_raw[n] =grb_evap_current.values[brisbane_lat_idx,brisbane_lon_idx]
    brisbane_rain_raw[n] =grb_rain_current.values[brisbane_lat_idx,brisbane_lon_idx]

    brisbane_datetime[n] = data_date_evap

    #print 'Processing time'+ unicode(data_date_evap_rain)
    if grb_evap_current.__getattribute__('endStep')==3:
        brisbane_evap_rate[n] = -brisbane_evap_raw[n]/3/3600*ms2mmday 
        brisbane_rain_rate[n] = brisbane_rain_raw[n]/3/3600*ms2mmday
    #elif grb_evap_current.__getattribute__('validityTime')==600:
    else:
        delta_time=(brisbane_datetime[n]- brisbane_datetime[n-1]).seconds
        brisbane_evap_rate[n] = -(brisbane_evap_raw[n]-brisbane_evap_raw[n-1])/delta_time*ms2mmday
        brisbane_rain_rate[n] = (brisbane_rain_raw[n]-brisbane_rain_raw[n-1])/delta_time*ms2mmday


    time_digi_ay[n]       =dates.date2num(data_date_evap_rain)

    print grb_rain_current,str(brisbane_evap_rate[n])
    print str(data_date_evap_rain)
   


fig=plt.figure(figsize=(20,15))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
plt_no=100
ax1.plot(brisbane_datetime[0:plt_no]+datetime.timedelta(hours=10),brisbane_evap_rate[0:plt_no],'ro-')
ax1.set_ylabel('evap (mm/day)')
ax1.set_xlabel('Brisbane time')

ax2.plot(brisbane_datetime[0:plt_no]+datetime.timedelta(hours=10),brisbane_rain_rate[0:plt_no],'ro-')
ax2.set_ylabel('rain (mm/day)')
ax2.set_xlabel('Brisbane time')
ax3.plot(brisbane_datetime[0:plt_no]+datetime.timedelta(hours=10),
brisbane_evap_rate[0:plt_no]-brisbane_rain_rate[0:plt_no],'ro-')
ax3.set_ylabel('evap-rain (mm/day)')
ax3.set_xlabel('Brisbane time')

fig.show()
fig_name='brisbane_evt_rain_plot.png'
fig.savefig(fig_name,format='png')
plt.close(fig)




    #rain= grb_rain_current.values  # (256, 512)
    
    #brisbane_evap=brisbane_evap;evap[brisbane_lat_idx,brisbane_lon_idx];
    
    #c=np.concatenate((a,b),axis=0)

#    else:
#        print 'Processing time'+ unicode(data_date_evap)+ ', drawing new graph' 
#        lats, lons = grb_evap_current.latlons()  # (256, 512)
#        fig=plt.figure(figsize=(20,15))
#        ax1 = fig.add_subplot(311)
#        ax2 = fig.add_subplot(312)
#        ax3 = fig.add_subplot(313)
#        
#        
#        v = np.linspace(-0.1,0.1, 21, endpoint=True)
#        im=ax1.contourf(lons,lats,evap_daily,levels=v)
#        ax1.set_ylabel('latitude')
#        ax1.set_xlabel('longitude')
#        ax1.set_title('Evaporation (m) at UTC time: '
#            +unicode(data_date_evap)+ ' or Beijing time:'
#            +unicode(data_date_evap+datetime.timedelta(hours=+8) ))
#        fig.colorbar(im,ax=ax1,ticks=v)
#        print 'the max evap is: '+str(np.max(evap_daily))+'m, minimum evap is: '+ str(np.min(evap_daily))+' m'
#
#
#        lats, lons = grb_rain_current.latlons()  # (256, 512)
#        im=ax2.contourf(lons,lats,rain_daily)
#        ax2.set_ylabel('latitude')
#        ax2.set_xlabel('longitude')
#        ax2.set_title('Precipitation (m) at UTC time: '
#            +unicode(data_date_evap_rain)+ ' or Beijing time:'
#            +unicode(data_date_evap_rain+datetime.timedelta(hours=+8) ))
#        fig.colorbar(im,ax=ax2)
#        print 'the max rain is: '+str(np.max(rain_daily))+'m, minimum evap is: '+ str(np.min(rain_daily))+' m'
#
#        #print 'Processing time'+ unicode(data_date_evap_rain)+ ', for precipitation finished'+str(lats.shape)
#
#        im=ax3.contourf(lons,lats,evap_daily-rain_daily)
#        ax3.set_ylabel('latitude')
#        ax3.set_xlabel('longitude')
#        ax3.set_title('Precipitation + evaporation (m) at UTC time: '
#            +unicode(data_date_evap)+ ' or Beijing time:'
#            +unicode(data_date_evap+datetime.timedelta(hours=+8) ))
#        fig.colorbar(im,ax=ax3)
#
#        evap_daily=evap
#        rain_daily=rain
#        date_previous=date_current
#
#
#
#        fig_name='daily_evp_rain_'+data_date_evap_previous_step.strftime('%Y_%m_%d')+'.png'
#        fig.savefig(fig_name,format='png')
#        plt.close(fig)



