#!/usr/bin/env bash
# Define package and service for Nginx
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  require   => Package['nginx'],
}

# Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80;
    server_name _;

    location / {
        return 200 'Hello World!\n';
    }

    location /redirect_me {
        return 301 http://\$host/new_location;
    }

    location = /new_location {
        return 200 'Redirected\n';
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
