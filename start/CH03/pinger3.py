#!/usr/bin/env python3
# Third example of pinging from Python
# By Enea Paja
#03/06/2023

#import neccessary Python modules.

import platform
import os

#define the prefix to begin pinging. 
ip_prefix = "10.1.51."
#Determinf the os
current_os = platform.system().lower()

#loop from 0 to 254 
for final_octet in range(12,23):
    #assign IP to ping to a variable
    #adding 1 to final_octet because loop starts at 0
    ip = ip_prefix + str(final_octet)
    print(f"this is pinging {ip} from {current_os}")
    
    if current_os == "Windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    #Excecute the ping command and capture exit code
    exit_code = os.system(ping_cmd)
    #print the exit code
    print("{0} is online".format(ip))











