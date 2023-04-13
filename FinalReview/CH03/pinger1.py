#!/usr/bin/env python3
# First example for he pingin
# by Enea

import platform
import os
# ---------------------------------------------------------
#aasign Ip to ping to a variable
# ip = "127.0.0.1"
# ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
# exit_code = os.system(ping_cmd)
# print(exit_code)
# ---------------------------------------------------------
# ---------------------------------------------------------
# ip= "127.0.0.1"
# current_os=platform.system().lower()

# if current_os =="windows":
#     ping_cmd=f"ping -n 1 -w 2 {ip} > null"
# else:
#     ping_cmd=f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

# exit_code = os.system(ping_cmd)

# print(exit_code)

# ---------------------------------------------------------
def ping_host(ip):
    current_os=platform.system().lower()

    if current_os =="windows":
        ping_cmd=f"ping -n 1 -w 2 {ip} > null"
    else:
        ping_cmd=f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    exit_code = os.system(ping_cmd)

    return exit_code

ip_prefix = "10.1.0."

for final_octet in range(150):
    ip = ip_prefix + str(final_octet +1)
    
    exit_code= ping_host(ip)
    
if exit_code ==0:
    print("{0} is online".format(ip))
# -------------------------------------------------------

