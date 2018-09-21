#!usr/bin/python

import urllib, urllib2, cookielib
import ssl,json,time

url='https://192.168.179.65/login.cgi'
ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open(url)
login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
r=opener.open(url,login_data)
print "login success"
url='https://192.168.179.65/status.cgi'
status_page=opener.open(url)
status=status_page.read()
json_status=json.loads(status)
signal=json_status['wireless']['signal']
rssi=json_status['wireless']['rssi']
noise=json_status['wireless']['noisef']
ccq=json_status['wireless']['ccq']
distance=json_status['wireless']['distance']
txrate=json_status['wireless']['txrate']
rxrate=json_status['wireless']['rxrate']
freq=json_status['wireless']['frequency']
channel=json_status['wireless']['channel']

print signal
