#!/usr/bin/env python
import time
import os
import paramiko
import getpass

#variables
def variables1():
	global device, my_vrf, tftp_server, image, os_size, md5_sum, myuser, mypass
	device = raw_input('Device to upgrade: ')
	my_vrf = raw_input('VRF: ')
	tftp_server = raw_input('TFTP Server: ')
	image = raw_input('Name of the NX-OS file: ')
	os_size = int(raw_input('Size in bytes of the NX-OS image: '))
	md5_sum = raw_input('MD5 Checksum of the image: ')
	myuser = raw_input('Username: ')
	mypass = getpass.getpass('Password: ')
	
#define clear-screen function
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

#define ssh connection function
def ssh_connect_no_shell(command):
	global output
	ssh_no_shell = paramiko.SSHClient()
	ssh_no_shell.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_no_shell.connect(device, port=22, username=myuser, password=mypass)
	ssh_no_shell.exec_command('terminal length 0\n')
	stdin, stdout, stder = ssh_no_shell.exec_command(command)
	output = stdout.readlines()
	ssh_no_shell.close()

#check if file is already on the flash
def check_if_file_present():
	ssh_connect_no_shell('dir | include ' + image)
	if any(image in s for s in output):
		print '\nThe file you are trying to upload is already there.'
		print '\nProgram will exit now...'
		exit()
	else:
		time.sleep(1)

#check if there is enough disk space
def check_if_enough_space():
	ssh_connect_no_shell('dir | include free')
	for line in output:
		if 'bytes' in line:
			bytes_count = int(line.split()[0].strip('('))
	if os_size < bytes_count:
		print "\nUpgrade can continue. There is enough space free on the disk."
	else:
		print "\nUpgrade cannot continue due not enough space on the flash."
		exit()

#perform the file upload
def upload_file():
	cmd_upload = "copy tftp:" + "//" + tftp_server + "/" + image + " " + "bootflash:" + " vrf " + my_vrf
	ssh_connect_no_shell(cmd_upload)
	print '\n##### Device Output Start #####'
	print '\n'.join(output)
	print '\n##### Device Output End #####'

#check if the file upload was succefull
def check_file_md5sum():
	cmd_md5_check = "show file " + image + " " + "md5sum"
	ssh_connect_no_shell(cmd_md5_check)
	if any(md5_sum in s for s in output):
		print "\nUpload Succesfull. " + "md5 " + md5_sum + " " + "checksum verified."
	else:
		print "\nUpload Failed. " + "Original Checksum " + md5_sum + " " + "differ from calculated checksum"

#main program
def main():
	print 'Program starting...\n'
	time.sleep(1)
	variables1()
	check_if_file_present()
	check_if_enough_space()
	upload_file()
	check_file_md5sum()

#run main program in main file
if __name__ == '__main__':
	clear_screen()
	main()
#end