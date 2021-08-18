"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""

#Amy and I reverse engineered this!


def most_active(bio_data):
    """Find window of time when most authors were active."""

    # START SOLUTION

    # Make a minefield of years 1900-1999
    century = [0] * 100

    # Add 1 in every year when someone was active

    for person, start, end in bio_data: #unpack input data #'Alice', 1901, 1950
        for year in range(start, end + 1): #1901 => 1951 
            
            #print(f'year = {year}') 
            century[year - 1900] += 1 #put num in correct index (index is 1901-1900 = 1 => [0, 1, 0, 0...], 1951-1900 = 51)

    #print(f'century = {century}')
    # Find the period of time when the max number of people were active

    best = 0
    in_best = True
    best_start = 0
    best_end = 100

    for year, num_active in enumerate(century): 

        if num_active > best:  # New best; start tracking it
            best = num_active #set best to the current highest num
            in_best = True 
            best_start = year #set best_start to current year

        elif num_active < best and in_best:  # End of best-period window
            best_end = year - 1  #we want to call the end of our range the previous index/year
            in_best = False #we've come up to the end of best period so change in_best to False 

    return best_start + 1900, best_end + 1900
   

# def most_active_faster(bio_data):
#     """Find window of time when most authors were active."""

#     # Make two minefields of years 1900-1999

#     starts = [0] * 100
#     ends = [0] * 100

#     for person, start, end in bio_data:
#         starts[start - 1900] += 1 #= > [0, 1, 0, 0 , 0 , 0, 1] scattered 1s whenever we hit a year someone started
#         ends[end - 1900] += 1

#     best = 0
#     in_best = False
#     best_start = 0
#     best_end = 0

#     # How many people are currently active/inactive
#     num_active = 0

#     for year in range(100): #[1, 2, 3, 4, 5...]

#         num_active -= ends[year] #[]
#         num_active += starts[year]

#         if num_active > best:  # New best; start tracking it
#             best = num_active
#             in_best = True
#             best_start = year

#         elif in_best and num_active < best:  # New best; start tracking it
#             best_end = year
#             in_best = False

#     return best_start + 1900, best_end + 1900

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")