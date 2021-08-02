"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # return none if needle not in haystack
    if needle not in haystack:
        return None

    #check if needle is the first ele   
    if needle == haystack[0]:
        return 0
    
    #if it's not, call function again and increment index 
    else:
        return 1 + recursive_index(needle, haystack[1:]) # => "you", ["hey", "there", "you"] => 1 + ["there", "you"] => 1 + 1 + ["you"]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO GO GO!\n")
