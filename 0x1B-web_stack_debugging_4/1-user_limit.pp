# Puppet manifest to change OS configuration for the holberton user

# Increase the maximum number of open files for the holberton user
user { 'holberton':
  max_files => '65536',
}

