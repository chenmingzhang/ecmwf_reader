
import numpy as np
import matplotlib.pyplot as plt
import datetime
#for n in [0,1,2,3,4,5]:

grbs_evap.seek(0)
grbs_rain.seek(0)
n_evp=0
evp_max=0
evp_min=0
for n in grbs_evap:
    n_evp+=1
    grb_evap_current = grbs_evap.read(1)[0]
    evap= grb_evap_current.values
    evp_max=np.amin([np.amax(evap),evp_min])
    evp_min=np.amin([np.amin(evap),evp_min])

no_rain=0
for n in grbs_rain:
    no_rain+=1
    grb_evap_current = grbs_rain.read(1)[0]
    evap= grb_evap_current.values
    evp_max=np.amin([np.amax(evap),evp_min])
    evp_min=np.amin([np.amin(evap),evp_min])


grbs_evap.seek(0)
grbs_rain.seek(0)


#for n in grbs_evap:
for n in np.arange(i):
    print str(n)
    grb_evap_current = grbs_evap.read(1)[0]
    lats, lons = grb_evap_current.latlons()  # (256, 512)
    evap= grb_evap_current.values  # (256, 512)

    
    fig=plt.figure(figsize=(20,15))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    im=ax1.contourf(lons,lats,evap)
    ax1.set_ylabel('latitude')
    ax1.set_xlabel('longitude')
    data_date=grb_evap_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_evap_current.__getattribute__('validityTime')/100)
    ax1.set_title('Evaporation (m) at UTC time: '
        +unicode(data_date)+ ' or Beijing time:'
        +unicode(data_date+datetime.timedelta(hours=+8) ))
    fig.colorbar(im,ax=ax1)
    print 'Processing time'+ unicode(data_date)+ ', for evaporation finished, ' +str(lats.shape)


    grb_rain_current = grbs_rain.read(1)[0]
    lats, lons = grb_rain_current.latlons()  # (256, 512)
    rain= grb_rain_current.values  # (256, 512)


    im=ax2.contourf(lons,lats,rain)
    ax2.set_ylabel('latitude')
    ax2.set_xlabel('longitude')
    data_date=grb_rain_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_rain_current.__getattribute__('validityTime')/100)
    ax2.set_title('Precipitation (m) at UTC time: '
        +unicode(data_date)+ ' or Beijing time:'
        +unicode(data_date+datetime.timedelta(hours=+8) ))
    fig.colorbar(im,ax=ax2)

    print 'Processing time'+ unicode(data_date)+ ', for precipitation finished'+str(lats.shape)



    im=ax3.contourf(lons,lats,rain+evap)
    ax3.set_ylabel('latitude')
    ax3.set_xlabel('longitude')
    ax3.set_title('Precipitation + evaporation (m) at UTC time: '
        +unicode(data_date)+ ' or Beijing time:'
        +unicode(data_date+datetime.timedelta(hours=+8) ))
    fig.colorbar(im,ax=ax3)



    fig_name='all_hours_evp_rain_'+data_date.strftime('%Y_%m_%d__%H_%M')+'.png'
    fig.savefig(fig_name,format='png')
    plt.close(fig)



