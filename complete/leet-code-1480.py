class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        start = 0
        end = 1
        
        sums = [nums[0]]
        
        while end <= len(nums) - 1: 
            window_sum = sum(nums[start:end + 1])  
            end +=1 
            sums.append(window_sum)
            
        return sums
    
    