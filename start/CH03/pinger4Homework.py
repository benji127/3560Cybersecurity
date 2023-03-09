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

start_ip = input("What is the IP address of the host you want to ping? ")
octets = start_ip.split(".")
last_octet = int(octets[3])

prefix =octets[0]+"."+octets[1]+"."+octets[2]+"."
ip_range = input("What is the range of IP addresses you want to ping? ")
#this is ip
new_last_octet = last_octet + int(ip_range)




print(new_last_octet)
print(f"This is the IP address of the host: {last_octet}")
#new_ip_address = f"{octets[0]}.{octets[1]}.{octets[2]}.{new_last_octet}"
#print(new_ip_address)
#Loop from 0-254
for final_octet in range(last_octet,new_last_octet):
    #assign ip address
    #adding 1 to the final octet

    if(final_octet > 255):
        print(f"You cannot ping more than 255 IP addresses in a single ping")
        exit(1)

    ip = f"{prefix}{final_octet}"
    
    print(f"This is the IP address of the host: {ip}")
    #call ping_host function and capture the return value.

    exit_code = ping_host(ip)


    #print results to console only if successful

    if exit_code == 0:
        print("{0} is online.".format(ip))
