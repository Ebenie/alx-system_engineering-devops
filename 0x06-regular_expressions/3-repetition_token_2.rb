#!/usr/bin/env ruby
# This ruby script check if the argument is provided matches.

if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

pattern = /#{ARGV[0]}/
testing_string = "hbn,hbtn,hbttn,hbtttn,hbttttn"
match_string = "hbtn,hbttn,hbtttn,hbttttn"

matches = testing_string.scan(pattern)
puts "Matches found:"
matches.each do |match|
  puts match
end
