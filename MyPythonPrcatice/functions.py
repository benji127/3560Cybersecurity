#########################################
#     Converting IP to number (decimal) #          
#########################################
def ip_to_decimal(ip_address):
    # Split the IP address into its four octets (segments)
    octets = ip_address.split('.')
    
    print(octets)
    # Convert each octet to an integer and shift it to its proper position
    decimal = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
    
    print(decimal)
    return decimal

##########################################
#         USAGE OF THIS FUNCTION         #     
##########################################
#
# ip_address = input("What is the Ip address that you want to convert?")
# decimal = ip_to_decimal(ip_address)
# print(f"The IP converted into decimal is: {decimal}")  # Output: 3232235777
# ___________________________________________________________________________________________________

def ip_to_decimal_2(ip_address):
    ip_num = 0
    octet = ip_address.split(".")
    for pow in range(3, -1, -1):
        ip_num += int(octet[3-pow]) * 256 ** pow
    print(ip_num)
    return ip_num   

def dec_to_ip(decimal):
    octets = []
    for i in range(4):
        octet = int(decimal) % 256
        octets.append(str(octet))
        decimal//=256
    print(".".join(octets))
    return ".".join(octets)
 


ip_num= input("What the IP ? ")
# ip_to_decimal(ip_num)
# ip_to_decimal_2(ip_num)
dec_to_ip(ip_num)


 

