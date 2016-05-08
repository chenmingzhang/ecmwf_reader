
import numpy as np
import matplotlib.pyplot as plt
import datetime
#for n in [0,1,2,3,4,5]:

#grbs_evap.seek(0)
#grbs_rain.seek(0)
#no_evp=0
#evp_max=0
#evp_min=0
#f  = ('output_file_test.txt','w')
#for n in grbs_evap:
#    no_evp+=1
#    grb1 = grbs_evap.read(1)[0]
#    print str(no_evp) , str(grb1)
#    f.write( str(no_evp ), grb1)
#    evap= grb1.values
#    evp_max=np.amin([np.amax(evap),evp_min])
#    evp_min=np.amin([np.amin(evap),evp_min])
#
#print 'Total evaporation data numer is',str(no_evp)
#
#no_rain=0
#for n in grbs_rain:
#    no_rain+=1
#    grb1 = grbs_rain.read(1)[0]
#    evap= grb1.values
#    evp_max=np.amin([np.amax(evap),evp_min])
#    evp_min=np.amin([np.amin(evap),evp_min])
#print 'Total evaporation data numer is',str(no_rain)


grbs_evap.seek(0)
grbs_rain.seek(0)

#grbs_evap.seek(2000)
#grbs_rain.seek(2000)

date_previous=1
month_previous=1
evap_monthly=0
rain_monthly=0
#for n in grbs_evap:
#for n in [0,1,2,3,4,5,6,7]:
# it is found that using the previous method can not get the size of the each grib object.
no_evp=2189
no_rain=2189
for n in np.arange(no_evp):
#for n in np.arange(186):


    grb1 = grbs_evap.read(1)[0]
    data_date=grb1.__getattribute__('analDate')+datetime.timedelta(hours=grb1.__getattribute__('validityTime')/100)

    grb2 = grbs_rain.read(1)[0]
    data_date_rain=grb2.__getattribute__('analDate')+datetime.timedelta(hours=grb2.__getattribute__('validityTime')/100)
    
    date_current=int(data_date.strftime("%d"))
    month_current=int(data_date.strftime("%m"))

    print str(n)+str(month_current)+str(month_previous)
    if (n+1!=no_evp and month_current==month_previous): # same day
        print 'Processing time'+ unicode(data_date)+ ', in a same month as previous month, which is '+ str(month_previous)
        evap= grb1.values  # (256, 512)
        evap_monthly=evap_monthly+evap
        rain= grb2.values  # (256, 512)
        rain_monthly=rain_monthly+rain
        data_date_previous_step=data_date_rain


    elif ((n+1==no_evp and month_current==month_previous) or month_current!=month_previous):
        print 'Processing time'+ unicode(data_date)+ ', reached a new month. now drawing new graph' 
        lats, lons = grb1.latlons()  # (256, 512)
        fig=plt.figure(figsize=(20,15))
        ax1 = fig.add_subplot(311)
        ax2 = fig.add_subplot(312)
        ax3 = fig.add_subplot(313)
        
        
        v = np.linspace(-0.04,0.04, 21, endpoint=True)

        days_in_this_month=int(data_date_previous_step.strftime("%d"))
        
        evap_monthly=evap_monthly/days_in_this_month
        rain_monthly=rain_monthly/days_in_this_month


        im=ax1.contourf(lons,lats,evap_monthly,levels=v)
        ax1.set_ylabel('latitude')
        ax1.set_xlabel('longitude')
        ax1.set_title('Evaporation (m) at UTC time: '
            +unicode(data_date)+ ' or Beijing time:'
            +unicode(data_date+datetime.timedelta(hours=+8) ))
        fig.colorbar(im,ax=ax1,ticks=v)
        print 'the max evap is: '+str(np.max(evap_monthly))+'m, minimum evap is: '+ str(np.min(evap_monthly))+' m'


        lats, lons = grb2.latlons()  # (256, 512)
        im=ax2.contourf(lons,lats,rain_monthly)
        ax2.set_ylabel('latitude')
        ax2.set_xlabel('longitude')
        ax2.set_title('Precipitation (m) at UTC time: '
            +unicode(data_date_rain)+ ' or Beijing time:'
            +unicode(data_date_rain+datetime.timedelta(hours=+8) ))
        fig.colorbar(im,ax=ax2)
        print 'the max rain is: '+str(np.max(rain_monthly))+'m, minimum evap is: '+ str(np.min(rain_monthly))+' m'

        #print 'Processing time'+ unicode(data_date_rain)+ ', for precipitation finished'+str(lats.shape)

        im=ax3.contourf(lons,lats,evap_monthly-rain_monthly)
        ax3.set_ylabel('latitude')
        ax3.set_xlabel('longitude')
        ax3.set_title('Precipitation + evaporation (m) at UTC time: '
            +unicode(data_date)+ ' or Beijing time:'
            +unicode(data_date+datetime.timedelta(hours=+8) ))
        fig.colorbar(im,ax=ax3)

        evap_monthly=evap
        rain_monthly=rain
        date_previous=date_current
        month_previous=month_current



        fig_name='monthly_evp_rain_'+data_date_previous_step.strftime('%Y_%m')+'.png'
        fig.savefig(fig_name,format='png')
        plt.close(fig)



