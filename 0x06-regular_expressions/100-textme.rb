#!/usr/bin/env ruby
# This ruby script read each line from the log file provided as the first argument

File.foreach(ARGV[0]) do |line|

    sender = line.match(/\[from:(?<sender>[\w+\s]+)\]/)[:sender]
    receiver = line.match(/\[to:(?<receiver>[\+\d]+)\]/)[:receiver]
    flags = line.match(/\[flags:(?<flags>[\d\-\:]+)\]/)[:flags]

    puts "#{sender},#{receiver},#{flags}"
end
