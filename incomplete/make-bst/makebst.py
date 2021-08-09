"""Make a binary tree from an array.

Adapted from Cracking the Coding Interview, 6th Ed.

Given a list of sorted numbers, make a binary search tree.

Returns the root node of a new BST that is valid and balanced.

For example, for [1,2,3], this produces this tree:

   2
  / \
 1   3

    >>> tree3 = make_bst([1, 2, 3])
    >>> tree3.data
    2
    >>> tree3.left.data
    1
    >>> tree3.left.left is None
    True
    >>> tree3.left.right is None
    True
    >>> tree3.right.data
    3
    >>> tree3.right.left is None
    True
    >>> tree3.right.right is None
    True

For [1..7], this produces this perfectly-balanced tree:

        4
     /-----\
    2      6
   / \    / \
  1   3  5   7

    >>> tree7 = make_bst([1, 2, 3, 4, 5, 6, 7])
    >>> tree7.data
    4
    >>> tree7.left.data
    2
    >>> tree7.left.left.data
    1
    >>> tree7.left.right.data
    3
    >>> tree7.right.data
    6
    >>> tree7.right.left.data
    5
    >>> tree7.right.right.data
    7

When we can't make things perfectly balanced (like below), this
fills left-hand nodes before right-hand nodes.

Using a less-perfectly-even lists; e.g. [1..4]:

    3
   / \
  2   4
 /
1

    >>> tree4 = make_bst([1, 2, 3, 4])
    >>> tree4.data
    3
    >>> tree4.left.data
    2
    >>> tree4.left.left.data
    1
    >>> tree4.left.right is None
    True
    >>> tree4.right.data
    4
    >>> tree4.right.left is None
    True
    >>> tree4.right.right is None
    True

And [1..5]:

     3
    / \
   2   5
  /   /
 1   4

    >>> tree5 = make_bst([1, 2, 3, 4, 5])
    >>> tree5.data
    3
    >>> tree5.left.data
    2
    >>> tree5.left.left.data
    1
    >>> tree5.right.data
    5
    >>> tree5.right.left.data
    4

And [1..6]:

      4
   /-----\
  2       6
 / \     /
1   3   5

    >>> tree6 = make_bst([1, 2, 3, 4, 5, 6])
    >>> tree6.data
    4
    >>> tree6.left.data
    2
    >>> tree6.left.left.data
    1
    >>> tree6.left.right.data
    3
    >>> tree6.right.data
    6
    >>> tree6.right.left.data
    5

By Joel Burton <joel@hackbrightacademy.com>


              10
            /-----\
           8       12
         / \       / \
        6   9     11  14
       / \            / \
      4   7          13  16
     /\                  / \
    2  5                15  18
   /\                       /\    
  1  3                     17 19 
"""

class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_bst(nums):
    """Given a list of sorted numbers, make a binary search tree.

    Returns the root node of a new BST that is valid and balanced.
    """
    BinaryNode

    #get length of list
    if len(nums) % 2 != 0:
        data = round(len(nums)/2)
        BinaryNode(data)
    else:
        data = int(len(nums)/2) + 1
        BinaryNode(data)
    
    root = self.data 
    
    return root
    #if length is odd, self.data = middle num round(len/2)  => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] = round(len/2)
        # self.data = 4 = nums[3] = int(len/2)
        #while self.left < len(nums):  
           # self.left.left =  
        #if len(nums) > 3? :
        # self.left.data = self.data - 2  

        # self.right.data = self.data + 2
     
     #while there still nums in the list, add whatevers greater than data (4) to self.data.right and less than to self.data.left
    
    
    # self.data = round(len(nums)/2)

    # while self.left.data => 2: 
    #     self.left.data = self.data - 2
    #     self.right.data = self.data + 1
    # self.left.data = self.data - 1
    # self.right.data = self.data + 1

    # while self.right.data <= len(nums) - 1:
    #     self.right.data = self.data + 2
    #     self.left.data = self.data - 1
    # self.left.data = self.data - 1
    # self.right.data = self.data + 1
    
    #  >>> tree6.data
    # 4
    # >>> tree6.left.data
    # 2
    # >>> tree6.left.left.data
    # 1
    # >>> tree6.left.right.data
    # 3
    # >>> tree6.right.data
    # 6
    # >>> tree6.right.left.data
    # 5
    #if length is even, self.data = len/2 + 1 => [1, 2, 3, 4, 5, 6] len/2 = 3 + 1
    
    
    



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n**** ALL TESTS PASSED. YOU'RE A TREE-MASTER!\n")
