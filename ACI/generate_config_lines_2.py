#!/usr/bin/python

import re

file = "devices.txt"

fvTenant = raw_input('TENANT: ')
fvAP = raw_input('APPLICATION PROFILE: ')
fvAEG = raw_input('EPG: ')
vlan = raw_input('VLAN: ')
mode = raw_input('regular (= trunk), native (= Access 802.1p), untagged (= Access untagged) : ')
nodeid_1 = raw_input('LEAF1: ')
nodeid_2 = raw_input('LEAF2: ')
status = raw_input('created, modified, deleted :' )


def generate_static_bindings_vpc():
	hosts = open(file, 'r')
	for x in hosts:
		print("create_static_binding_vpc(" + "'%s', " %fvTenant + "'%s', " %fvAP + "'%s', " %fvAEG + "'%s', " %vlan + "'%s', " %mode + "'%s', " %nodeid_1 + "'%s', " %nodeid_2 + "'" + (x.strip()) + "_INT_POLGRP', " + "'%s')" %status)
	print ('\n')
	hosts.close()

if __name__ == '__main__':
	generate_static_bindings_vpc()	