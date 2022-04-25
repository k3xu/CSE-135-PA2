#!/usr/bin/python3
import os
import cgi

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n\n")
print ("<html>")

print ("<body>")
print ("<h1 align=center>GET query string</h1>")
print ("<hr/>")

print("<p><b>Raw query string: " + os.environ['QUERY_STRING'] + "</b></p>")

query_string = cgi.FieldStorage()
print("<p><b>Formatted query string: </b></p>")
for key in query_string:
    #print(cgi.parse())
    print("<p>",query_string[key].value,"</p>")

print ("</body>")
print ("</html>")
