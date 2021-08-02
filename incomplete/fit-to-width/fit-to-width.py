"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    #break string into words
    words = string.split(" ")
    print(words)
    #current_line = []

    
    # #as long as the current_line list is under or equal to our given limit
    # while len(current_line) <= limit: 
        
    #     #loop over words list 
    #     for word in words: 

    #         #add the current word to current_line
    #         current_line.append(word)


    # print(current_line)



    #         if len(word) == limit: 
    #             current_line.append(word)
    #             continue

    #         if len(word + 1) <= limit: 
    #             current_line.append(word)



    # #grab characters until we hit char limit


    # # print characters 

    # #pop those characters out of the list



    current_line = ""

    current_line_list = []

    end_list = []
    #store words in list, each item is a string, append to string in current ele as long as len is still less than limit 

    #as long as we have a list of words to pull from
    #while len(words) > 0: 

    #while len(words) > 0: 

    #while len(current_line) <= limit:  #=> ('Hello, world! I love Python and Hackbright') words = ['Hello,', 'world!', 'I', 'love', 'Python', 'and', 'Hackbright']
        

    #loop over words list and add each word to current_line

    while len(current_line) <= limit: 

        for word in words: #['Hello']

        #if adding the current word with a space is still under the limit
        #if (len(current_line) + len(word))  <= limit: #len("") +len ("Hello") + 1 <= 10
            
            #add word to current_line   
            current_line = current_line + " " + word

            current_line_list.append(word)
            
                
            #remove that word from list after we've added it to the line
            words.pop(0)
        
    
    #if we've hit the limit of words for this line => "Hello world! I ", add list into other list
    end_list.append(current_line_list)
    
    #re initalize current_line and current_line_list
    current_line = " "

    current_line_list = []

    
    print(end_list)

    #-------------------#

    #print all lines
    # for line in end_list:

    #     print(line) 


    #-------------------#

    # #add words to string until we hit max length, then iterate through next set of words 
    # while end_list: 
        
    #     current_line = ""
        
    #     for word in words: 
            
    #         current_line = current_line + word


    


    #     current_line_length = word_length + len(current_line) 

        


    #     #if we can't add current word to current_line


    #     #once hit limit, add line to end_list 
    #     end_list.append(current_line)



    #     while len(string) < limit: 
    #     #count len of each word +1 to include a space which counts as a character
    #     #current_word = word
    #     #print(f'---- WORD = {word}-----')
    #     word_length = len(word) + 1
    #     #print(f'------WORD_LENGTH = {word_length}-----')

    #     #establish a var to see how long the end_string WOULD be if we added the current word
    #     print(f'-----TOTAL_LENGTH = {total_length}------')

    #     # #if the len of string + len of current string is still under char limit, add current word
    #     # #subtract 1 space at end of line 
    #     if (total_length - 1) < limit: 
    #         #print("----total_length is still under limit -----")
    #         if end_string == "": 
    #             end_string = end_string + word
    #         else: 
    #             end_string = end_string + " " + word
            
    #         #remove word from word_list after we add to the string
    #         #word_list.remove(word)
    

    #         #as long as total_length is under limit, print end_string
    #         #print(end_string)
            
    #         #reinitialize string
        
    #     #if we would hit the character limit for this string by adding curr word... 
    #     #even though we don't want to add the current word to the string, we want to loop through again 
    #     else: 
    #         # print(end_string)
    #         # end_string = ""
    
    #         #print(f'-------END_STRING prev line = {end_string}----')
            
    #         #end_string = ""           

    #         print(f'-------CURR WORD = {word}------')


    #print each item in array
        




    # create lists of words that are under the char limit so we can print individually [["Hello", "world!", "I"]["love"]["Python", "and"]["Hackbright"]]
    # print them as a string with spaces after each word except for the last one 



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
