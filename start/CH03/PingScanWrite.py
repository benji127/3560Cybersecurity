#!/usr/bin/env python3
# Fourth example of pinging from Python
# By  Enea Paja
# 05/03/2023


#import necessary python modules\


import platform
import os
import nmap
from datetime import datetime


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

def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    f = open("PingAndScan.log", "a")
    f.write(message)
    f.close()

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

    # Scan ports
    port_start = 20
    port_end = 25

    # Create the scanner object
    scanner = nmap.PortScanner()

    target_address = f"{prefix}{final_octet}"

    if(final_octet > 255):
        print(f"You cannot ping more than 255 IP addresses in a single ping")
        exit(1)

    # ip = f"{prefix}{final_octet}"
    
    print(f"This is the IP address of the host: {target_address}")
    #call ping_host function and capture the return value.

    exit_code = ping_host(target_address)


    #print results to console only if successful

    if exit_code == 0:
        write_log("{0} is online.".format(target_address))
        print("{0} is online.".format(target_address))


        write_log("Scanning {0}".format(target_address))
        print("Scanning {0}".format(target_address))
        # Loop through each port and scan
        for port in range(port_start, port_end):
            result = scanner.scan(target_address, str(port))
            port_status = result['scan'][target_address]['tcp'][port]['state']
            write_log("\tPort: {0} is {1}".format(port, port_status))
            print("\tPort: {0} is {1}".format(port, port_status))
