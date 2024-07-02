# make changes to config file using puppet

$content = 'Host alx-1
	HostName 54.160.117.191
	User ubuntu
	IdentityFile ~/.ssh/school
	PasswordAuthentication no'

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => $content,
}
