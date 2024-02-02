#!/usr/bin/env ruby
# This ruby script check if the argument is provided matches.

if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

pattern = /(hbtn|htn)+/
matches = ARGV[0].scan(pattern)
