#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>NX-OS Upload</h1>'
print '<form action="web_os_upgrade.py" method="get">'
print 'Device to upgrade: <input type="text" name="device">  <br />'
print 'VRF: <input type="text" name="my_vrf">  <br />'
print 'TFTP Server: <input type="text" name="tftp_server">  <br />'
print 'NX-OS Image: <input type="text" name="image">  <br />'
print 'NX-OS size in bytes: <input type="text" name="os_size">  <br />'
print 'MD5 Checksum: <input type="text" name="md5_sum">  <br />'
print 'Username: <input type="text" name="myuser">  <br />'
print 'Username: <input type="password" name="mypass">  <br />'
print '<input type="submit" value="Do Upgrade" />'
print '</form>'
print '</html>'