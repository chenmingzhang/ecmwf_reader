fname='monthly_swing_isoGSM_atm_ann.nc';
%fname_2='monthly_swing_CAM_ann_1.nc'
%ndisp=ncdisp(fname);
%ndisp=ncdisp_2(fname);
font_size=25;
nc.time=ncread(fname,'time');
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

%nc.time_digi=double(datenum('01/01/1900 00:0:0.0')+nc.time/24);
%datestr(nc_time_normal,'dd/mmm/yyyy');

nc.longitude=ncread(fname,'lon');
nc.latitude=ncread(fname,'lat');
nc.lev=ncread(fname,'lev');
%nc.e=ncread(fname,'e');
%nc.e=permute(nc.e,[2,1,3]);
%nc.e_mean=-mean(nc.e,3);
nc.qhdo=ncread(fname,'QHDO');
nc.T=ncread(fname,'T');
nc.qh218o=ncread(fname,'QH218O');
nc.qh2o=ncread(fname,'QH2O');



nc.qhdo=permute(nc.qhdo,[2,1,3]);
nc.T=permute(nc.T,[2,1,3]);
nc.qh218o=permute(nc.qh218o,[2,1,3]);
nc.qh2o=permute(nc.qh2o,[2,1,3]);




nc.qhdo_mean=mean(nc.qhdo,3);
nc.qh218o_mean=mean(nc.qh218o,3);
nc.qh2o_mean=mean(nc.qh2o,3);
nc.T_mean=mean(nc.T,3);

[nc.lon_mtx,nc.la_mtx]=meshgrid(nc.longitude,nc.latitude);

h=figure;
contourf(nc.lon_mtx,nc.la_mtx,nc.qhdo_mean);
set(gca,'FontSize',20,'FontWeight','bold','linewidth',2)
title('average QHDO kg/kg/SMOW','fontweight','bold','fontsize',font_size);
xlabel('Longitude','fontweight','bold','fontsize',font_size);
ylabel('Latitude','fontweight','bold','fontsize',font_size);
colorbar
savefig(h,[fname,'_QHDO.fig']);
csvwrite([fname,'_longitude.csv'],nc.lon_mtx);
csvwrite([fname,'_latitude.csv'],nc.la_mtx)
csvwrite([fname,'qhdo_mean.csv'],nc.qhdo_mean)


h=figure;
contourf(nc.lon_mtx,nc.la_mtx,nc.qh218o_mean);
set(gca,'FontSize',20,'FontWeight','bold','linewidth',2)
title('average QH218O kg/kg/SMOW','fontweight','bold','fontsize',font_size);
xlabel('Longitude','fontweight','bold','fontsize',font_size);
ylabel('Latitude','fontweight','bold','fontsize',font_size);
colorbar
savefig(h,[fname,'_QH218O.fig']);
csvwrite([fname,'_longitude.csv'],nc.lon_mtx);
csvwrite([fname,'_latitude.csv'],nc.la_mtx)
csvwrite([fname,'qh218o_mean.csv'],nc.qh218o_mean)


h=figure;
contourf(nc.lon_mtx,nc.la_mtx,nc.qh2o_mean);
set(gca,'FontSize',20,'FontWeight','bold','linewidth',2)
title('average QH2O kg/kg/SMOW','fontweight','bold','fontsize',font_size);
xlabel('Longitude','fontweight','bold','fontsize',font_size);
ylabel('Latitude','fontweight','bold','fontsize',font_size);
colorbar
savefig(h,[fname,'_QH2O.fig']);
csvwrite([fname,'_longitude.csv'],nc.lon_mtx);
csvwrite([fname,'_latitude.csv'],nc.la_mtx);
csvwrite([fname,'qh2o_mean.csv'],nc.qh2o_mean);


h=figure;
contourf(nc.lon_mtx,nc.la_mtx,nc.T_mean-273.15);
set(gca,'FontSize',20,'FontWeight','bold','linewidth',2)
title('average T celsius','fontweight','bold','fontsize',font_size);
xlabel('Longitude','fontweight','bold','fontsize',font_size);
ylabel('Latitude','fontweight','bold','fontsize',font_size);
colorbar
savefig(h,[fname,'_T.fig']);
csvwrite([fname,'_longitude.csv'],nc.lon_mtx);
csvwrite([fname,'_latitude.csv'],nc.la_mtx)
csvwrite([fname,'T_mean.csv'],nc.T_mean)
