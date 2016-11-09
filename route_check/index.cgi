#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>AM3 Routing Check:</h1>'

#HTML Form - Text Box
print '<form action="route_check.py" method="get">'
print 'Device: <input type="text" name="mydevice">  <br />'
print '<input type="submit" value="Verify" />'
print '</form>'


#HTML Form - Text Area
#print '<form action="next_command.execute.cgi" method="post" target="_blank">'
#print '<textarea name="textcontent" cols="100" rows="10">'
#print 'Command or block of commands to run'
#print '</textarea>'
#print '<input type="submit" value="Submit" />'
#print '</form>'

#HTML Form - Dropdown Menu
print '<form action="route_check.py" method="post" target="_blank">'
print '<select name="dropdown">'
print '<option value="vrf-accmedia" selected>vrf-accmedia</option>'
print '<option value="vrf-devmedia">vrf-devmedia</option>'
print '<option value="vrf-media">vrf-media</option>'
print '<option value="vrf-mediamanagement">vrf-mediamanagement</option>'
print '<option value="vrf-office">vrf-office</option>'
print '<option value="vrf-poc">vrf-poc</option>'
print '<option value="vrf-public">vrf-public</option>'
print '<option value="vrf-tstmedia">vrf-tstmedia</option>'
print '<option value="vrf-devmedia">vrf-devmedia</option>'
print '<option value="vrf-video">vrf-video</option>'
print '<option value="vrf-voip">vrf-voip</option>'
print '</select>'
print '<input type="submit" value="Submit"/>'
print '</form>'


print '</html>'
