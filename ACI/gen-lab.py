import time
import os
import re
import sys

y1= "create_static_binding_int("
tenant = "'LAB', "
app = "'LAB-AP', "
epgstart = "'LAB-"
epgend = "-EPG', '"
mode = "'regular', '"
status = "'created')"

#generate script output for EPG 2000-2254
def epg2k():
#EPG range 2000-2254 and vlan range
    for i in range(2000,2255):
        #port range 43-45
        for j in range(43,46):
            #leaf range 101-102
            for k in range(101,103):
                print (y1 + tenant + app + epgstart + str(i)) + epgend + str(i) + "', " + mode + str(k) + "', '" + str(j) + "', " + status
                
#generate script output for EPG 3000-3255
def epg3k():
#EPG range 3000-3255 and vlan range
    for i in range(3000,3256):
        #port range 43-45
        for j in range(43,46):
            #leaf range 101-102
            for k in range(101,103):
                print (y1 + tenant + app + epgstart + str(i)) + epgend + str(i) + "', " + mode + str(k) + "', '" + str(j) + "', " + status
        
if __name__ == '__main__':
    epg2k()
    epg3k()