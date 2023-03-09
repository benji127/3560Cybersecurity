#!/usr/bin/env python3
# Fourth example of pinging from Python
# By  Enea Paja
# 05/03/2023


#import necessary python modules\


import platform
import os

def ping_host(ip):
    #Determind the current os
    current_os = platform.system().lower()

    if current_os == "windows":
        #build ping command
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    #Excecute command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code

ip_prefix = "10.1.51."

#Loop from 0-254
for final_octet in range(254):
    #assign ip address
    #adding 1 to the final octet
    ip = ip_prefix + str(final_octet + 1)
    #call ping_host function and capture the return value.

    exit_code = ping_host(ip)


    #print results to console only if successful

    if exit_code == 0:
        print("{0} is online.".format(ip))



