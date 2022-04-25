#!/usr/bin/ruby
require "cgi"

print "Cache-Control: no-cache"
print "Content-type: text/html\r\n\n"
print "<html>"

print ("<head>")
print ("</head>")
print ("<body>")
print ("<h1 align=center>Post echo message</h1>")

print ("<p><b>Message body: </b></p>")
print ("<ul>")

cgi = CGI.new
params = cgi.params
for key in query_string:
params.each |key| do
    print"<p><b>#{key}:</b> #{params[key]}</p>"
end

print ("</ul>")
print ("</body>")
print ("</html>")
