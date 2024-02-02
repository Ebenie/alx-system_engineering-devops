#!/usr/bin/env ruby
# This script extracts patterns matching hbt+n from the input argume

matches = ARGV[0].scan(/hbt+n/)
puts matches.join
