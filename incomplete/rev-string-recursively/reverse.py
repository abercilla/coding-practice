"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
    

    if len(astring) < 2:
        return astring

    #astring[-1] is always holding the last letter from the last iteration, nested return statements
    return astring[-1] + rev_string(astring[:-1]) 




    
    astring = 'porcupine'
    return 'e' + 'porcupin' 

        astring = 'porcupin'
        return 'e' + ('n' + 'porcupi')
    
            astring = 'porcupi'
            return 'e' + 'n' + ('i' + 'porcup')

  






    #if astring is blank or one char, return astring as is  
      
    #     If not list:
    #         Return counter
    if astring == "":
        return " ".join(reversed_astring_list)

    if len(astring) <= 1: #leave this #if we want to return the reversed word, this will never be the right exit strategy??
        return astring # => ("enipucrop") 
     
    #make a list out of string 
    astring_list = list(astring) ['e' 'p', 'o', 'r', 'c', 'u', 'p', 'i', 'n', 'e']

    # #create an empty list
    # reversed_astring_list = []
    #atring_list[::-1]



    #index into last char of astring
    reversed_astring_list.apppend(astring_list[-1]) ['p', 'o', 'r', 'c', 'u', 'p', 'i', 'n', 'e'] 
                                                    ['e'] 
    

    #reversed_astring_list.append(astring_list[:-1])

    
    astring_list.pop() ['e'] ['p', 'o', 'r', 'c', 'u', 'p', 'i', 'n'] #slice of list 
    #remove last char, add to beginning of string

    return rev_string(" ".join(astring_list), reversed_astring_list) ("eporcupin") 


    
    Def add_numbers(list, counter = 0):
        
        If not list:
            Return counter

        Counter += List[-1] 
        list.pop()
        Return add_numbers(list, counter)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
