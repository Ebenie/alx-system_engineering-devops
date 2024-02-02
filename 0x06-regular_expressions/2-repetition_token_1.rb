#!/usr/bin/env ruby
#This ruby script regular expression for matching repetition token #1
regex = /hbt{2,5}n/

input = ARGV[0]

matches = input.scan(regex)

puts matches.join(",")
