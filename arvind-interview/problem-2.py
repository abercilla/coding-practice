def max_sub_array_of_size_k(k, arr):

  max_sum = 0
  start = 0
  end = k - 1
  #loop over array
  while end < len(arr):
    window_sum = sum(arr[start:end + 1])
    print("window sum")
    print(window_sum) #sum current window arr[0:2m]
    max_sum = max(window_sum, max_sum) #take max of current window sum and max_sum
    end += 1    #move both sides of the window up
    start += 1
    print("max_sum")
    print(max_sum)

  print("out of loop")
  return max_sum



  #sum all subarries of size k 
  #return the max sum 