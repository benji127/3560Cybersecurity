#!/usr/bin/env python3
# Script that hashes a password
# By  Enea Paja\
# 2023/03/30

import crypt

plain_pass = "Class3560March30"

print("MD5 : {0}".format(crypt.crypt(plain_pass,"$1$")))
print("Blowfish :  {0}".format(crypt.crypt(plain_pass, "$2a$")))
print("SHA-256 :  {0}".format(crypt.crypt(plain_pass, "$5$")))
print("SHA-512 :  {0}".format(crypt.crypt(plain_pass, "$6$")))

