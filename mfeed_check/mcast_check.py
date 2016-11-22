#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

#import variables from web-form
if form.getvalue('web_select'):
   web_select = form.getvalue('web_select')
else:
   web_select = "Not set"

print ('Content-type: text/html\r\n\r')
print ('<html>') #start of html output

#program start

import paramiko
import base64
b64usr = base64.b64decode("c29sYXJweXRob24=")
b64pass = base64.b64decode("M0QzN3ZnSjE4K1pX")
mroute_check = "show ip mroute vrf vrf-video | i 1/1"
mydeviceA = '10.149.132.205'
mydeviceB = '10.149.132.206'
primary_interface = 'GigabitEthernet1/1'
backup_interface = 'GigabitEthernet1/11'
primary_appertv = 'ATVP001'
backup_appertv = 'ATVP002'
command1 = "show stuff"
ssh = paramiko.SSHClient()

#if SSH certificate is not in hosts file automatically accept it
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print ('<h2>Multicast route for network path A via rtmcasta0101:</h2>')

while web_select == 'mcast_src_feed':
    #initiate ssh connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #run command on device and get read the output
    ssh.connect(mydeviceA, port=22, username=b64usr, password=b64pass)
    stdin, stdout, stder = ssh.exec_command(mroute_check)
    output1 = stdout.readlines()
#   print ('\n'.join(output1)
    ssh.close()
    break

if any(backup_interface in s1 for s1 in output1):
    print ("\nSource interface of MCAST Route is " + backup_interface)
    print ('<br>')
    print ("\nVideo feed is " + backup_appertv)
else:
    print ("\nSource interface of MCAST Route is " + primary_interface)
    print('<br />')
    print ("\nVideo feed is " + primary_appertv)

print ('<br />')
print ("=============================================================")
print ('<br />')
print ('<h2>Multicast route for network path B via rtmcastb0102:</h2>')

while web_select == 'mcast_src_feed':
    #initiate ssh connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #run command on device and get read the output
    ssh.connect(mydeviceB, port=22, username=b64usr, password=b64pass)
    stdin, stdout, stder = ssh.exec_command(mroute_check)
    output2 = stdout.readlines()
#   print ('\n'.join(output2))
    ssh.close()
    break

if any(backup_interface in s2 for s2 in output2):
    print ("\nSource interface of MCAST Route is " + backup_interface)
    print ('<br />')
    print ("\nVideo feed is " + backup_appertv)
else:
    print ("\nSource interface of MCAST Route is " + primary_interface)
    print ('<br />')
    print ("\nVideo feed is " + primary_appertv)   

#program end
print ('</html>') #end html page