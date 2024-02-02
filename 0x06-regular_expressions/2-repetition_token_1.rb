#!/usr/bin/env ruby
# This ruby script xtracts patterns matching hb?t?n from the input argument

matches = ARGV[0].scan(/hb?t?n/)
puts matches.join
