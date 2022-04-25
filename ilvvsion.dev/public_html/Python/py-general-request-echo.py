#!/usr/bin/python3
import cgi
import os

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n\n")
print ("<html>")

print ("<body>")
print ("<h1 align=center>General Request Echo</h1>")
print ("<hr/>")

print("<p><b>HTTP Protocol: </b>" + os.environ['SERVER_PROTOCOL'] + "</p>")
print("<p><b>HTTP Method: </b>" + os.environ['REQUEST_METHOD'] + "</p>")
print("<p><b>Query string: " + os.environ['QUERY_STRING'] + "</b></p>")

query_string = cgi.FieldStorage()
print("<p><b>Message body: </b></p>")
try:
    if len(query_string) > 0:
        for key in query_string:
            print("<p>",query_string[key].value,"</p>")
except:
    print('')

print ("</body>")
print ("</html>")
