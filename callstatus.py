print (" Starting script, importing modules.....")
import requests
from xml.etree import ElementTree as ET
import base64
import json
import datetime

print (str(datetime.datetime.now()) + " Modules imported")
print (str(datetime.datetime.now()) + " Reading config file.......")

with open("config.json") as configfile:
        config = json.load(configfile)
        myIP = config['ENDPOINT']['myIP']
        myUsername = config['ENDPOINT']['myUsername']
        myPassword = config['ENDPOINT']['myPassword']

print (str(datetime.datetime.now()) + " Config file read")
authString = base64.b64decode(myUsername+':'+myPassword)
print (str(datetime.datetime.now()) + " Base64 Auth string created")

def onAcall(IP):
    url = "http://"+ IP +"/getxml"
    querystring = {"location":"/Status/Call"}
    headers = {
        'Authorization': "Basic aW50ZWdyYXRvcjppbnRlZ3JhdG9y",
        }
    print(str(datetime.datetime.now()) + " Sending HTTP request......")
    response = (requests.request("GET", url, headers=headers, params=querystring))
    print(str(datetime.datetime.now()) + " Response received")
    print(str(datetime.datetime.now()) + " About to parse XML")
    xmlResponse = ET.fromstring(response.text)
    for data in xmlResponse:
        if "Empty Result" in data:
            return False
        elif "Call" in data:
            return True

if onAcall(myIP):
    print(str(datetime.datetime.now()) + " Endpoint with IP address " + myIP + " is on a call")
else:
    print(str(datetime.datetime.now()) + " Endpoint with IP address " + myIP + " is available, and not on a call")

