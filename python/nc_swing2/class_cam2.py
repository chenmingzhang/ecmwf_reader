import numpy as np
from netCDF4 import Dataset
from mpl_toolkits import basemap
import matplotlib.pyplot as plt
import os
class cam2:
    def __init__(self,fn):
        #import constants as const
        #from scipy.interpolate import griddata
        print 'Initializing class scale  ...'
        
        self.fh = Dataset(fn, mode='r')
        self.lons = self.fh.variables['lon'][:]
        self.lats = self.fh.variables['lat'][:]
        self.lons_unit= self.fh.variables['lon'].units
        self.lats_unit= self.fh.variables['lat'].units
        self.lons_mtx,self.lats_mtx=np.meshgrid(self.lons,self.lats)
	var_name_unicode=self.fh.variables.keys()
        self.var_no=len(var_name_unicode)
	self.var_name=[var_name_unicode[i].encode('utf8') for i in xrange(len(var_name_unicode))]
       # self.long_name=[self.fh.variables[i].long_name.encode('utf8') for i in self.var_name]
       #for i in self.var_name:
       #    print i
       #    b=self.fh.variables[i].long_name
        self.long_name=["" for x in xrange(len(self.var_name))] 
        self.units=["" for x in xrange(len(self.var_name))] 
        self.shape=["" for x in xrange(len(self.var_name))] 
        self.dim=["" for x in xrange(len(self.var_name))] 
        i=-1
        

        # infact i think this is not really useful as we can call from it anyway if we know the 
        # locations.
        for n in self.var_name:
            # the reason try except is needed here is because some of the variable does not
            # have long name and units
            try:
                i+=1
                self.dim[i]=self.fh.variables[n].dimensions
                self.shape[i]=self.fh.variables[n].shape
                self.long_name[i]=self.fh.variables[n].long_name.encode('utf-8')
                self.units[i]=self.fh.variables[n].units.encode('utf-8')
            except:
                self.long_name[i]=''
                self.units[i]=''

    def plot_vapor_contour(self):
        from mpl_toolkits.basemap import Basemap
        qh2o_2d=np.mean(self.fh.variables['QH2O'][:],0)
        qh2o_2d=np.mean(qh2o_2d,0)
        fig, ax = plt.subplots(2,figsize=(20,25)) #,sharex=True)
        self.my_map=Basemap(llcrnrlon=0,llcrnrlat=-80,urcrnrlon=350,urcrnrlat=80,projection='mill')
        #my_map=Basemap(llcrnrlon=-10,llcrnrlat=-80,urcrnrlon=340,urcrnrlat=80,projection='mill')
        #my_map=Basemap(llcrnrlon=0,llcrnrlat=-80,urcrnrlon=350,urcrnrlat=80,projection='merc')
        # it is funny that llcrnrlon=0,llcrnrlat=-90,urcrnrlon=360,urcrnrlat=90
        ## provides a white margin to the system
        meridians = np.arange(0.,360.,30.)

        #my_map=Basemap(llcrnrlon=0,llcrnrlat=-80,urcrnrlon=350,urcrnrlat=80,projection='mill')
        #my_map=Basemap(llcrnrlon=0,llcrnrlat=-80,urcrnrlon=360,urcrnrlat=80,projection='ortho')
        #my_map=Basemap(lat_0=0,lon_0=0,projection='ortho')
        self.my_map.drawcoastlines(ax=ax[0])#,alpha=0.5)
        #ax[0].plot_date(self.time_dt,self.scale1,'r+')
        #ax[0].plot_date(self.time_dt_sp,self.scale1_sp,'go')
        #ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%d/%b')) 
        #ax[0].grid(True)
        self.my_map.drawmeridians(meridians,labels=[1,1,1,1],fontsize=10,ax=ax[0])
        # this is the most important line for overlapping the plots
        self.lons_mtx_proj,self.lats_mtx_proj=self.my_map(self.lons_mtx,self.lats_mtx)
        #h_contour=ax[0].contourf(self.lons_mtx,self.lats_mtx,qh2o_2d)
        h_contour=ax[0].contourf(self.lons_mtx_proj,self.lats_mtx_proj,qh2o_2d)
        fig.colorbar(h_contour,ax=ax[0])

        ax[0].set_ylabel('Latitude')
        ax[0].set_xlabel('Longitude', labelpad=20)
        ax[0].set_title(self.fh.variables['QH2O'].long_name+''+self.fh.variables['QH2O'].units,y=1.08)

        #plt.xlabel('TIME')
        #fig.suptitle(['coef= ' + str(arg['coef'])+' time_interval_sec_sp= '+ str(arg['time_interval_sec_sp'])], fontsize=20)

        meridians = np.arange(0.,360.,30.)
        self.my_map.drawcoastlines(ax=ax[1])
        self.my_map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10,ax=ax[1])
        t_2d=np.mean(self.fh.variables['T'][:],0)
        t_2d=np.mean(t_2d,0)
        t_contour=ax[1].contourf(self.lons_mtx_proj,self.lats_mtx_proj,t_2d)
        fig.colorbar(t_contour,ax=ax[1])
        ax[1].set_ylabel('Latitude')
        ax[1].set_xlabel('Longitude', labelpad=20)
        ax[1].set_title(self.fh.variables['T'].long_name+''+self.fh.variables['T'].units)

        #ax[1].plot_date(self.time_dt,self.scale1,'r+')
        #ax[1].plot_date(self.time_dt_sp,self.evap_rate*const.ms2mmday,'go')
        #ax[1].grid(True)
        #ax[1].set_ylabel('EVAP. (mm/day)')

        fname='spline_coef'+'.png'
        fig.savefig(fname,format='png',dpi=300)
        #return fig.show()

    def show_variable_list(self):
        for i in xrange(self.var_no):
