


for n in np.arange(len(day_count_yearly)):
    fig=plt.figure(figsize=(20,25))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    #v = np.linspace(-0.02,0.02, 21, endpoint=True)
    evap_annual_avg_mmday=-evap_yearly_raw[:,:,n]/day_count_yearly[n]*1000
    rain_annual_avg_mmday=rain_yearly_raw[:,:,n]/day_count_yearly[n]*1000

    
    im=ax1.contourf(lons,lats,evap_annual_avg_mmday) #,levels=v)
    ax1.set_ylabel('latitude')
    ax1.set_title('Average Evaporation (mm/day) in '+str(1979+n))
    fig.colorbar(im,ax=ax1) #,ticks=v)
    #print 'the max evap is: '+str(np.max(evap_total))+'m, minimum evap is: '+ str(np.min(evap_total))+' m'
    #
    #
    im=ax2.contourf(lons,lats,rain_annual_avg_mmday)
    ax2.set_ylabel('latitude')
    ax2.set_title('Average Precipitation (mm/day) in '+str(1979+n))
    fig.colorbar(im,ax=ax2)
    #print 'the max rain is: '+str(np.max(rain_total))+'m, minimum evap is: '+ str(np.min(rain_total))+' m'
    #
    ##print 'Processing time'+ unicode(data_date_rain)+ ', for precipitation finished'+str(lats.shape)
    #
    im=ax3.contourf(lons,lats,evap_annual_avg_mmday-rain_annual_avg_mmday)
    ax3.set_title('Average Evaporation-precipitation (mm/day) in ' +str(1979+n))
    ax3.set_ylabel('latitude')
    ax3.set_xlabel('longitude')
    #ax3.set_title('Precipitation + evaporation (m) at UTC time: '
    #    +unicode(data_date)+ ' or Beijing time:'
    #    +unicode(data_date+datetime.timedelta(hours=+8) ))
    fig.colorbar(im,ax=ax3)
    #fig.show()
    #
    print 'average_evaporatoin_rain_in_year_'+ str(1979+n)+'.png'
    fig_name='average_evaporatoin_rain_in_year_'+ str(1979+n)+'.png'
    csv_name_rain='annual_average_evaporation_mmday_in_year_'+str(1979+n)+'.csv'
    csv_name_evap='annual_average_rain_mmday_in_year_'+str(1979+n)+'.csv'
    csv_name_total='annual_average_net_evaporation_mmday_in_year_'+str(1979+n)+'.csv'
    
    np.savetxt(csv_name_rain, evap_annual_avg_mmday, delimiter=",")
    np.savetxt(csv_name_evap, rain_annual_avg_mmday, delimiter=",")
    np.savetxt(csv_name_total, evap_annual_avg_mmday-rain_annual_avg_mmday, delimiter=",")
    fig.savefig(fig_name,format='png')
    plt.close(fig)


np.savetxt('lats.csv', lats, delimiter=",")
np.savetxt('lons.csv', lons, delimiter=",")

