#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

print ('Content-type: text/html\r\n\r')
print ('<html>')
print ('<h1>Playout Multicast Routing Check:</h1>')

#HTML Form - Radio Button
print ('<form action="mcast_check.py" method="post" target="_blank">')
print ('<input type="radio" name="web_select" value="mcast_src_feed" /> Check Playout Mcast Source Feed')
print ('<br>')
print ('<input type="submit" value="Check" />')
print ('</form>')