#           print "%s10 ," self.fh.variables.keys()[i]
            # negative means left alignment
            print "%-10s, %-18s, %-30s, %-10s, %-50s" %(self.fh.variables.keys()[i], self.shape[i], [self.dim[i][j].encode('utf8') for j in xrange(len(self.dim[i]))], self.units[i], self.long_name[i])

    def get_coastlines(self,npts_min=0):
        # open data and meta data files 
        # this script is obtained from websites
        dirname_basemap = os.path.dirname(basemap.__file__)
        path_points = os.path.join(dirname_basemap, 'data', 'gshhs_c.dat')
        path_meta = os.path.join(dirname_basemap, 'data', 'gshhsmeta_c.dat')

        # read points for each segment that is specified in meta_file
        points_file = open(path_points, 'rb')
        meta_file = open(path_meta,'r')
        segments = []
        for line in meta_file:
            # kind=1 are continents, kind=2 are lakes
            kind, area, npts, lim_south, lim_north, startbyte, numbytes,\
            date_line_crossing = line.split()
            points_file.seek(int(startbyte))
            data = np.fromfile(points_file, '<f4', count = int(numbytes)/4)
            data = data.reshape(int(npts), 2)
            if npts_min < int(npts):
                segments.append(data)
        return segments

    def plot_continent(self,continent_id=0,plot=False):
        self.coastal_segments = self.get_coastlines(npts_min=100)
        #segments2=[segments[i][:,0]+180  for i in xrange(len(segments))]
        #[segments[i][:,0]+=180  for i in xrange(len(segments))]   # fail
        # http://stackoverflow.com/questions/38493469/python-one-liner-to-do-arithmetic-operation-on-one-element-with-same-index-for-a?noredirect=1#comment64388031_38493469
        #segments=map(lambda x: [x[0] + 1, x[1]],segments)
        # make it consistent with other coordinates
        for i in xrange(len(self.coastal_segments)):
            if self.coastal_segments[i][0,0]<0:
                self.coastal_segments[i][:,0]= self.coastal_segments[i][:,0]+360 #-180  # plus 180 is to make sure the lats and lons are the same as cam2

        # move back to ziped profiles
        segments2=zip(*self.coastal_segments[continent_id])

        self.seg_lons_proj,self.seg_lats_proj=self.my_map(segments2[0],segments2[1])
        fig, ax = plt.subplots(2,figsize=(20,25))
        self.my_map.drawcoastlines(ax=ax[0])
        ax[0].plot(self.seg_lons_proj,self.seg_lats_proj)

        from matplotlib import path
        #p = path.Path(self.coastal_segments[0])  # 0 selects the circle that system chooses.
        p = path.Path(zip(*[self.seg_lons_proj,self.seg_lats_proj])) 
        ##hatch=p.contains_points([[self.lons_mtx.flat[i],self.lats_mtx.flat[i]] for i in xrange(self.lons_mtx.size)])
        self.hatch=p.contains_points([[self.lons_mtx_proj.flat[i],self.lats_mtx_proj.flat[i]] for i in xrange(self.lons_mtx.size)])
        ##hatch2=p.points_in_path([[self.lons_mtx.flat[i],self.lats_mtx.flat[i]] for i in xrange(self.lons_mtx.size)])
        ##plt.plot(self.lons_mtx.flat[hatch],self.lats_mtx.flat[hatch],'k.')
        ax[0].plot(self.lons_mtx_proj.flat[self.hatch],self.lats_mtx_proj.flat[self.hatch],'k.')
        ax[0].set_ylabel('Latitude')
        ax[0].set_xlabel('Longitude', labelpad=20)
        ax[1].set_title(self.fh.variables['T'].long_name+''+self.fh.variables['T'].units)


        meridians = np.arange(0.,360.,30.)
        self.my_map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10,ax=ax[0])

        fname='plot_continent.png'
        plt.savefig(fname,format='png',dpi=300)

        if plot==True: plt.show(block=False) 

    #def find_city_locations(self,locations=['sydney','perth']):    
    def find_city_locations(self,plot=False,locations=['sydney','perth','adelaide','brisbane','shanghai','los angeles','cape town','New York','Luanda','Lisbon']):
        # https://pypi.python.org/pypi/geopy
        from geopy.geocoders import Nominatim
        from scipy import spatial
        from time import sleep
        geolocator = Nominatim()
        #cities={}
        self.cities={k:{} for k in locations}
        #cities['location_name']=['sydney','darwin','perth','adelaide','brisbane','shanghai','los angeles']
        #cities['location_name']=['sydney']
        #location=[None]*len(cities['location_name'])
        #location={}
        #for i in cities['location_name']:
        #    location[str(i)] = geolocator.geocode(cities[ame'])
        
        #for i in cities['location_name'][i]:
        #    location[str(i)] = geolocator.geocode(cities[ame'])
        no_cities=len(self.cities)
        ##location=[[] for _ in xrange(no_cities)]
        ### get the address
        ##for i in xrange(len(cities['location_name'])):
        ##   #http://stackoverflow.com/questions/27914648/geopy-catch-timeout-error
        ##   location[i]=geolocator.geocode(cities['location_name'][i],timeout=None)
        ##   #if location[i].longitude<0:
        ##   #     location[i].longitude=location[i].longitude+360
        ##   sleep(1)
        ##
        ###http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.query.html 
        ##tree = spatial.KDTree(zip(self.lons_mtx.ravel(),self.lats_mtx.ravel()))
        ##pts  = np.array(  [[location[i].longitude,location[i].latitude] for i in xrange(no_cities)]   )
	### correct negative longitude
	##for i in xrange(len(pts)):
        ##    if pts[i][0]<0:
	##	pts[i][0]+=360
        ##dist,self.city_latlon_idx=tree.query(pts)
        



        #http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.query.html 
        tree = spatial.KDTree(zip(self.lons_mtx.ravel(),self.lats_mtx.ravel()))

        for i in self.cities:
           print i
           #http://stackoverflow.com/questions/27914648/geopy-catch-timeout-error
           self.cities[i]['location_geo']=geolocator.geocode(i,timeout=None)
           self.cities[i]['latitude']=self.cities[i]['location_geo'].latitude
           self.cities[i]['longitude']=self.cities[i]['location_geo'].longitude
	   # correct negative longitude
           if self.cities[i]['longitude']<0:
               self.cities[i]['longitude']+=360
           #if location[i].longitude<0:
           #     location[i].longitude=location[i].longitude+360
           dist,self.cities[i]['latlon_idx']=tree.query( [self.cities[i]['longitude'],self.cities[i]['latitude']])
           sleep(0.8)
        


        fig, ax = plt.subplots(1,figsize=(20,25))
        self.my_map.drawcoastlines(ax=ax)
        for i in self.cities:
            ax.plot(self.lons_mtx_proj.flat[self.cities[i]['latlon_idx']],self.lats_mtx_proj.flat[self.cities[i]['latlon_idx']],'go')
        
        
        fname='plot_cities.png'
        plt.savefig(fname,format='png',dpi=300)

       # plt.show(block=False) if plot==True
        if plot==True: plt.show(block=False) 

    def append_nc_files(self,file_path):
        #import os
        import glob
        import re
	fn=glob.glob("/home/chenming/gis_swing_nasa/*.nc")
        # after search it is found that only the file name shows the years for the cam2 model.
        self.no_append_files=len(fn)
        self.file_year=[[] for i in xrange(self.no_append_files)]
        self.file_lists={}
        for i in xrange(self.no_append_files):
            #http://stackoverflow.com/questions/15478127/remove-final-character-from-string-python
            self.file_year[i]=next(re.finditer(r'\d+$', fn[i][:-3])).group(0)
            #the advantage of using dictionary is that it is able to avoid repeat defining same thing
            self.file_lists[ self.file_year[i]]= {'fn'  :Dataset(fn[i], mode='r')}

        
        

    def averaging_results(self):
        pass
    

    def extracting_variable_over_time(self,variable=['UINT','VINT']):
        self.var_avg={}
        for i in variable:
            print i
            b=np.zeros(self.lats_mtx.shape,dtype=float   )
	    for n in self.file_lists:
                b+=self.file_lists[n]['fn'].variables[i][:].mean(0)
            self.var_avg[i]=b/float(self.no_append_files)
        fig, ax = plt.subplots(2,figsize=(20,25)) #,sharex=True)
        self.my_map.drawcoastlines(ax=ax[0])
        u_contour=ax[0].contourf(self.lons_mtx_proj,self.lats_mtx_proj,self.var_avg['UINT'])
        ax[0].set_ylabel('Latitude')
        ax[0].set_xlabel('Longitude', labelpad=20)
        ax[0].set_title(self.fh.variables['UINT'].long_name+''+self.fh.variables['UINT'].units,y=1.08)
        fig.colorbar(u_contour,ax=ax[0])
        self.my_map.drawcoastlines(ax=ax[1])
        v_contour=ax[1].contourf(self.lons_mtx_proj,self.lats_mtx_proj,self.var_avg['VINT'])
        ax[1].set_ylabel('Latitude')
        ax[1].set_xlabel('Longitude', labelpad=20)
        ax[1].set_title(self.fh.variables['VINT'].long_name+''+self.fh.variables['VINT'].units,y=1.08)
        fig.colorbar(v_contour,ax=ax[1])
        fname='U_V_average_over_time'+'.png'
        fig.savefig(fname,format='png',dpi=300)

    def extracting_city_variable_over_time(self,variable=['UINT','VINT','U','V'],layer=0):
        for k in self.cities:
            #self.cities[k]={'variables']
            print k
            #self.cities[k]={}
            for i in variable:
                self.cities[k][i]={}
                for j in self.file_year:
                    #print j
                    self.cities[k][i][j]=np.zeros(12,dtype=float)
                    for n in xrange(12):
                        #print n
                        if self.file_lists[j]['fn'].variables[i].ndim==3:
                            temp=self.file_lists[j]['fn'].variables[i][n,:,:]
			elif self.file_lists[j]['fn'].variables[i].ndim==4:
                            temp=self.file_lists[j]['fn'].variables[i][n,layer,:,:]  #bottom layer
                        self.cities[k][i][j][n]=temp.flat[self.cities[k]['latlon_idx']]

    def plot_wind_rose_at_cities(self,datatype=['UINT','VINT']):
        """ plot wind rose at each city based on cities['city']['UINT'] and ['VINT']"""
        from windrose import WindroseAxes
        from matplotlib import pyplot as plt
        import matplotlib.cm as cm
        import numpy as np

        #fig, ax = plt.subplots(5,2,sharex=True)
        #plt_idx=0
        for city,var in self.cities.iteritems():
            # convert all the u and v into one array
            u_int=np.concatenate([ var[datatype[0]][i] for i,b in var[datatype[0]].iteritems()])
            v_int=np.concatenate([ var[datatype[1]][i] for i,b in var[datatype[1]].iteritems()])
            # http://stackoverflow.com/questions/21484558/how-to-calculate-wind-direction-from-u-and-v-wind-components-in-r
            # get from u v to windrose
            wind_abs=np.sqrt(np.power(u_int,2.0)+np.power(v_int,2.0))
            wind_dir_trig_to = np.arctan2(u_int/wind_abs,v_int/wind_abs)
            wind_dir_trig_to_degrees = wind_dir_trig_to * 180.0/np.pi  
            wind_dir_trig_from_degrees = wind_dir_trig_to_degrees + 180.0
            wind_dir_cardinal = 90 - wind_dir_trig_from_degrees

            # draw wind rose

            ax = WindroseAxes.from_ax()
            ax.bar(wind_dir_trig_from_degrees, wind_abs, normed=True, opening=0.8, edgecolor='white')
            #ax.bar(wind_dir_cardinal, wind_abs, normed=True, opening=0.8, edgecolor='white')
            ax.set_legend()
            ax.set_title(city)
            #plt_idx+=1

            #plt.show(block=False)
            #savefig('foo.png')
            fname='windrose_'+datatype[0]+datatype[1]+'_'+city+'.png'
            plt.savefig(fname,format='png',dpi=300)



