#!/home/python
import cgi
import cgitb
cgitb.enable()


print 'Content-type: text/html\r\n\r'
print '<html>'
print '<h1>Please enter a keyword of your choice</h1>'
print '<form action="go.py" method="get">'
print 'First Name: <input type="text" name="first_name">  <br />'
print 'Last Name: <input type="text" name="last_name" />'
print '<input type="submit" value="Submit" />'
print '</form>'
print '</html>'