 
import math
import time
import matplotlib.pyplot as plt
import random

# Function to find the partition position
def partition(array, low, high):
  
  # Choose the rightmost element as pivot
  pivot = array[high]
  
  # Pointer for greater element
  i = low - 1
  
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
  
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
  
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  
  # Return the position from where partition is done
  return i + 1

# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
  
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
  
    # Recursive call on the left of pivot
    quick_sort(array, low, pi - 1)
  
    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, high)
  
    
if __name__ == '__main__': 
    arr = []
    exe_mer = []
    c = []    
    for j in range(0,11): 
        
        with open('input.txt','w') as f:
            for i in range(0,j*5000):
                f.write(str(random.randint(i,1000*i))) 
                f.write("\n")
        
        with open('input.txt','r') as f:
            content = f.readlines()
        
        count = 0

        for val in content:
            arr.append(int(val)) 
            count += 1 
        
        start = time.time_ns()
        quick_sort(arr,0,len(arr)-1)
        end = time.time_ns()
        
        c.append(count)
        exe_mer.append((end - start))
     
    
    l = [(math.log2(x+1)*x)*1300 for x in c]
    plt.plot(c,l)
    plt.plot(c,exe_mer)
    plt.xlabel('No of inputs')
    plt.ylabel('Time taken (in ns)')
    plt.legend(["nlog(n)","Quick-Sort"])
    plt.title("Quick-Sort")
    plt.show()