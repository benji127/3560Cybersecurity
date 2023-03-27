#!/usr/bin/env/pythin3
#Enea Paja - Assignment4
#2023-03-27




#encrypt function
def encrypt_epa_65(num_of_rotations_epa_65):
    path_epa_65 ="/home/enea6865/Desktop/Assignment4-epa-65/Part1-epa-65/Files-epa-65/"
    file_to_read_epa_65= path_epa_65 + input("What is the file you want read ?")
    try:
        file_epa_65 = open(file_to_read_epa_65.strip(), "r")
    except OSError:
         print("The file is not correct")
         return
    for line_of_file_epa_65 in file_epa_65:

        source_message_epa_65 = line_of_file_epa_65.lower()
        final_message_epa_65=""

        for letter in source_message_epa_65:
            ascii_num=ord(letter)

            if ascii_num >= 97 and ascii_num <=122:
                new_ascii = ascii_num + num_of_rotations_epa_65

                if new_ascii > 122:
                    new_ascii= new_ascii-26
                final_message_epa_65 = final_message_epa_65 + chr(new_ascii)
            else:
                final_message_epa_65 = final_message_epa_65 + chr(ascii_num)

        print(final_message_epa_65.strip())

#decrypt function
def decrypt_epa_65(Number_of_rotations_epa_65):
    path_epa_65 ="/home/enea6865/Desktop/Assignment4-epa-65/Part1-epa-65/Files-epa-65/"
    file_to_read_epa_65= path_epa_65 + input("What is the file you want read ?")
    try:
        file_epa_65 = open(file_to_read_epa_65.strip(), "r")
    except OSError:
         print("The file is not correct")
         return
    for line_of_file_epa_65 in file_epa_65:

        source_message_epa_65 = line_of_file_epa_65.lower()
        final_message_epa_65=""

        for letter in source_message_epa_65:
            ascii_num=ord(letter)

            if ascii_num >= 97 and ascii_num <=122:
                new_ascii = ascii_num - num_of_rotations_epa_65

                if new_ascii < 97:
                    new_ascii= new_ascii+26
                final_message_epa_65 = final_message_epa_65 + chr(new_ascii)
            else:
                final_message_epa_65 = final_message_epa_65 + chr(ascii_num)

        print(final_message_epa_65.strip())


# MAIN MENU
while True:
    # take input from the user Encrypt or Decrypt
    choice = input("Enter choice(E-encrypt or D-Decrypt): ")

    # check if choice is one of the four options
    if choice in ('d', 'D', 'e', 'E'):
        num_of_rotations_epa_65 = int(input("Enter the number of rotations "))
        if  num_of_rotations_epa_65 < 1 or num_of_rotations_epa_65 > 25 :
            print("Invalid input. Please enter a number between 1 and 25 inclusively.")
            continue

        if choice == 'e' or choice == 'E':
            #call encrypt function
            encrypt_epa_65(num_of_rotations_epa_65)

        else:
            #call the decrypt function
            decrypt_epa_65(num_of_rotations_epa_65)     

        # check if user wants another encryption/decryption
        # break the while loop if answer is no
        next_encrypt_epa_65 = input("You want to continue encrypt/decrypt ? (yes/no): ").strip()
        if next_encrypt_epa_65 == "no":
            break
    else:
        print("Invalid Input of menu")










#Assignmem44
#
#
#
#
#
#
#
#
#
#
#
