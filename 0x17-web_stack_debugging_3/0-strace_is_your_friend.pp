# Puppet manifest to fix Apache 500 error

# Define an exec resource to restart Apache
exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
}

