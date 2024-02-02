#!/usr/bin/env ruby
# This ruby script that accepts a string argument and matches it against a regular expression pattern to find occurrences of "hbtn", "hbttn", "hbtttn", or "hbttttn".

if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

pattern = /hb(t{2,5})n/

input_string = ARGV[0]

match = input_string.match(pattern)
if match
  puts "Match found: #{match[0]}"
else
  puts "No match found"
end
