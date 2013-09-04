#!/usr/bin/python 
# -*- coding: utf-8 -*-
import os
import glob
import time
import sys

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def read_temp_raw(id):
    f = open('/sys/bus/w1/devices/'+id+'/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(id):
    lines = read_temp_raw(id)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c #, temp_f

if (len(sys.argv) == 2):
	#print sys.argv[1]
	print(str(read_temp(sys.argv[1])))
else:
	print(str(read_temp('28-00000433c406'))+" "+str(read_temp('28-00000433b514')))

