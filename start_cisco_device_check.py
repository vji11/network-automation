#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>Cisco Device Check</h1>'
print '<form action="next_cisco_device_check.cgi" method="get">'
print 'Device: <input type="text" name="mydevice">  <br />'
print '<input type="submit" value="Verify" />'
print '</form>'
print '</html>'