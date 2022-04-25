#!/usr/bin/ruby
require 'json'

print "Cache-Control: no-cache\n"
print "Content-type: application/json\n\n"

date = Time.now
address = ENV['REMOTE_ADDR']

message = {'title' => 'Hello, Team IJK!', 'heading' => 'Hello, Team IJK!', 'message' => 'This page was generated with the Perl programming language', 'time' => date, 'IP' => address}

json_message = message.to_json
print "#{json_message}\n";
