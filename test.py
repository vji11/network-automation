#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>Please enter a keyword of your choice</h1>'
print '<form action="next.cgi" method="get">'
print 'Keyword: <input type="text" name="keyword">  <br />'
print '<input type="submit" value="Submit" />'
print '</form>'
print '</html>'