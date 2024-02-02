#!/usr/bin/env ruby
#This ruby script find regular expression to check if the argument is provided
if ARGV.empty?
  exit 1
end
pattern = /h(b+|tn)+/
matches = ARGV[0].scan(pattern)
