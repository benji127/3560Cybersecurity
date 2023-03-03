#!/usr/bin/env python3
# First example of pinging from Python
# By 
#import necessa

import platform
import os
print(platform.system())


#Assign IP to ping to a variable
ip ="127.0.0.1"
#build the ping command
ping_command = f"ping -c 1 -w 2 {ip} >/dev/null 2>&1"
#wxecute xommand and capture exor xode
exit_code = os.system(ping_command)
#print the exit code
print(exit_code)

if exit_code == 0:
    print(f"{ip} is reachable")
else:
    print(f"{ip} is unreachable")   


