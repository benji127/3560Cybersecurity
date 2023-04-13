#!/usr/bin/env python3
# Assignment5b - Enea Paja - 300356865

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

#Read function for global purspose
def read_file_epa_65():
    file_to_read_epa_65= "../Files-epa-65/encryptedmessage.txt"
    try:
        string_epa_65_read = open(file_to_read_epa_65, "r")
        string_epa_65 = string_epa_65_read.read()
        print(string_epa_65)
        
    except OSError:
         print("The file is not correct")
         return
    
    return (string_epa_65.encode())    


#Read function for global purspose
def read_cipher_file_epa_65():
    file_to_read_epa_65= "../Files-epa-65/secondenryptedmessage.txt"
    try:
        string_epa_65_read = open(file_to_read_epa_65, "rb")
        string_cipher_epa_65 = string_epa_65_read.read()
        print(string_cipher_epa_65)
        
    except OSError:
         print("The file is not correct")
         return
    
    return (string_cipher_epa_65)    


#Write function for global purpose
def write_to_file_epa_65(content_epa_65):
    # Open file for writing
    string_epa_65_write = open("../Files-epa-65/secondenryptedmessage.txt", "wb")

    string_epa_65_write.write(content_epa_65)
    # Close the file
    string_epa_65_write.close()

def generate_private_key_epa_65():
    # Generate the RSA private key
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return key

def encrypt(key,string_epa_65):
# def message = b"secret text"
    ciphertext = key.public_key().encrypt(
        string_epa_65,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def decrypt_new(key,ciphertext):
    plaintext = key.decrypt(
        ciphertext,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
    )
    
    return plaintext

key_epa_65 = generate_private_key_epa_65()

# MAIN MENU
while True:
    
    # take input from the user Encrypt or Decrypt
    choice = input("Please choose an option:\n"
                    "1) Encrypt the message \n"
                    "2) Decrypt the message \n"
                    "3) No, thank you, I am good! \n")

    # check if choice is one of the four options
    if choice in ('1', '2', '3'):
        if choice== '1':
            #call the decrypt function
            message_epa_65 = read_file_epa_65()
            enc_epa_65 = encrypt(key_epa_65, message_epa_65)
            
            print(f"Original messsage : { message_epa_65 } \n" )
            print(f"Encrypted messsage : { enc_epa_65 } \n" )
            write_to_file_epa_65(enc_epa_65)
            
        elif choice== '2':
            #call the encrypt function
            cipher =read_cipher_file_epa_65()
            dec_epa_65 = decrypt_new(key_epa_65,cipher)
            
            print(f"Original messsage : { cipher } \n" )
            print(f"Encrypted message: {dec_epa_65} \n")
            
        elif choice== '3':
            #call the encrypt function
            print("Have a nice day! The Encryption team is always at your service!")      
            break    
    else:
        print("Invalid Input of menu \n")