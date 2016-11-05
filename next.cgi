#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

device = form.getvalue('device')
image = form.getvalue('image')
os_size = form.getvalue('os_size')
md5_sum = form.getvalue('md5_sum')

print 'Content-type: text/html\r\n\r'
print '<html>' #start of html output

print device  <br/>

import paramiko
import base64

b64pass = base64.b64decode("Y2ljaTE=")
b64usr = base64.b64decode("dmppZWFudQ==")
md5_check = "show file " + image + " " + "md5sum"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(device, port=22, username=b64usr, password=b64pass)
stdin, stdout, stder = ssh.exec_command(md5_check)
output2 = stdout.readlines()
ssh.close()

if any(md5_sum in s for s in output2):
	print "Upload Succesfull" + "md5 " + md5_sum + " " + "checksum verified. Upload Succesfull."
else:
	print "Upload Failed." + "Original Checksum " + md5_sum + " " + "differ from calculated checksum"

print '</html>'	#end html page