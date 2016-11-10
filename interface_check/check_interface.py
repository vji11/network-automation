#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

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
int_check = "show interface " + "Gig" + mymodule + "/" + myport
sh_run_int = "show run interface " + "Gig" + mymodule + "/" + myport

#initiate ssh connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#run command on device and get read the output
ssh.connect(mydevice, port=22, username=b64usr, password=b64pass)
stdin, stdout, stder = ssh.exec_command(int_check)
output_int_check = stdout.readlines()
print '\n'.(output_int_check)
ssh.close()

#reading the input and parsing
for line in output_int_check:
    if 'media' in line:
        myduplex = (line.split()[0].strip('('))

for line in output_int_check:
    if 'media' in line:
        myspeed = (line.split()[1].strip('('))

for line in output_int_check:
    if 'CRC' in line:
        myinputerrors = (line.split()[0].strip('('))

#run command on device and get read the output
ssh.connect(mydevice, port=22, username=b64usr, password=b64pass)
stdin, stdout, stder = ssh.exec_command(sh_run_int)
output_sh_run_int = stdout.readlines()
#print '\n'.join(output_sh_run_int)
ssh.close()


for line in output_sh_run_int:
    if 'vlan' in line:
        my_vlan = (line.split()[3].strip('('))

#printing output
print "Duplex of the interface is: "+ myduplex
print('<br />')
print "Speed of the interface is: " + myspeed  
print('<br />')
print "Input errors on the interface: " + myinputerrors
print('<br />')
print "Access VLAN: " + my_vlan
print('<br />')

#program end

print '</html>'	#end html page
