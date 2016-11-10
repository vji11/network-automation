#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>Playout Multicast Routing Check:</h1>'

#HTML Form - Radio Button
print '<form action="mcast_check.py" method="post" target="_blank">'
print '<input type="radio" name="subject" value="mcast_src_feed" /> Check Playout Mcast Source Feed'
print ('<br>')
print '<input type="radio" name="subject" value="empty_value" /> Empty Value'
print '<input type="submit" value="Check" />'
print '</form>'