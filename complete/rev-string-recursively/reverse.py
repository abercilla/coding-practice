"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
    

    if len(astring) < 2:
        return astring

    return astring[-1] + rev_string(astring[:-1])

    
    # astring = 'porcupine'
    # return 'e' + 'porcupin' 

    #     astring = 'porcupin'
    #     return 'e' + ('n' + 'porcupi')
    
    #         astring = 'porcupi'
    #         return 'e' + 'n' + ('i' + 'porcup')

    #               astring = 'porcup'
    #               return 'e' + 'n' + 'i' + ('p' + 'porcu')

    #                   astring = 'porcu'
    #                   return 'e' + 'n' + 'i' + 'p' + ('u' + 'porc')

    #                       astring = 'porc'
    #                       return 'e' + 'n' + 'i' + 'p' + 'u' + ('c' + 'por')

    #                           astring = 'por'
    #                           return 'e' + 'n' + 'i' + 'p' + 'u' + 'c'  + ('r' + 'po')

    #                               astring = 'po'
    #                                return 'e' + 'n' + 'i' + 'p' + 'u' + 'c' + 'r' + ('o' + 'p')

    #                                  astring = 'p'
    #                                   return 'e' + 'n' + 'i' + 'p' + 'u' + 'c' + 'r' + 'o' + 'p' + ''



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
