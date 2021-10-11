"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True


Let's make sure it works when we can spend over 10 pennies::

    >>> coins(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
    True

"""

#--------------------ANNE AND KAVYA SOLUTIONS------------#




def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    
    Anne + Kavya Solution, Non-Recursive
    """

    amounts_change = [num_coins] # {3, 12, 21, 30}
    
    while num_coins > 0: #O(n) where n = num_coins
        amount = amounts_change[-1] #21 O(1)
        amounts_change.append(amount + 9) #{3, 12, 21, 30} O(1)
        num_coins -= 1 #2 - 1 - 0 
    # 1 + 1
    # 1 + 10
    # 10 + 10

        
    return set(amounts_change)


def coins(num_coins, amounts_change = [0]):
   """Pass through an amounts_change list each recursive call

      Anne + Kavya, recursive solution""" 

    if num_coins == 0: 
        return set(amounts_change)
    if len(amounts_change) == 1:  #[3, 12]
        amounts_change = [num_coins] #reset list to num_coins
        #return set(amounts_change)
    amount = amounts_change[-1] # 3 - 12 
    amounts_change.append(amount + 9) #[3, 12, 21]
    num_coins -= 1
    
    return coins(num_coins, amounts_change) #coins(1, [3, 12, 21])

#  1 + 1 + 1 + 1 pennies = 4 , dimes = 0
#     1 + 1 + 1 + 10 pennies = 3, dimes = 1
#     1 + 1 + 10 + 10 pennies = 2, dimes = 2
#     1 + 10 + 10 + 10 pennies = 1, dimes = 3
#     10 + 10 + 10 + 10 pennies = 0, dimes = 4

#----------------HB SOLUTIONS--------------------------------------
# def coins(num_coins): 
#     """HB Solution Non-Recurisve"""

#     amounts_change = set()

#     for pennies in range(0, num_coins + 1): #loop over every possibility for pennies, if num_coins is 4, pennies will be 0-4
#         dimes = num_coins - pennies #dimes has inverse relationship with pennies
#         amounts_change.add((dimes * 10) + (pennies * 1)) #create the change and add to set 
   

#     return amounts_change
#------------------------------------------------------
# def add_coins(left, total, results):
#     """Add combos coins to total.

#     If this is the last time we can add coins, return change.

#     Otherwise, recursively call until that condition.

#         >>> results = set()
#         >>> add_coins(left=1, total=0, results=results)
#         >>> results == set([1, 10])
#         True
#     """

#     DIME = 10
#     PENNY = 1

#     if left == 0:
#         # Base Case
#         # We've added all the coins we're supposed to, so keep
#         # track of this total of change and stop recursing
#         results.add(total)
#         return

#     # Fork into two recursions, one adding a dime and another a penny
#     # For each, we'll have 1 fewer coin to add afterwards, so left -= 1
#     add_coins(left - 1, total + DIME, results) #add_coins(left = 2, total = 10, results = set())
#     add_coins(left - 1, total + PENNY, results) #add_coins (left = 2, total = 1, results = set())


# def coins(num_coins):
#     """HB Solution, Recursive"""
 
#     """Find change from combinations of `num_coins` of dimes and pennies.

#     This should return a set of the unique amounts of change possible.
#     """

#     # START SOLUTION

#     results = set()

#     add_coins(left=num_coins, total=0, results=results) #add_coins(left = 3, total = 0, results = set())

#     return results

#------------------------------------------------------


# assert(coins(0) == {0})

# assert(coins(1) == {1, 10})

# assert(coins(2) == {2, 11, 20})

# assert(coins(3) == {3, 12, 21, 30})

# assert(coins(4) == {4, 13, 22, 31, 40})


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n")