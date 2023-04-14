#encrypt function MROT13
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
