#!/usr/bin/puppet
# Install Flask version 2.1.0 using pip package manager

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

