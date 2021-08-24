def max_sub_array_of_size_k(k, arr):
    #time compelxity = O(N*k) NOT O(n^2) because we're not iterating through the same array twice

  #what to do if k is same size as len(list)
  #what if k is negative or zero

  #initialize a current_max_sum variable
  current_max_sum = 0
  
  #loop over the list and sum the nums in subarray of len(k)
  for idx in range(0, len(arr)-k):
    current_sum = 0 #initialize current_sum every time we loop over another subarray
    for i in range(idx, idx + k):
      current_sum += arr[i] #add all nums from subarray arr[i] - arr[idx + k] to current_sum
    #compare max sum to current sum of current subarray
    if current_sum > current_max_sum:
      current_max_sum = current_sum  #keep track of the max sum we've seen so far

  
  #once we loop through the list, return max_sum that we've tracked
  return current_max_sum
