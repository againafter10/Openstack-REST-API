
#!/usr/bin/env python


######################################################
# illustrate the use of the OpenStack
# REST API
######################################################

############# These libraries are required ###########
import urllib2
import json

############### Configuration Section ################
############### Enter your own values ################
# OpenStack server address
# Can be IP address or DNS name
# Can be 127.0.0.1  (localhost) but usually isn't
# hostIP="192.168.1.106"
hostIP="localhost"

# Domain, User, Password
mydomainname= "default"
myusername=   "admin"
mypassword=   "admin_user_secret"


############### OpenStack API ports ########
# Make sure that these ports are open in the Control Node
# and that VirtualBox Port Forwarding (if used) is properly set
# Note that keystone administration port 35357 is no longer needed in v3,
# it is only there for backward compatibility with v2.
# All Keystone operations now go through port 5000
NOVAport         = "8774"
CINDERport       = "8776"
CEILOMETERport   = "8777"
GLANCEport       = "9292"
NEUTRONport      = "9696"
AWSport          = "8000"
HEATport         = "8004"
KEYSTONEport     = "5000"


################## Sample code logic starts here #######################################
print
print
print "********************************************"
print "* Obtain authorization token from Keystone *"
print "********************************************"
print "" ; print ""


print "Build the request headers, URL and body and POST everything      "
print"--------------------------------------------------------------------------"


#### Build the request headers
headers = {
          'Content-Type'   :   'application/json',
          'Accept'         :   'application/json'
           }
print "REQUEST HEADERS:" ; print headers

#### Build the request URL
CMDpath="/v3/auth/tokens"
APIport=KEYSTONEport
url="http://"+hostIP+":"+APIport+CMDpath
print "REQUEST URL:" ; print url

#### Build the request body
body='{"auth":{"identity":{"methods":["password"],"password":{"user":{"name":"'+myusername+'","domain":{"name":"'+mydomainname+'"},"password":"'+mypassword+'"}}}}}'
print "REQUEST BODY:" ; print body
print"--------------------------------------------------------------------------"
print "" ; print ""

#### Send the  POST request
req = urllib2.Request(url, body, headers)

quit()


print "Read the response headers and body"
print"--------------------------------------------------------------------------"

#### Read the response header
header = urllib2.urlopen(req).info()
print "RESPONSE HEADER" ; print "===============" ; print header


#### Read the response body
response = urllib2.urlopen(req).read()
print "RESPONSE BODY" ; print"=============" ; print response
print"--------------------------------------------------------------------------"
print ""
print ""

quit()

print "Decode the response header and body"
print"------------------------------------"

mytoken = header.getheader('X-Subject-Token')
print "KEYSTONE TOKEN (X-Subject-Token)" ; print "================================" ; print mytoken ; print ""


#### Convert response body to pretty print format
decoded = json.loads(response.decode('utf8'))
pretty = json.dumps(decoded,sort_keys=True,indent=3)
print "RESPONSE BODY IN PRETTY FORMAT" ; print "==============================" ; print pretty ; print "" ; print ""


#### Parse JSON formatted data for token issue date
issued = decoded['token']['issued_at']
print "TOKEN WAS ISSUED" ; print "================" ; print issued ; print "" ; print ""


#### Parse JSON formatted data for token expiration date
expires = decoded['token']['expires_at']
print "TOKEN WILL EXPIRE" ; print "=================" ; print expires ; print "" ; print ""
print "" ; print ""

quit()


############## List the NOVA API-v2 details #######

print "*****************************************"
print "*  Get list of the NOVA API-v2 details  *"
print "*****************************************"
print ""

print "Build the request headers, URL and body and GET everything"
print "-----------------------------------------------------------"

#### Build the headers
headers = {
          'Content-Type'   :   'application/json',
          'Accept'         :   'application/json',
          'X-Auth-Token'   :    mytoken
           }
print "REQUEST HEADERS" ; print "================" ; print headers ; print "" ; print ""


#### Build the URL
CMDpath="/v2"
APIport=NOVAport
url="http://"+hostIP+":"+APIport+CMDpath
print "URL" ; print "===" ; print url ; print "" ; print ""


#### Send the GET request
# Note that the second parameter which normally carries the body data
# is "None", making the request a "GET" instead of a "POST"
req = urllib2.Request(url, None, headers)

#### Read the response
response = urllib2.urlopen(req).read()

#### Convert to JSON format
decoded = json.loads(response.decode('utf8'))

#### Make it look pretty and indented
pretty = json.dumps(decoded,sort_keys=True,indent=3)
print "RESPONSE (FORMATTED)" ; print "====================" ; print pretty ; print "" ; print ""



quit()
