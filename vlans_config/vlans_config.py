#!/usr/bin/env python
import time
import os
import paramiko
import getpass



def args():
	parser = argparse.ArgumentParser(description='Python Program to configure Cisco switches.')
	parser.add_argument('-f', '--hosts', help='Specify a hosts file', required=True)
	arg = vars(parser.parse_args()) 
	hosts_file = arg['hosts']
	vlan_cfg = ['configure terminal',
			    'vlan 3232',
			    'name vlan-name',
			    'exit']
	global hosts_file, vlan_cfg

def creds():
	global myuser, mypass
	myuser = raw_input('Username: ')
	mypass = getpass.getpass('Password: ')

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def connect():
    creds()
    global remote_conn
    global host
    if os.path.isfile(hosts_file):
        myfile = open(hosts_file, 'r')
        for ip in myfile:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            remote_conn = ()
            ip = ip.strip('\n')
            host = ip
            print_host = host
            print_host = print_host.replace('\n', '')
            try:
                print '\n----- Connecting to %s -----\n' % print_host
                client.connect(host,
                               username=username,
                               password=password,
                               timeout=5)
                print '\t*** SSH session established with %s ***' % print_host
                remote_conn = client.invoke_shell()
                output = remote_conn.recv(1000)
                time.sleep(1)
                if '#' not in output:
                    remote_conn.send('en\n')
                    time.sleep(1)
                    print '\t*** Sending Enable Password ***'
                    remote_conn.send(en_password)
                    remote_conn.send('\n')
                    time.sleep(1)
                    output = remote_conn.recv(1000)
                if '#' in output:
                    print '\t*** Successfully Entered Enable Mode ***'
                    remote_conn.send('terminal length 0\n')
                    time.sleep(1)
                    get_int_and_cdp()
                else:
                    print '\t*** Incorrect Enable Password ***'
            except paramiko.SSHException:
                print '\t*** Authentication Failed ***'
            except socket.error:
                print '\t*** %s is Unreachable ***' % host
            client.close()

def test_cmds():
	for cmds in vlan_cfg:
		print '\t' + cmds

def main():
	print 'Program starting...\n'
	time.sleep(0)
	test_cmds()

if __name__ == '__main__':
	clear_screen()
	main()