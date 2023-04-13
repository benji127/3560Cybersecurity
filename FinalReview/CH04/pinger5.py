#!/usr/bin/env python3
# Fifthe example of pinging from python
# Reading IPs from a file 

import platform
import os
def ping_host(ip):
    current_os = platform.system().lower()
    if current_os =="windows":
        ping_cmd=f"ping -n -1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c -1 -w 2 {ip} > /dev/null 2>&1"
    exit_code =- os.system(ping_cmd)
    return exit_code

def import_addresses():
    lines=[]
    f=open("myips.txt", "r")
    
    for line in f:
        line = line.strip()
        lines.append(line)
    return lines

ip_addresses = import_addresses()

for ip in ip_addresses:
    exit_code = ping_host(ip)
    
    if exit_code ==0:
        print("{0} is online".format(ip))
    