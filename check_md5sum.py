#!/usr/bin/python
import paramiko
import base64

b64pass = base64.b64decode("Y2ljaTE=")
b64usr = base64.b64decode("dmppZWFudQ==")
image = 'test.txt'
device = raw_input('Device to upgrade: ')
md5_sum = raw_input('MD5 Checksum of the image: ')
md5_check = "show file " + image + " " + "md5sum"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(device, port=22, username=b64usr, password=b64pass)
stdin, stdout, stder = ssh.exec_command(md5_check)
output2 = stdout.readlines()
ssh.close()

if any(md5_sum in s for s in output2):
	print "ok - checksum verified"
else:
	print "not ok - upload failed - checksum error"