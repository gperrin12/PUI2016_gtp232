import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

def getMtaData(busline, mtakey = str(os.getenv("MTAKEY")), output = 'bus.json'):
	api = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mtakey + '&VehicleMonitoringDetailLevel=calls&LineRef='+ busline

	def get_jsonparsed_data(url):
    		"""
    		from http://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    		Receive the content of ``url``, parse it as JSON and return the object.

    		Parameters
    		----------
    		url : str

    		Returns
    		-------
    		dict
    		"""

		response = urllib.urlopen(url)
		data = response.read().decode("utf-8")
		return json.loads(data)
	
	jsonData = get_jsonparsed_data(api)

	with open(output, 'w') as outfile:
		json.dump(jsonData, outfile) 
