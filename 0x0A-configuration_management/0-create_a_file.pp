# create a file in /tmp with owner, group, and mode.

file { '/tmp/school':
ensure  => file,t
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}