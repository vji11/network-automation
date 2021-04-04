import time
import os
import re
import sys

tenant = "'openstack', "
app = "'ap_telesphorus', "
epg = "'epg_telesphorus_vmnet_am2_"
y1= "create_static_binding_vpc("
mode = "'regular', "
leaf1 = "'110', "
leaf2 = "'111', "
interface= "'vpc_ipg_44', "
status = "'created')"

for i in range(210,301):
    print (y1+tenant+app+epg+str(i))+"', "+"'"+str(i)+"', "+mode+leaf1+leaf2+interface+status