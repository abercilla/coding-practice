"""Complete first challenge for Advent Exercise"""

## MEMORIZE THIS ALGO!

#can refactor this to take in target_num as a parameter and make more dynamic

#find two numbers that sum to 2020
def find_nums(file):
    """Find two nums that sum to 2020"""

    handle = open(file)
    #print(handle)

    
    list_nums = []

    #add nums into list
    for line in handle:
        line = line.rstrip() # => strip any whitespace off of line
        line = int(line) # => convert to integers
        list_nums.append(line) # => add num to list 

    #loop over list of nums and for each num, sum to rest of nums in list, then remove num from ilist 
    for num in list_nums: 

        #compare each num to the num we've pulled out and see if it sums 2020
        for num_to_compare in list_nums: 

            if num + num_to_compare == 2020:

                return num, num_to_compare


def multiply_nums(num1, num2):
    """Multiple nums that sum to 2020"""

    return num1 * num2