#!/usr/bin/env ruby
#This ruby script find regular expression to check if the argument is provided

input = ARGV[0]

def match_regex(input)
  regex = /hb+t*n/
  return input.match(regex)
end

if input.nil?
  puts "Please input a string."
else
  puts match_regex(input)
end
