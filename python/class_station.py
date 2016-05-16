#An example of a class
# http://sthurlow.com/python/lesson08/
class Station:
    def __init__(self,fname):
        import csv
        import numpy as np
        #with open('site_address.csv', 'rb') as csvfile:
        #with open('site_address.csv', 'rb') as csvfile:
        #    fn = csv.reader(csvfile, delimiter=',')
        #    # to save the file in to the class, one needs to define as self.row_count
        #    self.station_no = sum(1 for row in fn)
        #    self.station_name=[list() for _ in xrange(self.station_no)]
        #    n=0
        #    #for row in fn:
        #    for row in fn:
        #        self.content = list(row[i] for i in fn)
        #    #     self.station_name[n] = row
        #    #     n+=1
        #        print ', '.join(row)
        #    #self.n=n


        ## below part is working
        ## http://stackoverflow.com/questions/3925614/how-do-you-read-a-file-into-a-list-in-python
        #with open('site_address.csv') as f:
        #    self.lines = f.read().splitlines()

        #http://stackoverflow.com/questions/24662571/python-import-csv-to-list
    
        
        #self.lines = []
        #with open('site_address.csv', 'r') as f:
        #    for line in f.readlines():
        #        l,name = line.strip().split(',')
        #        self.lines.append((l,name))



        #http://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list-with-python
        # TO 20160516 it seems to me that it is better of to deal with csv completely and then do others based on the list created in this loop
        with open('site_address.csv', 'rb') as f:
            # this below doesn't work well with your_list
            #self.station_no = sum(1 for row in f)
            reader = csv.reader(f)
            your_list = list(reader)
            #self.x=reader.split(',')
            #[self.strip() for self in reader.split(',')]

        self.station_no=len(your_list)
        self.latitude=np.zeros(self.station_no,dtype=float)
        self.longitude=np.zeros(self.station_no,dtype=float)
        ## method 1, it ends up with list that each cell is a list
        ## http://stackoverflow.com/questions/3880037/how-to-create-a-list-or-tuple-of-empty-lists-in-python
        #self.station_name=[list(someListOfElements) for _ in xrange(self.station_no)]

        # method 2, it ends up with list that each cell is a string
        # http://stackoverflow.com/questions/6376886/what-is-the-best-way-to-create-a-string-array-in-python
        self.station_name = ["" for x in range(self.station_no)]        

        for n in np.arange(self.station_no):
            self.station_name[n]=your_list[n][0]
            self.latitude[n]=float(your_list[n][1])
            self.longitude[n]=float(your_list[n][2])

    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"

    def plot_stations(self):
        import matplotlib.pyplot as plt
        fig=plt.figure(figsize=(20,15))
        plt.plot(self.longitude,self.latitude,'r+')
        plt.ylabel('latitude')
        plt.xlabel('longitude')
        fig.savefig('station_location.png',format='png')
        #return fig.show()


    def find_lats_lons_idx_from_mtx(self,lats,lons):
        import operator
        lats_ay=lats[:,1]
        lons_ay=lons[1,:]
        self.lats_idx=np.zeros(self.station_no,dtype=int)
        self.lons_idx=np.zeros(self.station_no,dtype=int)
        for n in np.arange(self.station_no):
            #http://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
            self.lats_idx[n], min_value = min(enumerate(abs(a.latitude[n] -lats_ay)), key=operator.itemgetter(1))
            self.lons_idx[n], max_value = min(enumerate(abs(a.longitude[n]-lons_ay)), key=operator.itemgetter(1))

    def extract_value_at_stations(self,evap_yearly_raw,rain_yearly_raw,lats,lons,day_count_yearly):
        # define a list of empty np array:
        #result = [np.zeros(5) for _ in xrange(3)]
        # result = [np.random.rand(5) for _ in xrange(3)]
        # get the first column
        # b=[result[n][0] for n in xrange(2)]   # this ends up with a list
        # c=c=np.array([result[n][0] for n in xrange(2)])   # this ends up with a np array
        self.evap_annual_mmday    = [np.zeros(self.station_no,dtype=float) for _ in np.arange(day_count_yearly.size)]   
        self.rain_annual_mmday    = [np.zeros(self.station_no,dtype=float) for _ in np.arange(day_count_yearly.size)]   
        self.net_evap_annual_mmday= [np.zeros(self.station_no,dtype=float) for _ in np.arange(day_count_yearly.size)]   
        self.evap_avg_mmday       = np.zeros(self.station_no,dtype=float)
        self.rain_avg_mmday       = np.zeros(self.station_no,dtype=float)
        self.net_evap_avg_mmday   = np.zeros(self.station_no,dtype=float)
        self.days_annual=days_count_yearly

        for n in np.arange(day_count_yearly.size):
           # although we plot evap and rain by plot(lons,lats,evap), the evap and rain is stored by evap[lats, lons, steps]
           self.evap_annual_mmday[n]     = -evap_yearly_raw[self.lats_idx,self.lons_idx,n]*1000/day_count_yearly[n]
           self.rain_annual_mmday[n]     = rain_yearly_raw[self.lats_idx,self.lons_idx,n]*1000/day_count_yearly[n]
           self.net_evap_annual_mmday[n] = self.evap_annual_mmday[n]-self.rain_annual_mmday[n]
        

    def interpolate_values_as_mtx(self,lats,lons):
        from scipy.interpolate import griddata
        self.lats_mtx=lats
        self.lons_mtx=lons
        self.interp_evap_annual_mmday_mtx    = [np.zeros(lats.shape,dtype=float) for _ in np.arange(day_count_yearly.size)]
        self.interp_rain_annual_mmday_mtx    = [np.zeros(lats.shape,dtype=float) for _ in np.arange(day_count_yearly.size)]
        self.interp_net_evap_annual_mmday_mtx= [np.zeros(lats.shape,dtype=float) for _ in np.arange(day_count_yearly.size)]

        for n in np.arange(self.days_annual.size):
            self.interp_evap_annual_mmday_mtx[n] = griddata(np.vstack([self.latitude,self.longitude]), self.evap_annual_mmday[n], (self.lats_mtx, self.lons_mtx), method='cubic')
            self.interp_rain_annual_mmday_mtx[n] = griddata(np.vstack([self.latitude,self.longitude]), self.rain_annual_mmday[n], (self.lats_mtx, self.lons_mtx), method='cubic')
        

        
        
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale
    #  print a.fn_no_stations()
    def fn_no_stations(self):
        return self.row_count



#import csv
#with open('site_address.csv', 'rb') as f:
#    reader = csv.reader(f)
#    your_list = list(reader)
#
#print your_list
