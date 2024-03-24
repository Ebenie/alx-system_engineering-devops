#!/usr/bin/env bash
# This Puppet manifest configures the SSH client to meet the requirements by ensuring that password authentication is disabled and specifying the private key ~/.ssh/school for authentication.

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

