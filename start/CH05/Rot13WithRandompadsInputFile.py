#!/usr/bin/env/pythin3
#Enea Paja
#2023-03-23

#python rot13 script reading from a file and the letter include upper 
#case letter and lower case letters and rotate based on a one time 
#pad using a separate file filled with random numbers , rotate each 
#character using this numbers. Do it  using separate functions for each operation
import onetimepad


#function to read the file
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
# function to write the file
def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        
#read one time pad values from the file.
def read_one_time_pad(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split()]
# function to encrypt the file based on numbers given form one time pad file
def rot13_encrypt(input_filename, output_filename, pad_filename):
    plaintext = read_file(input_filename)
    pad = read_one_time_pad(pad_filename)

    ciphertext = ''
    for i, char in enumerate(plaintext):
        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + pad[i]) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + pad[i]) % 26 + 97)
        else:
            encrypted_char = char
        ciphertext += encrypted_char

    write_file(output_filename, ciphertext)

def rot13_decrypt(input_filename, output_filename, pad_filename):
    ciphertext = read_file(input_filename)
    pad = read_one_time_pad(pad_filename)

    plaintext = ''
    for i, char in enumerate(ciphertext):
        if char.isupper():
            decrypted_char = chr((ord(char) - 65 - pad[i]) % 26 + 65)
        elif char.islower():
            decrypted_char = chr((ord(char) - 97 - pad[i]) % 26 + 97)
        else:
            decrypted_char = char
        plaintext += decrypted_char

    write_file(output_filename, plaintext)