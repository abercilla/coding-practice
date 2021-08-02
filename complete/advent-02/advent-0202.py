"""part 2 of day 2 in advent code challenge"""

""" 
    new rules: 
    
    Each policy actually describes two positions in the password, 
    where 1 means the first character, 2 means the second character, and so on. 
    (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
    Exactly one of these positions must contain the given letter. 
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

"""
#refactor into two separate functions

#---------------------PART 2 -------------------#
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
        
        #if the letter matches EITHER whatever is at the password index [min_char-1] OR [max_char -1] but NOT BOTH
        if (letter == password[min_char - 1] and letter != password[max_char - 1]) or (letter == password[max_char - 1] and letter != password[min_char - 1]): 
           
            #increment the password as a valid passowrd
            valid_count +=1


    return valid_count

    # 15-17 so indices are [14] and [16]

    # p p p p p p p p p p p  p p  p  s  p  s



    # x j w j j l j j j j d  j  j  j  j  m  j  j
    # 0 1 2 3 4 5 6 6 7 8 9 10 11 12 13 14 15 16 17
    # 1 2 3 4 5 6 7 8 9 10  11 12 13 14 15 16   
    