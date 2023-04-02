def rot13_encrypt(text):
    """Encrypts text using ROT13 algorithm"""
    result = ""
    for char in text:
        #char.isalpha() is a built-in Python method that returns a Boolean value 
        # indicating whether a given character is an alphabetic character. 
        # It returns True if the character is an uppercase letter, 
        # a lowercase letter, or a letter in some other alphabet, and False otherwise.
        if char.isalpha():
            #if it is uppercase() built in function
            if char.isupper():

                result += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            result += char
    return result


def rot13_decrypt(text):
    """Decrypts text using ROT13 algorithm"""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - 13) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - 13) % 26 + 97)
        else:
            result += char
    return result


# Open the file for reading
with open("sampleText.txt", "r") as input_file:
    # Read the contents of the file
    file_contents = input_file.read()

    # Encrypt the contents using ROT13
    encrypted = rot13_encrypt(file_contents)

# Open the file for writing
with open("output.txt", "w") as output_file:
    # Write the encrypted contents to the file
    output_file.write(encrypted)

# Open the file for reading
with open("output.txt", "r") as input_file:
    # Read the contents of the file
    file_contents = input_file.read()

    # Decrypt the contents using ROT13
    decrypted = rot13_decrypt(file_contents)

# Open the file for writing
with open("outputDecrypted.txt", "w") as output_file:
    #Write the decrypted contents to the file
    output_file.write(decrypted)