"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    
    #create empty list []
    chars = []
    
    for char in word: 
        #add every new char to list
        if char not in chars: #is this an additional for loop? 
            chars.append(char)
        #if encounter the char again, remove char from list 
        else: 
            chars.remove(char)
    
    #if length of word is even and list is empty, is palindrome
    if (len(word) % 2 == 0) and (len(chars) == 0):
        return True

    #if length of word is odd and list is == 1, is palindrome
    if (len(word) % 2 != 0) and (len(chars) == 1):
        return True   
    else: 
        return False
    
    # [aaaabbbb] = [bbaaaabb]
    # [aaabbbb] = [bababab]


# ---------- HB Solution -------------#

# def is_anagram_of_palindrome(word):
#     """Is the word an anagram of a palindrome?"""

#     # START SOLUTION

#     seen = {}

#     # Count each letter

#     for letter in word:
#         count = seen.get(letter, 0)
#         seen[letter] = count + 1

#     # It's a palindrome if the number of odd-counts is either 0 or 1

#     seen_an_odd = False

#     for count in seen.values():
#         if count % 2 != 0: #if we come across an odd count #
#             if seen_an_odd: #there can only be one char with an odd count
#                 return False #immediate exit if there are multiple chars with odd count
#             seen_an_odd = True

#     return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
