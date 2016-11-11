import os
import argparse
import paramiko
import getpass
import socket
import re
import sys
import time

# Get command line arguments, set global variables, and define supportive functions
# Define command line arguments and globals

def args():
    parser = argparse.ArgumentParser(description='Python Script to upgrade NX-OS Images on Cisco Nexus Devices.')
    parser.add_argument('-f', '--hosts',
                        help='Specify a hosts file',
                        required=True)
    arg = vars(parser.parse_args())

    parser.add_argument('-a', '--image',
                        help='Enter .bin image name -- '
                             '(default = 1)',
                        default='1')

    global main_menu_actions, sub_menu_actions, config_menu_actions, hosts_file, \
        network_devices, starts_items, image_file
    network_devices = {}
    hosts_file = arg['hosts']
    
    main_menu_actions = {
        'main_menu': main_menu,
        '1': sh_host_list,
        '2': select_image,
        '3': connect,
        '0': prog_exit}

    sub_menu_actions = {
        'cmd_outputs': sh_cmd_outputs,
        '1': upgrade_os,
        '2': check_md5,
        '9': main_menu}   

    
    cmd_upgrade_os = ['install all nxos bootflash: %s' % image_file]
    cmd_check_md5 = "show file " + image_file + " " + "md5sum" 
                           

###################################################################################################################
# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu choice validator
def exec_menu(menu_actions, menu_return, choice):
    clear_screen()
    try:
        menu_actions[choice]()
    except KeyError:
        print 'Invalid Selection, Please Try Again.\n'
        time.sleep(3)
        menu_return()

# Printed main menu
def main_menu():
    clear_screen()
    menu_actions = main_menu_actions
    menu_return = main_menu
    print '\n\n'
    print '\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    print '\t*                                                           *'
    print '\t*         DMC Network Device OS Upgrade                     *'
    print '\t*         version: beta 0.1                                 *'
    print '\t*  Please use with care. Always double check in device CLI  *'
    print '\t*  to validate the conformity of the operations.            *'
    print '\t*                     Program Development: Valentin Jieanu  *'
    print '\t*                                                           *'
    print '\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    print '\n\n\tPlease choose an option from the following:\n\n'
    print '\t\t1. Show the hosts file\n'
    print '\t\t2. Show the image .bin \n'
    print '\t\t3. Perform OS upgrade\n'
    print '\n\n\t\t0. Quit'
    choice = raw_input('\n\n >> ')
    exec_menu(menu_actions, menu_return, choice)
    return

# Get username and passwords

def creds():
    global username, password, en_password
    print '\n\n'
    print '\n\n Please enter username, password, and enable password:\n'
    print '\t(Note that Enable Password may be not required if your username have ' \
          'privilege level15. In this case just type anything as the value will be ignored.)\n\n'
    username = raw_input(' Enter Username: ')
    password = getpass.getpass(' Enter Password: ')
    en_password = getpass.getpass(' Enter Enable Password: ')
