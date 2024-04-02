#!/usr/bin/env bash
# Define a class for configuring custom HTTP header
class custom_http_response_header {


  $hostname = $facts['networking']['hostname']

  
  package { 'augeas-tools':
    ensure => installed,
  }

  # Manage NGINX service
  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'], 
  }


  augeas { 'custom_http_header':
    context => "/files/etc/nginx/sites-available/default",
    changes => [
      "set server//add_header X-Served-By '$hostname'",
    ],
    require => Package['augeas-tools'],
    notify  => Service['nginx'],
  }
}

include custom_http_response_header


