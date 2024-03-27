#!/usr/bin/env bash
# Define a class for Nginx configuration
class alx_nginx {

  # Install Nginx package based on OS family
  if ($operatingsystem =~ /(Debian|Ubuntu)/) {
    package { 'nginx': ensure => 'present' }
  } else {
    package { 'nginx': ensure => 'present' }  # Replace with RedHat package name if needed
  }

  # Manage Nginx service
  service { 'nginx':
    ensure => running,
    enable => true,
  }

  # Define root directory for website content
  $document_root = '/var/www/html'

  # Create the directory with proper permissions
  file { $document_root:
    ensure => directory,
    owner => 'www-data',
    group => 'www-data',
    mode => '0755',
  }

  # Create a simple index.html file
  file { $document_root + '/index.html':
    ensure => present,
    content => '<!DOCTYPE html><html><body>Hello World!</body></html>',
    owner => 'www-data',
    group => 'www-data',
    mode => '0644',
  }

  # Configure Nginx server block
  nginx::site { 'default':
    ensure => present,
    port => 80,
    server_name => '$::server_name',  # Replace with actual server name if needed
    root => $document_root,
  }

  # Configure 301 redirect for /redirect_me
  nginx::resource { 'redirect_rule':
    location => '/redirect_me',
    code => 301,
    uri => '/',
  }
}
