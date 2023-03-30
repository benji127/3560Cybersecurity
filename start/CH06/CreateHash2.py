#!/usr/bin/env python3
# Script that hashes a password with provided salt
# By Enea Paja


import crypt

plain_pass = "123456"
salt= "addingsomesalt"

print("MD5      :  {0}".format(crypt.crypt(plain_pass,"$1$-"+ salt)))
print("Blowfish :  {0}".format(crypt.crypt(plain_pass, "$2a$-"+ salt)))
print("SHA-256  :  {0}".format(crypt.crypt(plain_pass, "$5$-"+ salt)))
print("SHA-512  :  {0}".format(crypt.crypt(plain_pass, "$6$-"+ salt)))
