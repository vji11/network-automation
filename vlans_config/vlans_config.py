#!/usr/bin/env python
import time
import os
import paramiko
import getpass

commands = open('commands.txt', 'r')
device = open('hosts.txt', 'r')
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

def config_vlans():
	cmd = commands
	ssh_connect(cmd)
	print '\n##### Device Output Start #####'
	print '\n'.join(output)
	print '\n##### Device Output End #####'	


#main program
def main():
	print 'Program starting...\n'
	time.sleep(1)
	variables1()
	config_vlans()

#run main program in main file
if __name__ == '__main__':
	clear_screen()
	main()
#end







