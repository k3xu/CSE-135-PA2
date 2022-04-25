#!/usr/bin/python3
import os

print ("Cache-Control: no-cache")
print ("Content-type: text/html\r\n")
print ('\r\n')
print ("<html>")
print ("<head>")
print ("<h1 align=center>Environment Variables</h1>")
print ("</head>")
print ("<body>")
print ("<hr/>")
print ("<h2>Environment Variables</h2>")
print ("<ul>")

for key in os.environ:
    print("<li>",key,": ", os.getenv(key),"</li>")

print ("</ul>")

#print ("<h2>Server Variables</h2>")
#for key in os.environ:
    #print("<li>",key,": ", os.getenv(key),"</li>")

print ("</body>")
print ("</html>")





#print("<ul>")

#print("</ul>")

#print("<li><b>key:</b> value</li>")
    #echo "<ul>";
    #$env_array = getenv();
    #foreach ($env_array as $key=>$value) {
    #echo "<li><b>$key</b> : $value</li>";
    #};

    #echo "</ul>";

    #echo "<h2>Server Variables</h2>";
    #echo "<ul>";
    #$env_array = getenv();

    #foreach ($_SERVER as $key=>$value) {
    #echo "<li><b>$key:</b> $value</li>";
    #};
