#!/usr/bin/env/pythin3
#Enea Paja
#2023-03-23

source_message=input("What is the maessage to encrypt ?")
source_message = source_message.lower()
final_message=""

#get any letter on the input 
for letter in source_message:

    #and output it in ASCII number ord() built in function
    ascii_num=ord(letter)

    #letter value in ASCII starts and since it is used lower() function we except values from 'a'(97) - 'z'(122)
    if ascii_num >= 97 and ascii_num <=122:
        new_ascii = ascii_num +13
        #check if the number is bigger than ASCII value 122
        if new_ascii > 122:
            #make a total spin
            new_ascii= new_ascii-26
        #convert the message to letters again after repositioning    
        final_message = final_message + chr(new_ascii)
    else:
        final_message = final_message + chr(ascii_num)

print("Message has been converted") 

print(final_message)
