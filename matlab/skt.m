fn='2009_jan_skin_temp_00_06_12_18_skin_temp.nc';
ncdisp(fn);
nc.time=double(ncread(fn,'time'));
abs0=-273.15;
%Source:
%           /home/chenming/Projects/Tao_grib/Skin_temp/2009_jan_skin_temp_00_06_12_18_skin_temp.nc
%Format:
%           64bit
%Global Attributes:
%           Conventions = 'CF-1.6'
%           history     = '2016-04-19 06:19:19 GMT by grib_to_netcdf-1.14.5: grib_to_netcdf /data/data01/scratch/_mars-atls02-95e2cf679cd58ee9b4db4dd119a05a8d-ayuyUZ.grib -o /data/data01/scratch/_grib2netcdf-atls17-95e2cf679cd58ee9b4db4dd119a05a8d-7dFHMG.nc -utime'
%Dimensions:
%           longitude = 480
%           latitude  = 241
%           time      = 124   (UNLIMITED)
%Variables:
%    longitude
%           Size:       480x1
%           Dimensions: longitude
%           Datatype:   single
%           Attributes:
%                       units     = 'degrees_east'
%                       long_name = 'longitude'
%    latitude 
%           Size:       241x1
%           Dimensions: latitude
%           Datatype:   single
%           Attributes:
%                       units     = 'degrees_north'
%                       long_name = 'latitude'
%    time     
%           Size:       124x1
%           Dimensions: time
%           Datatype:   int32
%           Attributes:
%                       units     = 'hours since 1900-01-01 00:00:0.0'
%                       long_name = 'time'
%                       calendar  = 'gregorian'
%    skt      
%           Size:       480x241x124
%           Dimensions: longitude,latitude,time
%           Datatype:   int16
%           Attributes:
%                       scale_factor  = 0.0020629
%                       add_offset    = 271.4162
%                       _FillValue    = -32767
%                       missing_value = -32767
%                       units         = 'K'
%                       long_name     = 'Skin temperature'







nc.time_digi=double(datenum('01/01/1900 00:0:0.0')+nc.time/24);
%datestr(nc_time_normal,'dd/mmm/yyyy');
nc.time_str=datestr(nc.time_digi,'dd/mmm/yyyy HH:MM:SS');

nc.longitude=ncread(fn,'longitude');
nc.latitude=ncread(fn,'latitude');
nc.skt=ncread(fn,'skt');
nc.skt=permute(nc.skt,[2,1,3]);
nc.skt_mean=mean(nc.skt,3);


%nc.e_mean=-mean(nc.e,3);


[nc.long_mtx,nc.la_mtx]=meshgrid(nc.longitude,nc.latitude);
%[nc.long_mtx,nc.la_mtx]=meshgrid(nc.latitude,nc.longitude);
% >> a=[1,3,5];
% >> b=[2,4];
%>> [aa,bb]=meshgrid(a,b)
%
%aa =
%
%     1     3     5
%     1     3     5
%
%
%bb =
%
%     2     2     2
%     4     4     4






% ----------------------------  plot figure --------------------  
a.fig=figure;
set(a.fig,'name',[get_current_folder_name,'__session1'],'NumberTitle','off')


fs = 3; % sampling frequency
% Creating the movie : quality = 100%, no compression is used and the
% timing is adjusted to the sampling frequency of the time interval
qt=100;
set(gcf,'Units','normalized', 'WindowStyle','docked','OuterPosition',[0 0 1 1]);  % maximize the plotting figure
mov =  VideoWriter('evt.avi');% avifile('pvc1.avi','quality',qt,'compression','indeo5','fps',fs);
% mov.FrameRate records the number of images per second, the large the values, the faster the play goes.
%  note this does not change the size of the figure;
% also in matlab 2015, it seems one does not need to keep on watching the video while it is recording. 
mov.FrameRate = 10;mov.Quality=qt;
open(mov);

for n=1:length(nc.time)
  contourf(nc.long_mtx,nc.la_mtx,nc.skt(:,:,n)+abs0);
  title(['Temperature (celsius) at: ',nc.time_str(n,:),' UTC', ', or ',datestr(nc.time_digi(n)+8/24,'dd/mmm/yyyy, HH:MM'),' Beijing Time']);
  colorbar;
  caxis([-40 50])
  xlabel('Longitude');
  ylabel('Latitude');
  F = getframe(gcf); % save the current figure
  writeVideo(mov,F);% add it as the next frame of the movie
end
close(mov)

%-------------------- end plot figure --------------------   


%%% from the excise below, it is found that one does not need to use the linear way to get the real data
%% ncread has already done that
%%        1. Values in VARDATA equal to the '_FillValue' attribute value are
%%           replaced with NaNs. If '_FillValue' attribute does not exist,
%%           NCREAD will query the library for the variable's fill value.
%%        2. VARDATA is multiplied by the value of 'scale_factor' attribute.
%%        3. The value of the 'add_offset' attribute is added to VARDATA.
%
%nc.scale_factor=ncreadatt(fn,'skt','scale_factor');
%nc.add_offset=ncreadatt(fn,'skt','add_offset');
%figure;
%plot(nc.time_digi,squeeze(nc.skt(180,120,:))-273.15,'ro');hold on
%plot(nc.time_digi,nc.scale_factor*squeeze(nc.skt(180,120,:))+nc.add_offset-273.15,'go');hold on
%datetick('x','dd/mm MM:HH')

% ---------------------------------------------------------


%%figure;contour(nc.mesh_long,nc.mesh_la,nc.e_mean)
%figure;contour(nc.long_mtx,nc.la_mtx,nc.e_mean*1000);
%title('mm of water vaporized in 2010');
%xlabel('longitude');
%ylabel('latitude');
%csvwrite('longitude.csv',nc.long_mtx)
%csvwrite('latitude.csv',nc.la_mtx)
%csvwrite('evap_2010.csv',nc.la_mtx)
%
%%figure;plot(nc.time_digi,,squeeze(nc.e(120,150,:)));





