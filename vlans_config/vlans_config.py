#!/usr/bin/env python
import time
import os
import paramiko
import getpass

commands_file = open("commands.txt", "r")
device_file = open("hosts.txt", "r")


vlan_cfg = ['configure terminal',
			'vlan 3232',
			'name vlan-name',
            'exit']

def creds():
	global myuser, mypass
	myuser = raw_input('Username: ')
	mypass = getpass.getpass('Password: ')

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def configure():
	for cmds in vlan_cfg:
		print '\t*** Sending: ' + cmds + ' ***'






















def main():
	print 'Program starting...\n'
	time.sleep(0)
	configure()

if __name__ == '__main__':
	clear_screen()
	main()