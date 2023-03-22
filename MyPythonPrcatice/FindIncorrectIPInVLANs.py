#!/usr/bin/python3

def binary_subnet_mask(subnet_mask):
    # Convert subnet mask to binary string
    octets = [int(octet) for octet in subnet_mask.split('.')]
    binary = ''
    for octet in octets:
        binary += '{:08b}'.format(octet)
    return binary

def binary_ip_address(ip_address):
    # Convert IP address to binary string
    octets = [int(octet) for octet in ip_address.split('.')]
    binary = ''
    for octet in octets:
        binary += '{:08b}'.format(octet)
    return binary

def binary_network_address(ip_address, subnet_mask):
    # Calculate binary network address
    ip_bin = binary_ip_address(ip_address)
    subnet_mask_bin = binary_subnet_mask(subnet_mask)
    network_bin = ''
    for i in range(len(ip_bin)):
        network_bin += str(int(ip_bin[i]) & int(subnet_mask_bin[i]))
    return network_bin

def check_ip_address(ip_address, subnet_mask, expected_network):
    # Check if IP address is assigned correctly
    network_bin = binary_network_address(ip_address, subnet_mask)
    return network_bin == expected_network

# VLAN A
subnet_mask_a = '255.255.240.0'
expected_network_a = '1010110000010000'
pc1_ip_address_a = '172.168.80.2'
pc2_ip_address_a = '172.16.95.7'

# Check PC1's IP address in VLAN A
if check_ip_address(pc1_ip_address_a, subnet_mask_a, expected_network_a):
    print('PC1 in VLAN A has the correct IP address')
else:
    print('PC1 in VLAN A has an incorrect IP address')

# Check PC2's IP address in VLAN A
if check_ip_address(pc2_ip_address_a, subnet_mask_a, expected_network_a):
    print('PC2 in VLAN A has the correct IP address')
else:
    print('PC2 in VLAN A has an incorrect IP address')

# VLAN B
subnet_mask_b = '255.255.240.0'
expected_network_b = '1010110001100000'
pc3_ip_address_b = '172.16.206.5'
pc4_ip_address_b = '172.16.223.1'

# Check PC3's IP address in VLAN B
if check_ip_address(pc3_ip_address_b, subnet_mask_b, expected_network_b):
    print('PC3 in VLAN B has the correct IP address')
else:
    print('PC3 in VLAN B has an incorrect IP address')

# Check PC4's IP address in VLAN B
if check_ip_address(pc4_ip_address_b, subnet_mask_b, expected_network_b):
    print('PC4 in VLAN B has the correct IP address')
else:
    print('PC4 in VLAN B has an incorrect IP address')