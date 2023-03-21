import ipaddress

x=input(str("input the IP address: "))
z=ipaddress.IPv4Network(x)

# check the 
print("netmask : " + str(z.netmask))
print("network address : " + str(z.network_address))

for a in z.hosts():
    print ("HOST: " + str(a))

    