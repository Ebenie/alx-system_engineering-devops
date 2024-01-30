#!/usr/bin/env ruby

regex = /[A-Z]/
input = ARGV[0]

puts input.scan(regex).join

