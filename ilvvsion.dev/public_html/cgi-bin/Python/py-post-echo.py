#!/usr/bin/python3
import os
import cgi

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n\n")
print ("<html>")

print ("<head>")
print ("</head>")
print ("<body>")
print ("<h1 align=center>Post echo message</h1>")

print ("<p><b>Message body: </b></p>")
print ("<ul>")

query_string = cgi.FieldStorage()
for key in query_string:
    print("<p><b>%s:</b> %s</p>" % (key, query_string[key].value),"</p>")

print ("</ul>")
print ("</body>")
print ("</html>")
