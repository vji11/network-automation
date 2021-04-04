t1 = "create_static_binding_int('LAB', 'LAB-AP', 'LAB-"
p10143 = "'regular', '101', '43', 'created')"
p10144 = "'regular', '101', '44', 'created')"
p10145 = "'regular', '101', '45', 'created')"
p10243 = "'regular', '102', '43', 'created')"
p10244 = "'regular', '102', '44', 'created')"
p10245 = "'regular', '102', '45', 'created')"
#EPG range 2000-2254
for i in range(2000, 2255): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10143) 
for i in range(2000, 2255):
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10144) 
for i in range(2000, 2255): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10145)
for i in range(2000, 2255): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10243) 
for i in range(2000, 2255): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10244) 
for i in range(2000, 2255): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10245)    
#EPG range 3000-3255
for i in range(3000, 3256): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10143) 
for i in range(3000, 3256): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10144) 
for i in range(3000, 3256): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10145)   
for i in range(3000, 3256): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10243) 
for i in range(3000, 3256): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10244) 
for i in range(3000, 3256): 
   print str(t1) + str(i) + "-EPG', '" + str(i) + "', " + str(p10245) 
