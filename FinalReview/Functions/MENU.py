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