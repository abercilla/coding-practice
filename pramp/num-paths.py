
"""

For example::

    >>> numOfPathsToDest(4)
    5

"""

def numOfPathsToDest(n):
    #if square is only 1 square, there is only one possible path to
    if (n == 1):
        return 1

    lastRow = []
    for i in range(1, n-1):
        lastRow[i] = 1 # base case - the first row is all ones

    currentRow = []

    for j in range(1, n-1):
        for i in range(j, n-1):
            if (i == j):
                currentRow[i] = lastRow[i]
            else:
                currentRow[i] = currentRow[i-1] + lastRow[i]
        lastRow = currentRow

    return currentRow[n-1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
