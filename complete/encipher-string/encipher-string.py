"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""

#DID THIS ONE IN 15 MINUTES LET'S GOOOOOOOO

#notes
## you can get indices to loop back to 0 with [i % 26] (after 26, it'll go back to 0)
## 

def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""

    encoded_list = []

    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = upper_alpha.lower()

    #loop over string given 
    for idx, char in enumerate(txt): 
        #if the current character is an uppercase alpha char
        if char in upper_alpha:
            char_index = upper_alpha.index(char)
            encoded_list.append(upper_alpha[char_index + shift])

        elif char in lower_alpha:
            #find its index in alpha string and 
            char_index = lower_alpha.index(char)
            encoded_list.append(lower_alpha[char_index + shift])

        else: 
            encoded_list.append(char)
    
    return "".join(encoded_list)


    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