#    def plot_wind_rose_at_cities22(self,datatype=['UINT','VINT']):
#        """ plot wind rose at each city based on cities['city']['UINT'] and ['VINT']"""
#        from windrose import WindroseAxes
#        from matplotlib import pyplot as plt
#        import matplotlib.cm as cm
#        import numpy as np
#
#        fig, ax = plt.subplots(5,2)
#        plt_idx=0
#        for city,var in self.cities.iteritems():
#            # convert all the u and v into one array
#            u_int=np.concatenate([ var[datatype[0]][i] for i,b in var[datatype[0]].iteritems()])
#            v_int=np.concatenate([ var[datatype[1]][i] for i,b in var[datatype[1]].iteritems()])
#            # http://stackoverflow.com/questions/21484558/how-to-calculate-wind-direction-from-u-and-v-wind-components-in-r
#            # get from u v to windrose
#            wind_abs=np.sqrt(np.power(u_int,2.0)+np.power(v_int,2.0))
#            wind_dir_trig_to = np.arctan2(u_int/wind_abs,v_int/wind_abs)
#            wind_dir_trig_to_degrees = wind_dir_trig_to * 180.0/np.pi  
#            wind_dir_trig_from_degrees = wind_dir_trig_to_degrees + 180.0
#            wind_dir_cardinal = 90 - wind_dir_trig_from_degrees
#
#            # draw wind rose
#
#            ax.flat[plt_idx] = WindroseAxes.from_ax()
#            ax.flat[plt_idx].bar(wind_dir_trig_from_degrees, wind_abs, normed=True, opening=0.8, edgecolor='white')
#            #ax.bar(wind_dir_cardinal, wind_abs, normed=True, opening=0.8, edgecolor='white')
#            ax.flat[plt_idx].set_legend()
#            ax.flat[plt_idx].set_title(city)
#            plt_idx+=1
#
#        plt.show(block=False)

        #self.cities[k].variable[i][j]=self.file_lists[j]['fn'].variables[i][
        # http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python?rq=1
        #d = {'x': 1, 'y': 2, 'z': 3} 
        #for key, value in d.iteritems():
        #    print key value
            
        #for i,b in self.cities['perth']['UINT'].iteritems():
        #    print i,b
 
        #    self.var_avg[variable] =  

