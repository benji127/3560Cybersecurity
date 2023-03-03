#!/usr/bin/env python3
# Second example of pinging from Python
# By Enea Paja
# 03/03/2023

#import necessary libraries
import platform
import os

#Assign IP address to variable
ip = "127.0.0.1"

#determine the current operating system

current_os = platform.system().lower()

if current_os == "windows":
    #build ping command windows
    ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
elif current_os == "linux":
    ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

exit_code = os.system(ping_cmd)

print(exit_code)
   
