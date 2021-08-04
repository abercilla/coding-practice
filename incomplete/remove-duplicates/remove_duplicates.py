""" Remove duplicates in a list

For example::

    >>> remove_duplicates([6, 9, 7, 9, 2, 6, 0])
    [6, 9, 7, 2, 0]

    >>> remove_duplicates([])
    []

    >>> remove_duplicates([6, 9, 7])
    [6, 9, 7]

"""


def remove_duplicates(items):
    """Remove duplicates in the list items and return that list."""

    i = 0 
    j = 1
            
    for item in items[j:]: #[9, 7, 9, 2, 6, 0]

        #if the first item is equal to the current item we're looking at
        if items[i] == item: #=> if 6 == [9, 7, 9, 2, 6, 0]
            #remove the duplicate item
            items.remove(item)

            print(f'items now = {items}')
    
    #move on to the next item to compare to rest of list => 9 
    i += 1
    #move slice up => [7]
    j += 1

        #print(f'item in loop')
    
    return items


    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")



