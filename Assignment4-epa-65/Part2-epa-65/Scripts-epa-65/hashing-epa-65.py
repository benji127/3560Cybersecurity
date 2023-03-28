#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Enea Paja - Assignment4 Part2
# date: 3/27/202123

import hashlib 

original_text_to_enc_epa_65 = "AVE CAESAR LEGIO X TE SALUTANT".lower()
modified_text_to_enc_epa_65 = original_text_to_enc_epa_65.replace(" x " , " ix ")
winner = ""

# Convert message to lower-case for simplicity

def rot_13_epa_65(text_to_enc_epa_65):
    final_message = ""
    # Loop through each letter in the source message
    for letter in text_to_enc_epa_65:
        # Convert the letter to the ASCII equivalent
        ascii_num = ord(letter)
        # Check to see if an alphabetic (a-z) character, 
        # if not, skip
        if ascii_num >= 97 and ascii_num <= 122:
            # Add 13 to ascii_num to "shift" it by 13
            new_ascii = ascii_num + 13
            # Confirm new character will be alphabetic 
            if new_ascii > 122:
                # If not, wrap around
                new_ascii = new_ascii - 26
            final_message = final_message + chr(new_ascii)
        else:
            final_message = final_message + chr(ascii_num)
    #Converted 
    return final_message

# Print the shortest value
def get_the_lowest_digest_epa_65():
    new_hash = -1
    for alg_epa_65 in hashlib.algorithms_available:
        hash_epa_65 = hashlib.new(alg_epa_65)
        if hash_epa_65.digest_size == 0:
            continue
        elif new_hash == -1 or hash_epa_65.digest_size < new_hash:
            new_hash = hash_epa_65.digest_size
            winner = alg_epa_65
    print(f"I am using : {winner}, because it is the lowest digest with size {new_hash}")    
    return winner

#hash function
def hash_epa_65(text_to_hash_epa_65):
    h_epa_65 = hashlib.new(winner)
    h_epa_65.update(text_to_hash_epa_65.encode())

    return h_epa_65.hexdigest()

#Print the results 

winner = get_the_lowest_digest_epa_65()

print (f"Original message:  {original_text_to_enc_epa_65}")
print (f"Encrypted original message:  {rot_13_epa_65(original_text_to_enc_epa_65)}")
print (f"Digest of the original message:  {hash_epa_65(original_text_to_enc_epa_65)}")
print (f"Modified message:  {modified_text_to_enc_epa_65}")
print (f"Encrypted modified message:  {rot_13_epa_65(modified_text_to_enc_epa_65)}")
print (f"Digest of the modified message:  {hash_epa_65(modified_text_to_enc_epa_65)}" )


