#!/usr/bin/env python3

def generate_vigenere_table_epa_65():
    html = "<html><head><title>Vigenère Table</title></head><body><table>"
    html += "<tr><th></th>"
    # Generate table body
    for i in range(26):
        html += "<tr>"
        html += f"<td>{chr(65+i)}</td>"
        for j in range(26):
            char = chr(((i+j) % 26) + 65)
            html += f"<td>{char}</td>"
        html += "</tr>"

    html += "</table></body></html>"

    # Save HTML to file
    with open("../Files-epa-65/vigenere_epa_65.html", "w") as file:
        file.write(html)

#Read function for global purspose
def read_file_epa_65():
    file_to_read_epa_65= "../Files-epa-65/encryptedmessage.txt"
    try:
        string_epa_65_read = open(file_to_read_epa_65.strip(), "r")
        string_epa_65 = string_epa_65_read.read()
        
    except OSError:
         print("The file is not correct")
         return
    
    return (string_epa_65)    

#Write function for global purpose
def write_to_file_epa_65(content_epa_65):
    # Open file for writing
    string_epa_65_write = open("../Files-epa-65/secondenryptedmessage.txt", "w")

    string_epa_65_write.write(content_epa_65)
    # Close the file
    string_epa_65_write.close()

#the key
def enter_key():
    key_epa_65 = input("What is the key you wan tot enter? ")  
    return (key_epa_65)   

# This function decrypts the
# encrypted text and returns
# the original text
def original_dec(string_epa_65, key):
    
    decrypted_message = ""
    for i in range(len(string_epa_65)):
        c = string_epa_65[i]
        k = key[i % len(key)]
        decrypted_message += chr((ord(c) - ord(k) + 26) % 26 + ord('A'))
    return decrypted_message

def original_enc(string_epa_65,key):
    
    encrypted_message = ""
    for i in range(len(string_epa_65)):
        c = string_epa_65[i]
        k = key[i % len(key)]
        encrypted_message += chr((ord(c) - ord(k) + 26) % 26 + ord('A'))
    return encrypted_message

# MAIN MENU
while True:
    # take input from the user Encrypt or Decrypt
    choice = input("Please choose an option:\n"
                    "1) Generate Vigenère table in .html format \n"
                    "2) Decrypt the message \n"
                    "3) Encrypt the message \n"
                    "4) No, thank you, I am good! \n")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        # num_of_rotations_epa_65 = int(input("Enter the number of rotations "))
        # if  num_of_rotations_epa_65 < 1 or num_of_rotations_epa_65 > 25 :
        #     print("Invalid input. Please enter a number between 1 and 25 inclusively.")
        #     continue

        if choice == '1' :
            #Generate Vigenère table in .html format
            generate_vigenere_table_epa_65()
            print("The HTML table is generated in ../Files-epa-65/vigenere_epa_65.html")

        elif choice== '2':
            #call the decrypt function
            enc_epa_65 = read_file_epa_65()
            key_entered_epa_65 = enter_key()  
            dec_epa_65 = original_dec(enc_epa_65, key_entered_epa_65)
            
            print(f"Encrypted messsage : { enc_epa_65 } \n" )
            print(f"Key: {key_entered_epa_65}\n")
            print(f"Decrypted message: {dec_epa_65} \n")
            
        elif choice== '3':
            #call the encrypt function
            original_epa_65 = "WELOVECYBERSECURITYCOURSES"
            key_epa_65="PYTHON"
            enc_epa_65=original_enc(original_epa_65,key_epa_65)
            write_to_file_epa_65(enc_epa_65)
            
            print(f"Original messsage : { original_epa_65 } \n" )
            print(f"Key: {key_epa_65}\n")
            print(f"Encrypted message: {enc_epa_65} \n")
            
        elif choice== '4':
            #call the encrypt function
            print("Have a nice day! The Encryption team is always at your service!")      
            break    
            
        # # # check if user wants another encryption/decryption
        # # # break the while loop if answer is no
        # next_encrypt_epa_65 = input("You want to continue again with the menu ? (yes/no): ").strip()
        # if next_encrypt_epa_65 == "no":
        #     break
    else:
        print("Invalid Input of menu \n")