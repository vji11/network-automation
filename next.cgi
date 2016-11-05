#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

device = form.getvalue('device')
image = form.getvalue('image')
os_size = form.getvalue('os_size')
md5_sum = form.getvalue('md5_sum')

print 'Content-type: text/html\r\n\r'
print '<html>' #start of html output

tftp_server = '10.65.18.99'
my_vrf = 'default'
cmd_dir = 'dir | i free'
import base64
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
    print "\nUpload Succesfull. " + "md5 " + md5_sum + " " + "checksum verified."
else:
    print "\nUpload Failed. " + "Original Checksum " + md5_sum + " " + "differ from calculated checksum"

print '</html>'	#end html page