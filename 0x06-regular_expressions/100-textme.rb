#!/usr/bin/env ruby
# This ruby script check if the argument is provided matches.

regex = /hbt*n/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join(",")
