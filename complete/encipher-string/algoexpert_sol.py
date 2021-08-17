def cipherString(string, key):
    """return the ciphered string using unicode"""

    #initalize a new list to keep ciphered chars
    ciphered_chars = []

    #make sure key will wrap back around if larger than 26
    new_key = key % 26

    #loop over the string and append ciphered versions of each char to ciphered_chars
    for letter in string: 
        #getNewLetterCode is a helper function that will return the ciphered char for each letter 
        ciphered_chars.append(getNewLetterCode(letter, new_key))

    return "".join(ciphered_chars)

def getNewLetterCode(letter, key):
    """get the new letter codes for each char"""

    #get the new code for each letter by getting unicode code and shifting by key
    new_letter_code = ord(letter) + key

    #if within the unicode range for alpha (97-122), return the ciphered char to be appended to ciphered_chars
    if new_letter_code <= 122: 
        return chr(new_letter_code)

    #if we shift outside of the unicode range for alphabet (97-122), wrap back around and add 96 to get back into unicode range
    else: 
        return chr(96 + new_letter_code % 122)
