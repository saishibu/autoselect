#!usr/bin/python

import urllib, urllib2, cookielib
import ssl,json,time

import mechanize
from bs4 import BeautifulSoup

url='https://192.168.179.65/login.cgi'
ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open(url)
login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
r=opener.open(url,login_data)
print "login success"

url2='https://192.168.179.65/link.cgi'
br = mechanize.Browser()
br.open(url2)
br.set_handle_redirect(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

for form in br.forms():
    print "Form name: ", form.name
    br.select_form(nr=0) # nr=0 It selects html form without name
