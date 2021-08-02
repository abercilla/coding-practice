"""Given a list of numbers 1...max_num, find which one is missing in a list."""

#define function that takes in list of nums, and max_num
def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
# -----------------------my solution ---------------------#

    range_list = [] #[7, 3, 2, 4, 5, 6, 1, 9, 10] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #use range to look at all numbers from 1 to max_num
    for i in range(1, max_num + 1):

        range_list.append(i)
    
    #loop over the range to make sure each num in range is in the list we're given
    for range_num in range_list:

        #if one of the nums in the range is NOT in our list, return that num in range
        if range_num not in nums:

            return range_num

# #----------------without adding a new list -------# 

#     #loop over all nums from 1 to max_num
#     for i in range(1, max_num + 1):

#         #if current num we're looping over in range is not in given list, return it
#         if i not in nums: 
#             return i


# #----------from HB SOLUTIONS-------# (ridiculous)

    # 1st solution: Initial solution: keep track of what you've
    #               seen in a separate list

    #initialize a list => [False] * 10 => [False, False, False, False, False, False, False, False, False, False]
    # seen = [False] * max_num

    # #loop over given list => [7, 3, 2, 4, 5, 6, 1, 9, 10]
    # for n in nums:
        
    #     # list starts as => [False, False, False, False, False, False, False, False, False, False]
    #     # # change False to True in seen list if it's in our given list nums 

    #     # # seen is in order => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #     # # find index of current num in seen [7..] => seen[7-1] => seen[6] => where 7 would be in seen list of [False, False..]
    #     # # change to True bc we've "seen" it => [False, False, False, False, False, **True**, False, False, False, False]
        
    #     seen[n - 1] = True
    
    # #[True, True, True, True, True, True, True, False, True, True]
    # # # return seen

    # # # The False value is the one we haven't seen
    
    # # # get the index of wherever the last "False" is and add 1 to get the actual num instead of index
    # return seen.index(False) + 1

# #---------------without a new list and O(n)--------#


        # 3rd solution: find missing number by comparing expected sum vs actual

    # # sum all numbers in the expected range => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => 55
    # expected = sum(range(max_num + 1))
        

    # # Alternatively, there's a math formula that finds the sum of 1..n
    # # https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
    # #
    # # expected = ( n + 1 ) * ( n / 2 )}
    
    # # # subtract the expected sum from actual sum of given list nums
    # return expected - sum(nums)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
