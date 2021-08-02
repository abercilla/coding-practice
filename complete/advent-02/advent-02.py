"""Return Valid Passwords"""

#------------------ PART 1-------------------------#
def count_valid_passwords(file):
    """Count valid passwords from text file"""


    handle = open(file)
    
    valid_count = 0

    #loop over each line of file
    for line in handle: 
        line = line.rstrip()

        char_range, letter, password = line.split()
        letter = letter.rstrip(":")

        min_char, max_char = char_range.split("-")
        min_char = int(min_char)
        max_char = int(max_char)


        # make sure letter is in the password
        if letter in password: 
            
            #unpack range
            full_char_range = []
 
            for i in range(min_char, max_char+1):
                full_char_range.append(i)


            # count how many times the letter is in the password 
            letter_count = 0 
            
            for char in password: 
                if char == letter:
                    letter_count += 1
            
            if letter_count in full_char_range: 
                
                #increment the password as a valid passowrd
                valid_count +=1

    return valid_count