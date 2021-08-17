"""Calculator

    >>> calc("+ 1 2")  # 1 + 2 
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3) # (9+ 2) * 3 #(* 3 + 2 9)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""
def calculateNums(char1, char2, operation):
    """perform calculations"""

    if operation == "+":
        return char1 + char2
    
    if operation == "-":
        return char1 - char2

    if operation == "/":
        return char1 / char2

    if operation == "*":
        return char1 * char2 

def calc(s):
    """Evaluate expression."""

    operations = ["+", "-", "/", "*"]
    stack = [] 
    chars = s.split(" ") # list of strings so need to change to ints

    #loop over input (s) in reverse
    for char in chars[::-1]:
        stack.append(char)
        #print(stack)
        if char in operations:
            
            #put char sin stack and current char in helper function and store result in a variable
            output = calculateNums(int(stack[1]), int(stack[0]), char) 
            
            # print(int(stack[1]), int(stack[0]))
            # print(output)

            #empty stack then append output
            stack = []
            stack.append(output)

    return int(stack[0])
        
#--------------KAVYA'S SOLUTION
    # split the string at spaces and make a list
    # s = s.split()
    # # create an empty 'stack' list to add items to as you pop them from the end of s
    # stack = []
    # # create list of operators to compare to
    # operators = ['+','-','*','/']
    # #loop over chars in s from the back and add to the stack, until you find an operator
    # for char in reversed(s):
    #     if char not in operators:
    #         stack.append(char)
    #     else:
    #         # once operator is found, pop the most recent two items from stack and apply operation func
    #         a = int(stack.pop())
    #         b = int(stack.pop())
    #         x = char
    #         # add that new value to stack. 
    #         stack.append(operation(a, b, x))
    # # once loop is complete, stack should just be one string
    # return int(stack[0])
 


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
