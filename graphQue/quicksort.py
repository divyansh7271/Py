 
import math
import time
import matplotlib.pyplot as plt
import random

def partition(array, low, high):

  pivot = array[high]

  i = low - 1
  
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
  
      (array[i], array[j]) = (array[j], array[i])
  
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  
  return i + 1

def quick_sort(array, low, high):
  if low < high:
  
    pi = partition(array, low, high)
  
    quick_sort(array, low, pi - 1)
  
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