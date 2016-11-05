#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

keyword = form.getvalue('keyword')

print 'Content-type: text/html\r\n\r'
print '<html>'
print device
print image
print os_size
print md5_sum
print '</html>'