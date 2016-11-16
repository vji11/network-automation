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
	global main_menu_actions, hosts_file, commands_file, vlan_cfg
	hosts_file = arg['hosts']
	commands_file = arg['commands']
	vlan_cfg = ['configure terminal',
			    'vlan 3232',
			    'name vlan-name',
			    'exit']
	main_menu_actions = {
		'main_menu': main_menu,
		'1': sh_host_list,
		'2': sh_commands_list,
		'3': connect,
		'0': prog_exit}

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def press_return():
    print '\n\n(Make sure to resync the device to see any configuration changes)'
    print '\n\nPress enter to go back\n'
    raw_input(' >> ')


def sh_host_list():
    hosts = open(hosts_file, 'r')
    print '\n\n\tHosts in file: \n'
    for x in hosts:
        print '\t\t' + x.strip('\n')
    print '\n\n'
    hosts.close()
    press_return()
    main_menu()

def sh_commands_list():
	commands = open(commands_file, 'r')
	print '\n\n\tCommands in file: \n'
	for x in hosts:
		print '\t\t' + x.strip('\n')
	print '\n\n'
	commands.close()
	press_return()
	main_menu()

def main_menu():
    clear_screen()
    menu_actions = main_menu_actions
    menu_return = main_menu
    print '\n\n'
    print '\n\n\tPlease choose an option from the following:\n\n'
    print '\t\t1. Show IP addresses in list file\n'
    print '\t\t2. Show the commands to be pushed to the devices\n'
    print '\t\t3. Perform the configuration'
    print '\n\n\t\t0. Quit'
    choice = raw_input('\n\n >> ')
    exec_menu(menu_actions, menu_return, choice)
    return  

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