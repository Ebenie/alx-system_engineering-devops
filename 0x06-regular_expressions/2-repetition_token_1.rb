#!/usr/bin/env ruby
# This Ruby script checks if a string argument is provided from the command line, defines a regular expression pattern to match "htn" or "htbn" patterns, then matches

if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

pattern = /ht(n|bn)/

input_string = ARGV[0]

match = input_string.match(pattern)

if match
  puts "Match found: #{match[0]}"
else
  puts "No match found"
end
