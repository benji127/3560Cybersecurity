#########################################
#     Converting IP to number (decimal) #          
#########################################
# def ip_to_decimal(ip_address):
#     # Split the IP address into its four octets (segments)
#     octets = ip_address.split('.')
    
#     # Convert each octet to an integer and shift it to its proper position
#     decimal = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
    
#     return decimal

##########################################
#         USAGE OF THIS FUNCTION         #     
##########################################
#
# ip_address = input("What is the Ip address that you want to convert?")
# decimal = ip_to_decimal(ip_address)
# print(f"The IP converted into decimal is: {decimal}")  # Output: 3232235777
# ___________________________________________________________________________________________________

def ip_str_to_num(ip_str):
    ip_num = 0
    octet = ip_str.split(".")
    for pow in range(3, -1, -1):
        ip_num += int(octet[3-pow]) * 256 ** pow
    return ip_num

ip_str_to_num(input(""))

