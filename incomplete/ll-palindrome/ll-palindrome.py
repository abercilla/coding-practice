# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head): #[1, 2, 1, 1, 2, 1]
        """
        :type head: ListNode -> obj in list
        :rtype: bool - > return True or False
        """
    
        # slow = fast = cur = head
        # 1. slow = 2 head[1]
        #.   fast = 1 head[2]
        # while fast and fast.next:
        #.  fast = fast.next.next
        #.  slow = slow.next
        #iterate over nodes to find the end and midpoint
        #start adding second half of array to new stack until get to end of array
        # once you have your midpoint (slow pointer):
        # stack = [slow.val]
        # while(slow.next):
        #.  slow = slow.next
        #.  stack.append(slow.val)
        # cur = [1,2,1,2, 1], stack for second half = [ 2, 1]
        #keep pointer to midpoint so we can compare first half of arry to new stack
        #pop off items from stack as we compare
        # while(stack){
        #  if (stack.pop() != cur.val)
        #     return False
        #  cur = cur.next
        # }

    #get tail of a linked list
    #loop over all .next values starting with head.next until .next = None 