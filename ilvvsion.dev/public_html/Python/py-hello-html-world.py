#!/usr/bin/python3
from datetime import date
from datetime import datetime
import os

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n")
print ('\r\n')
print ("<html>")
print ("<head>")
print ("<title>Hello Team IJK</title>")
print ("</head>")
print ("<body>")
print ("<h1 align=center>Hello Team IJK</h1>")
print ("<p>Hello Team IJK</p>")
print ("<p> This page was generated with the Python programming language</p>")
print ("<p>This program was run at: ", date.today().strftime("%m/%d/%y"), datetime.now().strftime("%H:%M:%S %Y"), "</p>")
print ("<p>Your current IP address is ", os.getenv('REMOTE_ADDR'), "</p>")
print ("</body>")
print ("</html>")
