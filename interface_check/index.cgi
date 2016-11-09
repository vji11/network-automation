#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>Cisco Switch Check Interface Status</h1>'
print '<form action="next_check_interface.cgi" method="get">'
print 'Device: <input type="text" name="mydevice">  <br />'
print 'Module: <input type="text" name="mymodule">  <br />'
print 'Port: <input type="text" name="myport">  <br />'
print '<input type="submit" value="Verify" />'
print '</form>'
print '</html>'
