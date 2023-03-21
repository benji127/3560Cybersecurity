#!/usr/bin/env python3
# Port scanner example 
# Use 'pip3 install python-nmap' to install modules
# Use 'sudo apt -y install nmap' to install nmap
# By Enea Paja
# 2/27/2021

# import necessary Python modules
import nmap

# Identify target address
target_address = "10.0.2.15"

# Identify start and stop port for the scan
port_start = 20
port_end = 30

# Create the scanner object
scanner = nmap.PortScanner()

print("Scanning {0}".format(target_address))
# Loop through each port and scan
for port in range(port_start, port_end):
    result = scanner.scan(target_address, str(port))
    port_status = result['scan'][target_address]['tcp'][port]['state']
    print("\tPort: {0} is {1}".format(port, port_status))

