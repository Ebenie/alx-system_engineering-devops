#!/usr/bin/env ruby
#This ruby script find regular expression to check if the argument is provided

def match_regex(argument)
  pattern = /hbt{2,5}n/
  if argument.match?(pattern)
    puts "Match found: #{argument}"
  else
    puts "No match found for #{argument}"
  end
end

if ARGV.length != 1
  puts "Usage: ruby 2-repetition_token_1.rb <argument>"
else
  match_regex(ARGV[0])
end
