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

print '<form action="next_command.execute.cgi" method="post" target="_blank">'
print '<textarea name="textcontent" cols="100" rows="10">'
print 'Command or block of commands to run'
print '</textarea>'
print '<input type="submit" value="Submit" />'
print '</form>'

print '<form action="/cgi-bin/dropdown.py" method="post" target="_blank">'
print '<select name="dropdown">'
print '<option value="Maths" selected>Maths</option>'
print '<option value="Physics">Physics</option>'
print '</select>'
print '<input type="submit" value="Submit"/>'
print '</form>'