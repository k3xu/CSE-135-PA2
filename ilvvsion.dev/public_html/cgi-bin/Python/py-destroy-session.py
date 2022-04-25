#!/usr/bin/python3
import os
import cgi
from http import cookies

cookie = cookies.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')

cookie.load(cookie_string)
cookie['PHPSESSID']['expires'] = 0
cookie['name']['expires'] = 0
print (cookie)

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n\n")
print ("<html>")
print ("<body>")
print ("<h1>Session Destroyed</h1>")

print ('<a href=\'../py-cgiform.html\'>Back to the Python CGI Form</a><br />')
print ('<a href=\'./py-sessions-1.py\'>Back to Page 1</a><br />')
print ('<a href=\'./py-sessions-2.py\'>Back to Page 2</a><br />')
print ("</html>")
print ("</body>")
