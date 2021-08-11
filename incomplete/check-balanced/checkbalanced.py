"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False

Imbalanced Six:

    1
   / \
  2   6
 / \   
3   4
   /
  5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False
"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?"""
        
        def _num_descendants(node):
            """Returns number of descendants or None if already imbalanced."""

            if not node:
                # Our base case: we're not a real node (child of a leaf)
                return 0

            # Get descendants on left; if "None", already imbalanced---bail out
            left = _num_descendants(node.left) 
            #print(f'left is {left}')

            if left is None:
                return None

            # Get descendants on right; if "None", already imbalanced---bail out
            right = _num_descendants(node.right)
            #print(f'right is {right}')

            if right is None:
                return None

            if abs(left - right) > 1:
                # Heights vary by more than 1 -- imbalanced!
                return None

            # Height of this node is height of our deepest descendant + ourselves
            return max(left, right) + 1

        return _num_descendants(self) is not None

        # root = self.data
        # left_distance = 0 
        # right_distance = 0
        
        # if not root: 
        #     return True
             
        # if self.left is None and self.right is None: 
        #     if (left_distance - right_distance) <= 1 or (right_distance - left_distance) <= 1:
        #         return True 
            
        # if self.left is None and self.right is not None: #we start moving on right branch
        #     is_balanced(self.right)
        #     right_distance += 1
        # elif self.left is not None and self.right is None: #we start moving on left branch 
            
        #     is_balanced(self.left)
        # else: #self.left AND self.right are not None
            

        # if self.left != None:
        #     left_distance += 1 # 1 - 2 
        #     is_balanced(self.left) #2 - 3  

        # if self.right != None:
        #     right_distance += 1
        #     is_balanced(self.right)
        
        # #traverse down by self.left until None 
        # while (self.left != None ) or (self.left.right.left != None):
                





if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED! GO GO GO!\n")
