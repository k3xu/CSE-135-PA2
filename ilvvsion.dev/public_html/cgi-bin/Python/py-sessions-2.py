#!/usr/bin/python3
import os
import cgi
import hashlib, time
from http import cookies

cookie = cookies.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')

if not cookie_string:
    name = "You do not have a name set"
else:
    cookie.load(cookie_string)
    sid = cookie['PHPSESSID'].value
    name = cookie['name'].value

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n\n")
print ("<html>")
print ("<body>")
print ("<h1>Python Sessions 2</h1>")

try:
    name = cookie['name'].value
except:
    name = "You do not have a name set"

print ("<p><b>Name: </b>", name)
print ("<br />")
print ('<a href=\'./py-sessions-1.py\'>Session Page 1</a><br />')
print ('<a href=\'../py-cgiform.html\'>Python CGI Form</a><br />')
print ('<form style=\'margin-top:30px\' action=\'./py-destroy-session.py\' method=\'get\'>')
print ('<button type=\'submit\'>Destroy Session</button>')
print ("</form>")
print ("</body>")
print ("</html>")
