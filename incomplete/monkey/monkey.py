"""When can the monkey cross the river?

In this problem, a monkey is trying to jump across a certain 
distance across a river, using stones in the river to break its
jumps into sections.

However, the monkey can only jump N number of stones at a time.

As an added piece of complexity, the water level is decreasing 
with each hour, and as the water level gets lower, more stones 
emerge for the monkey to use to cross the river.

We can represent the `stones` in the river like this::

    [ 1, 2, 5, 0, 3, 4 ]

Where the number in the array corresponds to when the stone will 
emerge. (Bigger numbers are later in time.)

The stone times are **unique** -- numbers in
the list will never appear more than once.

So, for the above array, at time `t`, the stones would emerge as::

    t     river (* stone, - not yet a stone)
    -     ----------------------------------
    0     [ -  -  -  *  -  -  ]
    1     [ *  -  -  *  -  -  ]
    2     [ *  *  -  *  -  -  ]
    3     [ *  *  -  *  *  -  ]
    4     [ *  *  -  *  *  *  ]

Write a function that given the `stones` in the river as represented 
above, and the number of stones the monkey is able to jump, the earliest
time `t` that the monkey would be able to make it across the river.

For example::

    >>> earliest_arrival(3, [1, 2, 3, 0])
    1

    >>> earliest_arrival(2, [1, 2, 3, 0]) 
    2

    >>> earliest_arrival(3, [1, 4, 0, 2, 3, 5])
    2

    >>> earliest_arrival(5, [5, 2, 3, 8, 9, 99, 4, 0])
    3

"""


def earliest_arrival(jump_distance, stones):
    """Find the earliest time a monkey can jump across a river."""
    #jump_distance of 3 means they skip 2 stones and land on 3rd
    stone = ''
    #based on jump_distance, what are all the stone nums within that distance
    #when jump_distance is 5, can jujp to stones[4]
    
    stone = min(stones[:(jump_distance - 1)]) #stone = 2

    t = max(0, stone) #t = 2
    print(f't starts at = {t}')
    i = stones.index(stone) # i = 1
    print(f'i starts at = {i}')   
    #as long as 
    while i + jump_distance <= len(stones) - 1: # 3 + 5 <= 7
        print(f'i + jump_distance = {i + jump_distance}')

        stone = min(stones[(i + 1):(i + jump_distance)]) #stone = 3
        print(f'stone: {stone}')
        if t < stone: 
            t = stone #reassign to 3
         
        i = stones.index(stone) # i = 2
        print(f'i = {i}')  
        stone = min(stones[(i + 1):(i + jump_distance)]) #stone 
        t = max(t, stone)
        print(f'end of while loop: t = {t}') 
    
    return t
    #what's the lowest num within that jump_distance 
    #go to that stone, then look at next stones in new jump_distance
    #t becomes whatever stone we jumped to
    #if the next stone we jump to is a higher value, reassign t
    #get length of list of stones so we don't go past length
    #var assigned to len(list) and compare to index we're at 
    #if index we're jumping to is higher than len of list, then we're done
    #control for indexerror with while loop?
    #   


if __name__ == "__main__":
    import doctest
    if not doctest.testmod().failed:
        print("\n*** ALL TESTS PASS; YOU MUST BE JUMPING WITH JOY\n")
