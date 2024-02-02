#!/usr/bin/env ruby
# This script defines a method to extract sender, receiver, and flags from log lines

def extract_info(line)
  sender = line.match(/\[from:(.+?)\]/)[1]
  receiver = line.match(/\[to:(.+?)\]/)[1]
  flags = line.match(/\[flags:(.+?)\]/)[1]
  [sender, receiver, flags]
end

File.foreach(ARGV[0]) do |line|
  if line.include?("Sent SMS") || line.include?("Receive SMS")
    sender, receiver, flags = extract_info(line)
    puts "#{sender},#{receiver},#{flags}"
  end
end
