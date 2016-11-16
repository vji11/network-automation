#!/usr/bin/env python
import time
import os
import paramiko
import getpass

commands_file = open("commands.txt", "r")
device_file = open("hosts.txt", "r")


def creds():
	global myuser, mypass
	myuser = raw_input('Username: ')
	mypass = getpass.getpass('Password: ')

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def pf():
	with open("commands.txt", "r") as f:
		text = f.readlines()
		for line in text:
			print line
	f.close()

def main():
	print 'Program starting...\n'
	time.sleep(0)
	pf()

if __name__ == '__main__':
	clear_screen()
	main()