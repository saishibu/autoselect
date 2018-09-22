import mechanize,ssl

theurl = 'https://192.168.1.20/login.cgi'
ssl._create_default_https_context = ssl._create_unverified_context
mech = mechanize.Browser()
mech.set_handle_robots(False)
mech.open(theurl)

mech.select_form(nr=0)
mech["userid"] = "ubnt"
mech["password"] = "1234"
results = mech.submit().read()
