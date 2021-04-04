#!/usr/bin/python

import re
import os

file = "patch.csv"
int_type = "Management"
leaf_pattern = "nl-srk03a-sl"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def jeg():
	openfile = open(file, "r")
	data = openfile.readlines()
	for line in data:
		line = line.strip()
		if re.search(leaf_pattern and int_type, line):
			print line

if __name__ == '__main__':
	clear_screen()
	jeg()	