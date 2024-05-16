# Puppet manifest to fix the web server setup featuring Nginx
# Manifest file: 0-the_sky_is_the_limit_not.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
}

# Configure Nginx to handle more concurrent connections
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "worker_processes auto;\n",
  notify  => Service['nginx'],
}

# Restart Nginx service if configuration changes
exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,
}

# Ensure the web server can handle the ApacheBench load test
# by adjusting the worker_processes and worker_connections settings
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "worker_processes auto;\nworker_connections 1024;\n",
  notify  => Exec['restart_nginx'],
}

