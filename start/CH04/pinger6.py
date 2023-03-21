#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By Enea Paja

import platform
import os
from datetime import datetime


def write_log(message):
    now=str(datetime.now()) + "\t"
    message = now + str(message) +"\n"
    f = open("pinger.log", "a")
    f.write(message)
    f.close()

def ping_host(ip):
    
    ping_cmd = f"ping -n 1 -w 2 {ip} > /dev/null 2>&1"

    return ping_cmd

def import_addresses():
    # Create empty list object
    lines =[]
    # Open file and read line by line
    f=open("ips.txt", "r")

    for line in f:
        # User strip() to remove spaces and carriage return
        line = line.strip()
        # Add the line to the lines list obj
        lines.append(line)

        # Return the list obj to the main body
    return lines

    #Read IPS from file

write_log("Reading IPs from ips.txt")
ip_addreses=import_addresses()
write_log("Imported {0} IPs".format(len(ip_addreses)))

for ip in ip_addreses:
    #Call ping_host function and capture the return value
    ping_cmd = ping_host(ip)

    #Print results to onsole only if successful
    if ping_cmd==0:
        write_log("{0} is online".format(ip))
        print("{0} is online".format(ip))
    else:
        write_log("{0} is offline ".format(ip))    
    