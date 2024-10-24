import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json
import ssl

data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Email: ', tree.find('email').get('hide'))

data_json = '''[
{"id": "001",
"x": "2",
"name": "Chuck"},
{"id": "009",
"x": "7",
"name": "Brent"}
]'''

info = json.loads(data_json)
print ('User Count: ', len(info))

for person in info: #loop through the list o
    print('Name:', person['name'])
    print('ID: ',person['id'])


api_key = False

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
    print(data)
    continue

print(json.dumps(js, indent=4))
lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)

#read api docs to get around how to access the api