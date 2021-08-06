"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    alpha = set("abcdefghijklmnopqrstuvwxyz")

    sentence_chars = set(sentence)

    if len(sentence_chars) >= len(alpha): #if there are additional chars like "!" or "&"
        return True
    else: 
        return False

    #-----alternate solution from HB => use *is.alpha()* to isolate alpha chars --------#

    # #put all alpha chars from given sentence in lowercase form in a new set called used 
    # used = {char.lower() for char in sentence if char.isalpha()}
    
    # #return boolean for if the lenth of set is exactly equal to 26 ?? doesn't account for other chars
    # return len(used) == 26



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
