# this script reads the station location

import csv
with open('site_address.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
         print ', '.join(row)
