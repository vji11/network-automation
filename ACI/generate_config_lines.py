#!/usr/bin/python

import time
import os
import re
import sys

'''variable create interface policy group'''
domain = "'AEP_BAREMETAL', "
speed = "'10G_AUTO_ON', "
cdp = "'CDP_DISABLED', "
lldp = "'LLDP_ENABLED', "
lacp = "'LACP_ACTIVE'"
y1 = "create_interface_policy_group_vpc("
z1 = ", " + domain + speed + cdp + lldp + lacp + ")"

'''variables create interface switch profile'''
leaf1 = "'211', "
leaf2 = "'212', "
port1 = "'', " 
port2 = "'',"
y2 = "create_interface_switch_profile("
z2 = ", " +  leaf1 + leaf2 + port1 + port2 + ")"

'''variables create static bindings vpc'''
tenant = "'TN_LG_PROD', "
app_profile = "'APP_FND_BACKUP_01', "
epg = "'EPG_FND_BACKUP_01', "
mode =  "'untagged', "
vlan =  "'3283', "
primary_encap = "'3284', "
y3 = "create_static_binding_vpc(" + tenant + app_profile + epg + vlan + primary_encap + mode + leaf1 + leaf2

def gen1():
	hosts = open("devices.txt", 'r')
	for x in hosts:
		print (y1 + "'" + (x.strip()) + "'" + z1)
	print ('\n')
	hosts.close()

def gen2():
        hosts = open("devices.txt", 'r')
        for x in hosts:
                print (y2 + "'" + (x.strip()) + "'" + z2)
        print ('\n')
        hosts.close()

def gen3():
    hosts = open("devices.txt", 'r')
    for x in hosts:
        print (y3 + "'" + (x.strip()) + "_INT_POLGRP', " + "'created')")
    print ('\n')
    hosts.close()

if __name__ == '__main__':
    gen1()
    gen2()
    gen3()