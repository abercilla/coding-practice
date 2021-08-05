"""Return new list from items with duplicates removed.

For example::

    >>> deduped([1, 1, 1])
    [1]

Keep items in the order where they first appeared::

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

A list with no duplicates would return the same::

    >>> deduped([1, 2, 3])
    [1, 2, 3]

This should return a *new* list, not mutate the existing
list::

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

An empty list should return an empty list::

    >>> deduped([])
    []

"""


def deduped(items):
    """Return new list from items with duplicates removed."""
    
    deduped = []
    seen = set()

    #if list isn't empty
    if not items:
        return items
    #loop over list of items[1:] => [9, 7, 9, 2, 6, 0]
    for item in items:
        #lookup in a set instead of a list to cut runtime down from O(n^2) to O(n)
        if item not in seen:
            seen.add(item) 
            deduped.append(item)
    
    return deduped
    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE NO DUPE!\n")
