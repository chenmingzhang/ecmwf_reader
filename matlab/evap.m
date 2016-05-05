ndisp=ncdisp('evp_2010.nc');
nc.time=ncread('evp_2010.nc','time');
%>> ncdisp('_grib2netcdf-atls18-95e2cf679cd58ee9b4db4dd119a05a8d-fnTRg_.nc','time')         
%Source:
%           /home/gchenming/Dropbox/_grib2netcdf-atls18-95e2cf679cd58ee9b4db4dd119a05a8d-fnTRg_.nc
%Format:
%           64bit
%Dimensions:
%           time = 365   (UNLIMITED)
%Variables:
%    time
%           Size:       365x1
%           Dimensions: time
%           Datatype:   int32
%           Attributes:
%                       units     = 'hours since 1900-01-01 00:00:0.0'
%                       long_name = 'time'
%                       calendar  = 'gregorian'

nc.time_digi=double(datenum('01/01/1900 00:0:0.0')+nc.time/24);
%datestr(nc_time_normal,'dd/mmm/yyyy');

nc.longitude=ncread('evp_2010.nc','longitude');


nc.latitude=ncread('evp_2010.nc','latitude');
nc.e=ncread('evp_2010.nc','e');
nc.e=permute(nc.e,[2,1,3]);
nc.e_mean=-mean(nc.e,3);


[nc.long_mtx,nc.la_mtx]=meshgrid(nc.longitude,nc.latitude);

%figure;contour(nc.mesh_long,nc.mesh_la,nc.e_mean)
figure;contour(nc.long_mtx,nc.la_mtx,nc.e_mean*1000);
title('mm of water vaporized in 2010');
xlabel('longitude');
ylabel('latitude');
csvwrite('longitude.csv',nc.long_mtx)
csvwrite('latitude.csv',nc.la_mtx)
csvwrite('evap_2010.csv',nc.la_mtx)

figure;plot(nc.time_digi,,squeeze(nc.e(120,150,:)));





