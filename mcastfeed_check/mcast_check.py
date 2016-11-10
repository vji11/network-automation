#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

#import variables from web-form
if form.getvalue('subject'):
   web_select = form.getvalue('subject')
else:
   web_select = "Not set"

print 'Content-type: text/html\r\n\r'
print '<html>' #start of html output



#program start

import paramiko
import base64
b64pass = base64.b64decode("Z2l6bW9YMTEx")
b64usr = base64.b64decode("dmppZWFudQ==")
mroute_check = "show ip mroute vrf vrf-video | i 1/1"
command1 = "show stuff"

while web_select == 'mcast_src_feed':
	#initiate ssh connection
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#run command on device and get read the output
	ssh.connect(mydevice, port=22, username=b64usr, password=b64pass)
	stdin, stdout, stder = ssh.exec_command(mroute_check)
	output_int_check = stdout.readlines()
	ssh.close()

#reading the input and parsing
for line in mroute_check:
    if '1/11' in line:
        my_mroute = (line.split()[2].strip('('))
        print 'multicast source feed is B: ' + my_mroute
    else:
    	my_mroute = (line.split()[2].strip('('))
    	print 'multicast source feed is A: ' + my_mroute

#program end
print '</html>'	#end html page
