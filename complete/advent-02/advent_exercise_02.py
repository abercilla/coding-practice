"""Complete Challenge 2 for Advent Exercise"""

#find THREE numbers that sum to 2020 and return product

# ATTEMPT 1 ------


def find_nums(file):
    """Find three nums that sum to 2020"""

    handle = open(file)

    list_nums = []

    #add nums into list
    for line in handle:
        line = line.rstrip() # => strip any whitespace off of line
        line = int(line) # => convert to integers
        list_nums.append(line) # => add num to list 

    #find nums that sum to 2020

    #loop over list of nums
    for num in list_nums: 

        #compare each num to the num we've pulled out and see if it sums 2020
        for second_num in list_nums: 

            for third_num in list_nums:

                if num + second_num + third_num == 2020:

                    return num * second_num * third_num


#-------- REFACTOR 1

def find_nums(file):
    """Find three nums that sum to 2020"""

    handle = open(file)

    list_nums = []

    #add nums into list
    for line in handle:
        line = line.rstrip() # => strip any whitespace off of line
        line = int(line) # => convert to integers
        list_nums.append(line) # => add num to list 

    #find nums that sum to 2020

    #loop over list of nums
    for num in list_nums: 

        #compare each num to the num we've pulled out and see if it sums 2020
        for second_num in list_nums: 

            if num + second_num  == 2020:

                third_num = 2020 - (num + second_num)

                return hird_num