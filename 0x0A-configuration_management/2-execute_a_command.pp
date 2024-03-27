# Define an exec resource to kill the process named "killmenow"
exec { 'pkill':
  command => 'pkill killmenow',

}

