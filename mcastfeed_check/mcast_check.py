#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

#import variables from web-form
if form.getvalue('subject'):
   subject = form.getvalue('subject')
else:
   subject = "Not set"

print 'Content-type: text/html\r\n\r'
print '<html>' #start of html output

print "<html>"
print "<head>"
print "<title>iapula</title>"
print "</head>"
print "<body>"
print "<h2> Selected Button is %s</h2>" % subject
print "</body>"


#program start
#program end


print '</html>'	#end html page
