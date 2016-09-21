import sys
import json
import csv
import pandas as pd
import getMtaData as gmd

# to run: python get_bus_info.py $MTAKEY B52 B52.csv

mtakey = sys.argv[1]
busline = sys.argv[2]
output = sys.argv[3]

download = True #turn off for testing to avoid pinging the api too much

# download and read the data

if(download):
  gmd.getMtaData(busline, mtakey, 'bus.json')

with open('bus.json') as data_file:    
  data = json.load(data_file)

busses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

busses_clean = [[u'Latitude',u'Longitude',u'Stop Name',u'Stop Status']]
for i in range(len(busses)):
  lat = busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
  lon = busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
  if (busses[i]['MonitoredVehicleJourney']['OnwardCalls']=={}):
	stop = "N/A"
	status = "N/A"
  else:
	stop = busses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
	status = busses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'] 
  bus_new = [lat,lon,stop,status]
  busses_clean.append(bus_new)
 
with open(output, 'wb') as f:   
  writer = csv.writer(f)
  writer.writerows(busses_clean)
