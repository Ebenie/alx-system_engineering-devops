# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define the custom HTML content for the root
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Configure a 301 redirect for /redirect_me
nginx::resource::vhost { 'redirect_me':
  www_root       => '/var/www/html',
  ensure         => present,
  listen_options => 'default_server',
  redirect       => 'https://www.example.com',
  ssl            => false,
}

