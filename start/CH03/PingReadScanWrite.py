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

#Function for writing the optput to another file
def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    f = open("ImportedIPAndScan.log", "a")
    f.write(message)
    f.close()

def import_addresses():
    # Create empty list object
    lines = []
    # Open file and read line-by-line
    f = open("../CH04/homeips.txt", "r")
    for line in f:
        # Use strip() to remove spaces and carriage returns
        line = line.strip()
        # Add the line to the lines list object
        lines.append(line)
    # Return the list object to the main body
    return lines

#validate octets not bigger than 255
def check_int_octets(ip):
    octets = ip.split(".")

    for octet in octets:
        if int(octet) > 255:
            print("Invalid IP address")
            break
    else:
        print("Valid IP address")        

# read IPs from file
ip_addresses = import_addresses()

#Loop from 0-254
for ip in ip_addresses:
    #assign ip address

    #Call Validate IP octets function
    check_int_octets(ip)

    # Scan ports
    port_start = 20
    port_end = 25

    # Create the scanner object
    scanner = nmap.PortScanner()

    # ip = f"{prefix}{final_octet}"
    print(f"This is the IP address of the host: {ip}")
    

    #call ping_host function and capture the return value.
    exit_code = ping_host(ip)
    write_log("Scanning {0}".format(ip))
    print("Scanning {0}".format(ip))
    

    #print results to console only if successful
    if exit_code == 0:
        write_log("{0} is online.".format(ip))
        print("{0} is online.".format(ip))
        # Loop through each port and scan
        for port in range(port_start, port_end):
            result = scanner.scan(ip, str(port))
            port_status = result['scan'][ip]['tcp'][port]['state']
            write_log("\tPort: {0} is {1}".format(port, port_status))
            print("\tPort: {0} is {1}".format(port, port_status))

        
