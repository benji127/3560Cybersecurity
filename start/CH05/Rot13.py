#!/usr/bin/env/pythin3
#Enea Paja
#2023-03-23

source_message=input("What is the maessage to encrypt ?")
source_message = source_message.lower()
final_message=""

for letter in source_message:
    ascii_num=ord(letter)

    if ascii_num >= 97 and ascii_num <=122:
        new_ascii = ascii_num +13

        if new_ascii > 122:
            new_ascii= new_ascii-26
        final_message = final_message + chr(new_ascii)
    else:
        final_message = final_message + chr(ascii_num)

print("Message has been converted") 

print(final_message)
