"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    #initalize set of vowels (for better lookup)
    vowels = set("aeiou")
    # #split phrase into list of words
    words = phrase.split()

    end_phrase = []
    #  #loop over the words in the phrase
    for word in words:  
    # #if word beings with consonant, move first letter [0] to end and append "ay" after word
        if word[0] not in vowels: #("hello")
            word = word[1:] + word[0] + "ay"
    # #if word begins with a vowel, append "yay" after word
        else:
            word = word + "yay"
    # # add word to new list
        end_phrase.append(word)
            
    # # join together as string again at end
    return " ".join(end_phrase)

    





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. REATGAY OBJAY!\n")
