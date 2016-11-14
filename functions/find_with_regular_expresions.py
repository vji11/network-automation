#!/usr/bin/env python

'''
find with regular expresion
. (dot) anu char
\w word char
\d digit
\s whitespace
+ 1 or more
* 0 or more
before pattern field put r so python will ignore the code from interpreting
'''
import time
import os
import re

def Find(pattern, text):
	match = re.search(pattern, text)
  	if match:
  		print match.group() + '\n'
  	else:
  		print 'Pattern not found in text'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
	print 'programul ruleaza un joint...\n'
  	time.sleep(3)
	Find(r'0/1\.', 'GigabitEthernet0/1.vlan-id')

if __name__ == '__main__':
	clear_screen()
	main()	