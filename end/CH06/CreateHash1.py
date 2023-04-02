#!/usr/bin/env python3
# Script that hashes a password
# By Enea Paja  
# date: 2023/02/30

# Import Python modules
import crypt

# Prompt user for plain-text password
plain_pass = input("What is the password? ")

# Print out hashes
print("MD5       : {0}".format(crypt.crypt(plain_pass,"$1$")))
print("Blowfish  : {0}".format(crypt.crypt(plain_pass,"$2a$")))
print("eksblofish: {0}".format(crypt.crypt(plain_pass,"$2y$")))
print("SHA-256   : {0}".format(crypt.crypt(plain_pass,"$5$")))
print("SHA-512   : {0}".format(crypt.crypt(plain_pass,"$6$")))

