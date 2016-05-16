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


    def find_lats_lons_idx_from_mtx(self,lats,lons):
        lats_ay=lats[:,1]
        lons_ay=lons[1,:]
        for n in np.arange(self.station_no):
            
        return a
        
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
