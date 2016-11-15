#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

def variables1():
    global device, my_vrf, ftp_server, image, os_size, md5_sum, myuser, mypass
    device = form.getvalue('device')
    image = form.getvalue('image')
    os_size = form.getvalue('os_size')
    md5_sum = form.getvalue('md5_sum')
    tftp_server = form.getvalue('tftp_server')
    my_vrf = form.getvalue('my_vrf')
    myuser = form.getvalue('myuser')
    mypass = form.getvalue('mypass')

print 'Content-type: text/html\r\n\r'
print '<html>' #start of html output

#program start


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
	cmd_upload = "copy ftp://"  + tftp_server + "/" + image + " " + "bootflash:" + " vrf " + my_vrf
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
	variables1()
	check_if_file_present()
	check_if_enough_space()
	upload_file()
	check_file_md5sum()

#run main program in main file
if __name__ == '__main__':
	main()
#end
 
print '</html>'	#end html page