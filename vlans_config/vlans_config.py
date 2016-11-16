#!/usr/bin/env python
import os
import argparse
import paramiko
import getpass
import socket
import re
import sys
import time

def args():
	parser = argparse.ArgumentParser(description='Python Program to configure Cisco switches. Use with care.')
	parser.add_argument('--hosts', help='Specify a hosts file', required=True)
	parser.add_argument('--commands', help='Specify a commands file', required=True)
	arg = vars(parser.parse_args())
	global hosts_file, commands_file, vlan_cfg
	hosts_file = arg['hosts']
	commands_file = arg['commands']
	vlan_cfg = ['configure terminal',
			    'vlan 3232',
			    'name vlan-name',
			    'exit']

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def creds():
	global myuser, mypass
	myuser = raw_input('Username: ')
	mypass = getpass.getpass('Password: ')

def test_cmds():
	for cmds in vlan_cfg:
		print '\t' + cmds

def main():
	print 'Program starting...\n'
	time.sleep(0)
	test_cmds()

if __name__ == '__main__':
	args()
	main()