#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Enea Paja
# 2023/04/01

# May need pip3 install cryptography or 'pip3install cryptography -U' prior to running 
#import necessary Pyhton Modules

from cryptography.fernet import Fernet

def create_key():
    # Generate an enc key
    # Keep this secret and store in a secure location
    key = Fernet.generate_key()
    print("Key: " , key.decode())

def encrypt(plain_text, key):
    #convert pain_text and key into bytes for encryption
    plain_text = plain_text.encode()  
    key = key.encode()
    #encrypt the data using the provided key
    cipher_text = Fernet(key).encrypt(plain_text)
    # Convert the cipher_text back to a string
    cipher_text = cipher_text.decode()
    return cipher_text

def decrypt(cipher_text,key):
    # Convert cipher_text and key into bytes
    cipher_text = cipher_text.encode()
    key=key.encode()
    #Decrypt the data using the provided key
    plain_text = Fernet(key).decrypt(cipher_text)
    #conver the plain_text back to a string
    plain_text = plain_text.decode()
    return plain_text
encKey=""
#Prompt the user for the method to use
print( "Which  op would you like to do? ")
method=input(" Create key(c), Encrypt(e), Decrypt(d)" )
method = method[0].lower()
print(method)
#Using the first letter of the method call the correct functions 
if method =="c":
    create_key()
elif method =="e":
    #Prompt user for plain_text and encryptoiuon key
    plain_text=input("What is the message to enc? ")
    encKey = input("Encryption Key:")
    
    cipher_text = encrypt(plain_text, encKey)
    print(cipher_text)
elif method =="d":
    #Prompt the user for cipher_text message encryption key 
    cipher_text = input("Message to decrytop")
    encKey = input("Encryption key:")
    plain_text=decrypt(cipher_text,encKey)
    print(plain_text)
else:
    print("Wrong selection of the menu")    
