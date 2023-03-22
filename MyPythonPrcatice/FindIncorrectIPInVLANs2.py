def calculate_network_address(ip_address, subnet_mask):
    # Convert IP address and subnet mask to binary strings
    ip_binary = ''.join([bin(int(octet))[2:].zfill(8) for octet in ip_address.split('.')])
    mask_binary = ''.join([bin(int(octet))[2:].zfill(8) for octet in subnet_mask.split('.')])
    
    # Calculate network address by performing a bitwise AND operation on the binary strings
    network_binary = ''.join([str(int(ip_binary[i]) & int(mask_binary[i])) for i in range(len(ip_binary))])
    
    # Convert binary network address back to dotted decimal format
    network_address = '.'.join([str(int(network_binary[i:i+8], 2)) for i in range(0, 32, 8)])
    
    return network_address

def calculate_subnet_range(network_address, subnet_mask):
    # Calculate the number of bits in the host portion of the subnet mask
    host_bits = 32 - sum([bin(int(octet))[2:].count('1') for octet in subnet_mask.split('.')])
    
    # Calculate the number of possible hosts on the subnet
    num_hosts = 2**host_bits - 2
    
    # Calculate the first and last valid host IP addresses on the subnet
    first_host = '.'.join(network_address.split('.')[:-1] + [str(int(network_address.split('.')[-1]) + 1)])
    last_host = '.'.join(network_address.split('.')[:-1] + [str(int(network_address.split('.')[-1]) + num_hosts)])
    
    return (first_host, last_host)

# VLAN A
vlan_a_address = '172.16.90.255'
vlan_a_subnet_mask = '255.255.240.0'
vlan_a_network_address = calculate_network_address(vlan_a_address, vlan_a_subnet_mask)
vlan_a_range = calculate_subnet_range(vlan_a_network_address, vlan_a_subnet_mask)

# VLAN B
vlan_b_address = '172.16.208.255'
vlan_b_subnet_mask = '255.255.240.0'
vlan_b_network_address = calculate_network_address(vlan_b_address, vlan_b_subnet_mask)
vlan_b_range = calculate_subnet_range(vlan_b_network_address, vlan_b_subnet_mask)

# Check PC1's IP address in VLAN A
pc1_address_a = '172.168.80.2'
if pc1_address_a >= vlan_a_range[0] and pc1_address_a <= vlan_a_range[1]:
    print('PC1 in VLAN A has the correct IP address')
else:
    print('PC1 in VLAN A has an incorrect IP address')

# Check PC2's IP address in VLAN A
pc2_address_a = '172.16.95.7'
if pc2_address_a >= vlan_a_range[0] and pc2_address_a <= vlan_a_range[1]:
    print('PC2 in VLAN A has the correct IP address')
else:
    print('PC2 in VLAN A has an incorrect IP address')

# Check PC3's IP address in VLAN B
pc3_address_b = '172.16.206.5'
if pc3_address_b >= vlan_b_range[0] and pc3_address_b <= vlan_b_range[1]:
    print('PC3 in VLAN B has the correct IP address')