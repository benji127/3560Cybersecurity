#!/usr/bin/env python3

import sys
import math

def ip_str_to_num(ip_str):
    ip_num = 0
    octet = ip_str.split(".")
    for pow in range(3, -1, -1):
        ip_num += int(octet[3-pow]) * 256 ** pow
    return ip_num

def num_to_ip_str(ip_num):
    octet = []
    num = ip_num
    for pow in range(3, -1, -1):
        octet_num = math.floor(num / 256 ** pow)
        octet.append(str(octet_num))
        num = num - octet_num * 256 ** pow
    return ".".join(octet)

##################
### start here ###
##################
#
# usage:
# ./cidr.py [ <in_filename> [<out_filename>] ]
# 
# where in_filename default to be cidr.txt
#       with lines of x.x.x.x/n in the file
#
# output:
# network address, subnet mask, first host ip, last host ip,
# and ordinal number (n-th) of the CIDR formatted IP is positioned
# within this subnet.
#
# results are written to stdout if out_filename is absent
# otherwise, write to file named "out_filename"
# (note: not append)
#
# example:
# ./cidr.py
#    file cidr.txt will be read and the result will be shown on screen
# ./cidr.py haha.txt
#    file haha.txt will be read and the result will be shown on screen
# ./cidr.py haha.txt hoho.txt
#    file haha.txt will be read and the result will be written to file hoho.txt
#

in_filename = "cidr.txt" # default filename
if len(sys.argv) > 1:
    in_filename = sys.argv[1]

out_file = sys.stdout # default output
if len(sys.argv) > 2:
    out_file = open(sys.argv[2], "w")

in_file = open(in_filename, "r")

for line in in_file:
    cidr_addr = line.strip().split("/")
    ip_num = ip_str_to_num(cidr_addr[0])
    cidr_num = int(cidr_addr[1])
    
    subnet_num = 0
    for i in range(cidr_num, 0, -1):
        subnet_num = (subnet_num >> 1) + 2 ** 31

    ######
    ### relationship between those numbers ###
    ######
    network_num = ip_num & subnet_num
    broadcast_num = network_num | (2 ** 32 - 1 - subnet_num)
    first_host_num = network_num + 1
    last_host_num = broadcast_num - 1
    nth_host = ip_num - first_host_num + 1

    ######
    ### different str formatting
    ######
    print(line.strip(), ":", file=out_file)
    print("Network address: {0}".format(num_to_ip_str(network_num)), file=out_file)
    print(f"Subnet mask: {num_to_ip_str(subnet_num)}", file=out_file)
    print("Broadcast address:", num_to_ip_str(broadcast_num), file=out_file)
    print("First host ip in subnet: %s" % num_to_ip_str(first_host_num), file=out_file)
    print("Last host ip in subnet: %s" % num_to_ip_str(last_host_num), file=out_file)
    print(f"{cidr_addr[0]} is the #{nth_host} host within this network", file=out_file)
    print("", file=out_file)

in_file.close()
if out_file != sys.stdout:
    out_file.close()

