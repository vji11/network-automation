#!/usr/bin/python
import base64

tftp_server = '10.65.18.99'
my_vrf = 'default'
cmd_dir = 'dir | i free'
device = raw_input('Device to upgrade: ')
image = raw_input('Name of the NX-OS file: ')
os_size = int(raw_input('Size in bytes of the NX-OS image: '))
md5_sum = raw_input('MD5 Checksum of the image: ')
b64pass = base64.b64decode("Y2ljaTE=")
b64usr = base64.b64decode("dmppZWFudQ==")
cmd_up = 'copy tftp:'
cmd_1 = cmd_up + "//" + tftp_server + "/" + image + " " + "bootflash:" + " vrf " + my_vrf
md5_check = "show file " + image + " " + "md5sum"  

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(device, port=22, username=b64usr, password=b64pass)
stdin, stdout, stder = ssh.exec_command(cmd_dir)
output = stdout.readlines()
#print '\n'.join(output)
ssh.close()

for line in output:
    if 'bytes' in line:
        bytes_count = int(line.split()[0].strip('('))

try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

print "Are you sure? (y/n)"
while True:
    char = getch()
    if char.lower() == "y":
        print char
        #check disk-space and perform upgrade
        if os_size < bytes_count:
            print "Performing upgrade..."
            ssh.connect(device, port=22, username=b64usr, password=b64pass)
            stdin, stdout, stder = ssh.exec_command(cmd_1)
            output1 = stdout.readlines()
            print '\n'.join(output1)
            ssh.close()         
        else:
            print "Upgrade cannot continue due not enough space on the flash"
    else:
    	print "Program End"
    	break

#Verifify the MD5 checksum
ssh.connect(device, port=22, username=b64usr, password=b64pass)
stdin, stdout, stder = ssh.exec_command(md5_check)
output2 = stdout.readlines()
ssh.close()

if any(md5_sum in s for s in output2):
    print "md5 " + md5_sum + " " + "checksum verified. Upload Succesfull."
else:
    print "Upload Failed. Original Checksum " + md5_sum + " " + "differ from calculated checksum"
