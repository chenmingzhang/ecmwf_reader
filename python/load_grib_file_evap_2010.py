# this script loads the grib file on the system 
import sys
import os
import pygrib
import time
#sys.modules[__name__].__dict__.clear()


start_time=time.time()
print("now_reading evaporation data" )
# how to find home folder for python
#http://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python
grbs_evap=pygrib.open(os.path.expanduser('~')+"/Dropbox/evap_total_2010.grib")
elapsed_time_min=(time.time()-start_time)/60
print("it takes %8.3e minutes for loading evaporation"  % (elapsed_time_min))
start_time=time.time()
print("now_reading precipitation data" )
grbs_rain=pygrib.open(os.path.expanduser('~')+"/Dropbox/precipitation_total_2010.grib")
elapsed_time_min=(time.time()-start_time)/60
print("it takes %8.3e minutes for loading evaporation"  % (elapsed_time_min))




print("Reading finished!" )


#start_time=time.time()
#grbs_rain=pygrib.open("/home/chenming/Downloads/_mars-atls18-95e2cf679cd58ee9b4db4dd119a05a8d-it73Gf.grib")
#elapsed_time_min=(time.time()-start_time)/60
#
#print("it takes %8.3e minutes for loading rain"  % (elapsed_time_min))
#print("reading finished")


#grbs.seek(2)
#grbs.tell()  # show the current location
#
#grb = grbs.read(1)[0] #read the next line then you can use grbs.seek to go to the lines that you are interested.
##7:Evaporation:m of water equivalent (instant):reduced_gg:surface:level 0:fcst time 12 hrs:from 197901010000
#
## the script here find the file called 'evaporation', and it going to be the very first one to show up as discripbed by 0
## if 0 is changed to 10, then it is going to be the 11th instance that comes with 'Evaporation'
## this approach is not very efficient as it searches all the way through the system
#grb = grbs.select(name='Evaporation')[0]
#
##maxt= grb.values  # get the grb values.
##  maxt.shape, maxt.min(), maxt.max()
#evap= grb.values  # get the grb values.
##  evap.shape, evap.min(), evap.max()
#grb['values']
#
#grb = grbs.select(name='Evaporation')[0]
#
#grb.__getattribute__('date')
#grb.__getattribute__('time')
#
#grb.keys()  # this gets a list of the attributes for analysis
#
#lats, lons = grb.latlons()
#
##[u'parametersVersion', u'hundred', u'globalDomain', u'GRIBEditionNumber', u'eps', u'offsetSection0', u'section0Length', u'totalLength', u'editionNumber', u'WMO', u'productionStatusOfProcessedData', u'section1Length', u'wrongPadding', u'table2Version', u'centre', u'centreDescription', u'generatingProcessIdentifier', u'gridDefinition', u'indicatorOfParameter', u'parameterName', u'parameterUnits', u'indicatorOfTypeOfLevel', u'pressureUnits', u'typeOfLevel', u'level', u'yearOfCentury', u'month', u'day', u'hour', u'minute', u'second', u'unitOfTimeRange', u'P1', u'P2', u'timeRangeIndicator', u'numberIncludedInAverage', u'numberMissingFromAveragesOrAccumulations', u'centuryOfReferenceTimeOfData', u'subCentre', u'paramIdECMF', u'paramId', u'cfNameECMF', u'cfName', u'cfVarNameECMF', u'cfVarName', u'unitsECMF', u'units', u'nameECMF', u'name', u'decimalScaleFactor', u'setLocalDefinition', u'dataDate', u'year', u'dataTime', u'julianDay', u'stepUnits', u'stepType', u'stepRange', u'startStep', u'endStep', u'marsParam', u'validityDate', u'validityTime', u'deleteLocalDefinition', u'localUsePresent', u'localDefinitionNumber', u'GRIBEXSection1Problem', u'marsClass', u'marsType', u'marsStream', u'experimentVersionNumber', u'perturbationNumber', u'numberOfForecastsInEnsemble', u'grib2LocalSectionNumber', u'shortNameECMF', u'shortName', u'ifsParam', u'gridDescriptionSectionPresent', u'bitmapPresent', u'section2Length', u'radius', u'numberOfVerticalCoordinateValues', u'neitherPresent', u'pvlLocation', u'dataRepresentationType', u'gridDefinitionTemplateNumber', u'Ni', u'Nj', u'latitudeOfFirstGridPoint', u'latitudeOfFirstGridPointInDegrees', u'longitudeOfFirstGridPoint', u'longitudeOfFirstGridPointInDegrees', u'resolutionAndComponentFlags', u'ijDirectionIncrementGiven', u'earthIsOblate', u'resolutionAndComponentFlags3', u'resolutionAndComponentFlags4', u'uvRelativeToGrid', u'resolutionAndComponentFlags6', u'resolutionAndComponentFlags7', u'resolutionAndComponentFlags8', u'latitudeOfLastGridPoint', u'latitudeOfLastGridPointInDegrees', u'longitudeOfLastGridPoint', u'longitudeOfLastGridPointInDegrees', u'iDirectionIncrement', u'iDirectionIncrementInDegrees', u'N', u'scanningMode', u'iScansNegatively', u'jScansPositively', u'jPointsAreConsecutive', u'alternativeRowScanning', u'iScansPositively', u'scanningMode4', u'scanningMode5', u'scanningMode6', u'scanningMode7', u'scanningMode8', u'global', u'numberOfDataPoints', u'numberOfValues', u'latLonValues', u'latitudes', u'longitudes', u'distinctLatitudes', u'distinctLongitudes', u'PVPresent', u'PLPresent', u'numberOfOctectsForNumberOfPoints', u'interpretationOfNumberOfPoints', u'pl', u'lengthOfHeaders', u'missingValue', u'tableReference', u'section4Length', u'halfByte', u'dataFlag', u'binaryScaleFactor', u'referenceValue', u'referenceValueError', u'sphericalHarmonics', u'complexPacking', u'integerPointValues', u'additionalFlagPresent', u'orderOfSPD', u'boustrophedonic', u'hideThis', u'packingType', u'bitsPerValue', u'constantFieldHalfByte', u'bitMapIndicator', u'values', u'numberOfCodedValues', u'packingError', u'unpackedError', u'maximum', u'minimum', u'average', u'numberOfMissing', u'standardDeviation', u'skewness', u'kurtosis', u'isConstant', u'dataLength', u'changeDecimalPrecision', u'decimalPrecision', u'bitsPerValueAndRepack', u'scaleValuesBy', u'offsetValuesBy', u'gridType', u'getNumberOfValues', u'section5Length', 'analDate', 'validDate']
#
#
#grb.__getattribute__('analDate')
#datetime.datetime(1979, 1, 1, 0, 0)
#>>> grb.__getattribute__('validDate')
#datetime.datetime(1979, 1, 1, 0, 0)
#>>> grb.__getattribute__('dataTime')
#0
#>>> grb.__getattribute__('julianDay')
#2443874.5
#>>> grb.__getattribute__('day')
#1
#>>> grb.__getattribute__('hour')
#0
#>>> grb.__getattribute__('minute')
#0
#>>> grb.__getattribute__('second')
#0
#>>> grb.__getattribute__('centuryOfReferenceTimeOfData')
#20
#
#>>> grb['validityTime']  # this is the data i am after
#900
#
#>>> grb_evap_current.__getattribute__('endStep') 
#  3 6 9 12 18 24
