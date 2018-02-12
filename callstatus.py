import requests
from xml.etree import ElementTree as ET
import base64
import json

with open("config.json") as configfile:
        config = json.load(configfile)
        myIP = config['ENDPOINT']['myIP']
        myUsername = config['ENDPOINT']['myUsername']
        myPassword = config['ENDPOINT']['myPassword']

authString = base64.b64decode(myUsername+':'+myPassword)

def onAcall(IP):
    url = "http://"+ IP +"/getxml"
    querystring = {"location":"/Status/Call"}
    headers = {
        'Authorization': "Basic aW50ZWdyYXRvcjppbnRlZ3JhdG9y",
        }
    response = (requests.request("GET", url, headers=headers, params=querystring))
    xmlResponse = ET.fromstring(response.text)
    for data in xmlResponse:
        if data.tag == 'Call':
            TransmitCallRate = data[2].text
            return True, TransmitCallRate
        else:
            return False

busy, bandwidth = onAcall(myIP)

if busy:
    print(" Endpoint with IP address " + myIP + " is on a " + bandwidth + "Kbps call")
else:
    print(" Endpoint with IP address " + myIP + " is available, and not on a call")

