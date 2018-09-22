import mechanize

theurl = 'http://192.168.1.20/login.cgi'
mech = mechanize.Browser()
mech.open(theurl)

mech.select_form(nr=0)
mech["userid"] = "ubnt"
mech["password"] = "1234"
results = mech.submit().read()
