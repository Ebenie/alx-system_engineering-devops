#!/usr/bin/env ruby

regex = /^[0-9]{10}$/
input = ARGV[0]

puts input.match(regex)

