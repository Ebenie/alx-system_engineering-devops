#!/usr/bin/env ruby
# This rub script extract sender, receiver, and flags using regular expression

matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

matches.each do |match|
  puts "#{match[0]},#{match[1]},#{match[2]}"
end
