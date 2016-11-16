#!/usr/bin/env python
import time
import os
import paramiko
import getpass

tacacs = '.tacacslogin'
commands = 'commands.txt'
hostsfile = 'hosts.txt'
devicetype = "ios"
verbose = "yes"

# Variables
def variables1():
	global myuser, mypass
	myuser = raw_input('Username: ')
	mypass = getpass.getpass('Password: ')

# Define clear-screen function
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


def ssh_connect(commands):
	global output
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(device, port=22, username=myuser, password=mypass)
	ssh.exec_command('terminal length 0\n')
	stdin, stdout, stder = ssh.exec_command(commands)
	output = stdout.readlines()
	print '\n'.join(output)
	ssh.close()








