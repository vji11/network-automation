#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue('web_select'):
   web_select = form.getvalue('web_select')
else:
   web_select = "Not set"

print ('Content-type: text/html\r\n\r')
print ('<html>')

import paramiko
import base64
b64usr = base64.b64decode("pepene")
b64pass = base64.b64decode("mamaliga")
mroute_check = "show ip mroute vrf vrf-video | i 1/1"
mydeviceA = '10.149.132.205'
mydeviceB = '10.149.132.206'
primary_interface = 'GigabitEthernet1/1'
backup_interface = 'GigabitEthernet1/11'
primary_appertv = 'ATVP001'
backup_appertv = 'ATVP002'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print ('<h3>Multicast route for network path A via rtmcasta0101:</h3>')

while web_select == 'mcast_src_feed':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mydeviceA, port=22, username=b64usr, password=b64pass)
    stdin, stdout, stder = ssh.exec_command(mroute_check)
    output1 = stdout.readlines()
    ssh.close()
    break

if any(backup_interface in s1 for s1 in output1):
    print ("\nSource interface of MCAST Route is " + backup_interface)
    print ('<br>')
    print ("\nVideo feed is " + backup_appertv)
else:
    print ("\nSource interface of MCAST Route is " + primary_interface)
    print ('<br>')
    print ("\nVideo feed is " + primary_appertv)

print ('<br>')
print ('<h3>Multicast route for network path B via rtmcastb0102:</h3>')

while web_select == 'mcast_src_feed':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mydeviceB, port=22, username=b64usr, password=b64pass)
    stdin, stdout, stder = ssh.exec_command(mroute_check)
    output2 = stdout.readlines()
    ssh.close()
    break

if any(backup_interface in s2 for s2 in output2):
    print ("\nSource interface of MCAST Route is " + backup_interface)
    print ('<br>')
    print ("\nVideo feed is " + backup_appertv)
else:
    print ("\nSource interface of MCAST Route is " + primary_interface)
    print ('<br>')
    print ("\nVideo feed is " + primary_appertv)   

print ('</html>')
