#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

device = form.getvalue('device')
image = form.getvalue('image')
os_size = form.getvalue('os_size')
md5_sum = form.getvalue('md5_sum')

print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>Performing the following upgrade</h1>'
print device <br />
print image <br />
print os_size <br />
print md5_sum <br />
print '</html>'