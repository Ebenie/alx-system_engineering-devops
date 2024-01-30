#!/usr/bin/env ruby

regex = /hbt{0,}n/
input = ARGV[0]

puts input.match(regex)

