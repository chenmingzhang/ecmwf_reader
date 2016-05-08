from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim_land",
    "date": "1979-01-01/to/1979-12-31",
    "expver": "2",
    "levtype": "sfc",
    "param": "182.128/228.128",     # this line represents which type of property you wish to retrieve 182.128 is evaporation, 228.128 is precipitation
    "step": "3/6/9/12/18/24",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    "target": "CHANGEME",
})


# evaporation only
#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim_land",
    "date": "1979-01-01/to/1979-12-31",
    "expver": "2",
    "levtype": "sfc",
    "param": "182.128",
    "step": "3/6/9/12/18/24",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    "target": "CHANGEME",
})


# precipitation only
#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim_land",
    "date": "1979-01-01/to/1979-12-31",
    "expver": "2",
    "levtype": "sfc",
    "param": "228.128",
    "step": "3/6/9/12/18/24",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    "target": "CHANGEME",
})
