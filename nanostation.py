#!usr/bin/python
#wmode
#sta
#ap


import urllib, urllib2, cookielib
import ssl,json,time

import mechanize
from bs4 import BeautifulSoup

url='https://192.168.1.20/login.cgi'
ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open(url)
login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
r=opener.open(url,login_data)
print "login success"

url2='https://192.168.179.65/link.cgi'
r=opener.open(url2)
login_data=urllib.urlencode({'wmode':'sta'})
r=opener.open(url2,login_data)
print r


#br = mechanize.Browser()
#br.open(url2)
#print(br.title())
