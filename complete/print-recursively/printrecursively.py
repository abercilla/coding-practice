"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

   >>> print_recursively([5, 3, 6, 8])
   5
   3
   6
   8

   >>> print_recursively([])

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""

    # if lst is empty, break
    if not lst:  
        return 
        
    # print first item in list
    print(lst[0])

    # remove first item in list
    lst.remove(lst[0])

    # call function again
    print_recursively(lst)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. GREAT JOB!\n")
