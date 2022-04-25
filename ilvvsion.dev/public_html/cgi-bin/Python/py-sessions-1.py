#!/usr/bin/python3
import os
import cgi
import hashlib, time
from http import cookies

cookie = cookies.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
name = "You do not have a name set"

if os.environ['REQUEST_METHOD'] == 'POST':
    if not cookie_string:
        sid = hashlib.sha256((repr(time.time())).encode('utf-8')).hexdigest()
        cookie['PHPSESSID'] = sid
        try:
            cookie['name'] = cgi.FieldStorage()['username'].value
        except:
            cookie['name'] = name
    else:
        cookie.load(cookie_string)
        sid = cookie['PHPSESSID'].value
        try:
            cookie['name'] = cgi.FieldStorage()['username'].value
        except:
            cookie['name'] = name

    print (cookie)
else:
    try:
        cookie.load(cookie_string)
        sid = cookie['PHPSESSID'].value
        name = cookie['name'].value
    except:
        name = "You do not have a name set"

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n\n")
print ("<html>")
print ("<body>")
print ("<h1>Python Sessions 1</h1>")

try:
    name = cookie['name'].value
except:
    name = "You do not have a name set"


print ("<p><b>Name: </b>", name)
print ("<br />")
print ('<a href=\'./py-sessions-2.py\'>Session Page 2</a><br />')
print ('<a href=\'../py-cgiform.html\'>Python CGI Form</a><br />')
print ('<form style=\'margin-top:30px\' action=\'./py-destroy-session.py\' method=\'get\'>')
print ("</form>")
print ("</body>")
print ("</html>")
