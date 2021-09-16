def max_sub_array_of_size_k(k, arr):
    """Sliding window solution for same problem"""

    max_sum = 0
    window_sum = 0
    window_start = 0 

    for window_end in range(len(arr)):#arr = [2, 1, 5, 1, 3, 2], range = (0, 1, 2, 3, 4, 5 ) #loop over by index 
        window_sum += arr[window_end] #add each subsequent num to sum
        
        #SLIDE THE WINDOW if we've hit size of window k
        if window_end >= k-1: 
            max_sum = max(max_sum, window_sum) #change the max to be whatever is highest so far  #5
            window_sum -= arr[window_start] #subtract the elemnt going out #5-1 = 4
            window_start += 1 #slide the window ahead #2

        return max_sum




Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

