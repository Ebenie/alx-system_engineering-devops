#!/usr/bin/env ruby
#This ruby script find regular expression to check if the argument is provided

if ARGV.empty?
  exit 1
end
regex = /hb+t*n/
matches = ARGV[0].scan(regex)
input = ARGV[0]
puts input.match(regex)
