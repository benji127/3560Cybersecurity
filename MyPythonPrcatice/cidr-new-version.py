#!/usr/bin/env python3

import sys

def ip_str_to_num(ip_str):
    """
    # method 1
    ip_num = 0
    octet = ip_str.split(".")
    for pow in range(3, -1, -1):
        ip_num += int(octet[3-pow]) * 256 ** pow
    return ip_num
    """

    # method 2
    return sum((1 << 8*(3 - n)) * octet for n, octet in zip(range(4), [ int(o_str) for o_str in ip_str.split(".") ]))

def num_to_ip_str(ip_num):
    """
    # method 1
    octet = []
    num = ip_num
    for pow in range(3, -1, -1):
        octet_num = num // (256 ** pow)
        octet.append(str(octet_num))
        num = num - octet_num * 256 ** pow
    return ".".join(octet)
    """

    # method 2
    return ".".join(str(o_num) for o_num in ip_num.to_bytes(4, byteorder='big'))

def subnetmask_num_to_cidr_num(subnetmask_num):
    return subnetmask_num.bit_count()

def cidr_num_to_subnetmask_num(cidr_num):
    """
    # method 1
    subnetmask_num = 0
    for i in range(cidr_num, 0, -1):
        subnetmask_num = (subnetmask_num >> 1) + 2 ** 31
    return subnetmask_num
    """

    # method 2
    return 0x100000000 - (1 << (32 - cidr_num))

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
#    will read stdin and the result will be shown on stdout
# ./cidr.py haha.txt
#    file haha.txt will be read and the result will be shown on screen
# ./cidr.py haha.txt hoho.txt
#    file haha.txt will be read and the result will be written to file hoho.txt
#

in_file= "cidr.txt" # default filename


out_file = open(sys.argv[2], "w") if len(sys.argv) > 2 else sys.stdout

in_file = open(sys.argv[1], "r") if len(sys.argv) > 1 else sys.stdin

print("ketu--> {in_file}")


"""
# method 1
while True:
    if in_file is sys.stdin:
        print("x.x.x.x/n: ", end="")
        line = input()
    else:
        line = in_file.readline()
    if not line:
        break
"""
# method 2
for line in in_file:
    print('test')
    cidr_addr = line.strip().split("/")
    ip_num = ip_str_to_num(cidr_addr[0])
    cidr_num = int(cidr_addr[1])
    
    subnetmask_num = cidr_num_to_subnetmask_num(cidr_num)

    ######
    ### relationship between those numbers ###
    ######
    network_num = ip_num & subnetmask_num
    broadcast_num = network_num | (0xffffffff - subnetmask_num)
    nth_host = ip_num - network_num
    first_host_num = network_num + 1 if cidr_num != 32 else network_num
    last_host_num = broadcast_num - 1 if cidr_num != 32 else network_num

    ######
    ### different str formatting
    ######
    print(line.strip(), ":", file=out_file)
    print("Network address: {0}".format(num_to_ip_str(network_num)), file=out_file)
    print(f"Subnet mask: {num_to_ip_str(subnetmask_num)}", file=out_file)
    print("Broadcast address:", num_to_ip_str(broadcast_num), file=out_file)
    print("First host ip in subnet: %s" % num_to_ip_str(first_host_num), file=out_file)
    print("Last host ip in subnet: %s" % num_to_ip_str(last_host_num), file=out_file)
    if nth_host == 0:
        print(f"{cidr_addr[0]} is the network address", file=out_file)
    elif nth_host == 255:
        print(f"{cidr_addr[0]} is the broadcast address", file=out_file)
    else:
        print(f"{cidr_addr[0]} is the #{nth_host} host within this network", file=out_file)
    print(f"! counter check: cidr number is { subnetmask_num_to_cidr_num(subnetmask_num) } !")
    print("", file=out_file)

if in_file is not sys.stdin:
    in_file.close()

if out_file is not sys.stdout:
    out_file.close()

