#!/usr/bin/python

#import variables from web-form
mydevice = form.getvalue('mydevice')
mymodule = form.getvalue('mymodule')
myport = form.getvalue('myport')


print 'Content-type: text/html\r\n\r'
print '<html>' #start of html output

#program start

import paramiko
import base64
b64pass = base64.b64decode("Y2ljaTE=")
b64usr = base64.b64decode("dmppZWFudQ==")
int_check = "show interface " + "Gig"+ mymodule + "/" + port + " status"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(device, port=22, username=b64usr, password=b64pass)
stdin, stdout, stder = ssh.exec_command(int_check)
output_int_check = stdout.readlines()
print '\n'.join(output_int_check)
ssh.close()

#program end
