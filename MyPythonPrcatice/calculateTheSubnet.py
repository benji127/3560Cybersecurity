import ipaddress

def calculate_subnet(ip_address):
    """
    Given an IP address (as a string), returns its subnet and number of hosts.
    """
    ip = ipaddress.IPv4Address(ip_address)
    network = ipaddress.IPv4Network(ip, strict=False)
    subnet = str(network.network_address) + '/' + str(network.prefixlen)
    num_hosts = network.num_addresses - 2  # Subtract network and broadcast addresses
    return subnet, num_hosts

# Read IP addresses from input file
input_file = 'input.txt'
with open(input_file, 'r') as f:
    ip_addresses = f.read().splitlines()

# Calculate subnets and number of hosts for each IP address
subnets_and_hosts = []
for ip_address in ip_addresses:
    subnet, num_hosts = calculate_subnet(ip_address)
    subnets_and_hosts.append((ip_address, subnet, num_hosts))

# Write subnets and number of hosts to output file
output_file = 'output.txt'
with open(output_file, 'w') as f:
    for ip_address, subnet, num_hosts in subnets_and_hosts:
        f.write(ip_address + ',' + subnet + ',' + str(num_hosts) + '\n')