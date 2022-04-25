#!/usr/bin/ruby
print "Cache-Control: no-cache\n"
print "Content-type: text/html \n\n"

# print HTML file top
print <<"EOS"
<!DOCTYPE html>
<html><head><title>Environment Variables</title>
</head><body><h1 align="center">Environment Variables</h1>
<hr>
EOS

# Loop over the environment variables and print each variable and its value
ENV.each_pair{|key, value| print "<b>#{key}:</b> #{value}<br />\n"}

# Print the HTML file bottom
print "</body></html>"
