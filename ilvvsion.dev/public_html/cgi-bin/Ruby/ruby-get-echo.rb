#!/usr/bin/ruby

require "cgi"

print "Cache-Control: no-cache\n"
print "Content-type: text/html \n\n"

# print HTML file top
print <<"EOS"
<!DOCTYPE html>
<html><head><title>GET Request Echo</title>
</head><body><h1 align="center">Get Request Echo</h1>
<hr>
EOS

# The Query String is simply an environment variable

env_query_string = ENV['QUERY_STRING']
print "<b>Query String:</b> #{env_query_string}<br />\n"

# Credit for this code to parse the Query string:
# https://www.mediacollege.com/internet/perl/query-string.html

=begin
if env_query_string.length > 0
  buffer = ENV['QUERY_STRING']
  pairs = buffer.split("&")
  pairs.each do |pair|
    name, value = pair.split("=")
    value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    in[name] = value
  end
end

#Print out the Query String
loop_var = 0
in.each do |key|
  loop_var += 1
  if loop_Var % 2 != 0 
    print "#{key} = #{in[key]}<br/>\n"
  end
end  

=end

#=begin
cgi = CGI.new
params = cgi.params

params.each do |key|
  print "#{key} = #{params[key]}<br/>\n"
end
#=end



# Print the HTML file bottom
print "</body></html>"
