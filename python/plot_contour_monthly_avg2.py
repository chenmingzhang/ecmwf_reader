
import numpy as np
import matplotlib.pyplot as plt
import datetime
#for n in [0,1,2,3,4,5]:

f = open('myfile','w')

grbs_evap.seek(0)
grbs_rain.seek(0)
no_evap=0
evp_max=0
evp_min=0
for n in grbs_evap:
    no_evap+=1
    grb_evap_current = grbs_evap.read(1)[0]
    evap= grb_evap_current.values
    evp_max=np.amax([np.amax(evap),evp_max])
    evp_min=np.amin([np.amin(evap),evp_min])

no_rain=0
rain_max=0
rain_min=0
for n in grbs_rain:
    no_rain+=1
    grb_evap_current = grbs_rain.read(1)[0]
    rain= grb_evap_current.values
    rain_max=np.amax([np.amax(rain),rain_max])
    rain_min=np.amin([np.amin(rain),rain_min])


grbs_evap.seek(0)
grbs_rain.seek(0)


#for n in grbs_evap:
for n in np.arange(no_evap):
#for n in [0,1,2]: #,3,4,5,6,7,8,9,10,11]:
    print str(n)
    grb_evap_current = grbs_evap.read(1)[0]
    lats, lons = grb_evap_current.latlons()  # (256, 512)
    evap= grb_evap_current.values  # (256, 512)

    
    fig=plt.figure(figsize=(20,15))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    v = np.linspace(-0.01,0.01, 21, endpoint=True)
    im1=ax1.contourf(lons,lats,evap,levels=v)  # this turns out is the best way
       # to do the uniform contour, i spent 1.5 hours on this
    #im1=ax1.pcolor(lons,lats,evap)
    ax1.set_ylabel('latitude')
    ax1.set_xlabel('longitude')
    data_date=grb_evap_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_evap_current.__getattribute__('validityTime')/100)
    ax1.set_title('Evaporation (m) at UTC time: '
        +unicode(data_date)+ ' or Beijing time:'
        +unicode(data_date+datetime.timedelta(hours=+8) ))
    cb=plt.colorbar(im1,ax=ax1,ticks=v)
    
    #cb.set_clim(vim=evp_min,vmax=evp_max)
    im1.colorbar.set_clim(-0.01,0.01)
    print 'Processing time'+ unicode(data_date)+ ', for evaporation finished, ' +str(lats.shape)+ str(evp_max)
    f.write('Processing time'+ unicode(data_date)+ ', for evaporation finished,' +str(lats.shape)+ str(evp_max))


    grb_rain_current = grbs_rain.read(1)[0]
    lats, lons = grb_rain_current.latlons()  # (256, 512)
    rain= grb_rain_current.values  # (256, 512)


    v = np.linspace(-0.05,0.5, 13, endpoint=True)
    #im2=ax2.contourf(lons,lats,rain,levels=v)
    im2=ax2.contourf(lons,lats,rain)
    ax2.set_ylabel('latitude')
    ax2.set_xlabel('longitude')
    data_date=grb_rain_current.__getattribute__('analDate')+datetime.timedelta(hours=grb_rain_current.__getattribute__('validityTime')/100)
    ax2.set_title('Precipitation (m) at UTC time: '
        +unicode(data_date)+ ' or Beijing time:'
        +unicode(data_date+datetime.timedelta(hours=+8) ))
    cb2=fig.colorbar(im2,ax=ax2,ticks=v)

    print 'Processing time'+ unicode(data_date)+ ', for precipitation finished'+str(lats.shape)+str(rain_max)
    f.write( 'Processing time'+ unicode(data_uate)+ ', for precipitation finished'+str(lats.shape)+str(rain_max) )



    im3=ax3.contourf(lons,lats,evap-rain)
    ax3.set_ylabel('latitude')
    ax3.set_xlabel('longitude')
    ax3.set_title('Precipitation + evaporation (m) at UTC time: '
        +unicode(data_date)+ ' or Beijing time:'
        +unicode(data_date+datetime.timedelta(hours=+8) ))
    cb3=fig.colorbar(im3,ax=ax3)
    #cb3.set_clim([rain_min,rain_max])

    fig_name='daily_evp_rain_'+data_date.strftime('%Y_%m_%d__%H_%M')+'.png'
    fig.savefig(fig_name,format='png')
    plt.close(fig)



