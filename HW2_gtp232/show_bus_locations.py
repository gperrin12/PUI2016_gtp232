import sys
import json
import csv
import pandas as pd
import getMtaData as gmd

mtakey = sys.argv[1]
busline = sys.argv[2]

download = False #turn off for testing to avoid pinging the api too much

# download and read the data

if(download):
  gmd.getMtaData(busline, mtakey, 'bus.json')

with open('bus.json') as data_file:    
  data = json.load(data_file)

buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#count the number of buses
num_buses = 0
buses_clean = []
for i in range(len(buses)):
	num_buses += 1
	bus_number = i
	bus_lat = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	bus_lon = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	bus_new = [bus_number, bus_lat, bus_lon]
	buses_clean.append(bus_new)


print "Bus Line : " + str(busline)
print "Number of Active Buses : " + str(num_buses)
for i in range(len(buses_clean)):
	print "Bus " + str(buses_clean[i][0]) + " is at latitude " + str(buses_clean[i][1]) + " and longitude " + str(buses_clean[i][2])


