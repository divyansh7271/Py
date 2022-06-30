
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


from cmath import log, sqrt
import math
import time
import matplotlib.pyplot as plt
import random

# def heapify(arr, n, i):
# 	largest = i # Initialize largest as root
# 	l = 2 * i + 1	 # left = 2*i + 1
# 	r = 2 * i + 2	 # right = 2*i + 2

# 	# See if left child of root exists and is
# 	# greater than root
# 	if l < n and arr[largest] < arr[l]:
# 		largest = l

# 	# See if right child of root exists and is
# 	# greater than root
# 	if r < n and arr[largest] < arr[r]:
# 		largest = r

# 	# Change root, if needed
# 	if largest != i:
# 		arr[i], arr[largest] = arr[largest], arr[i] # swap

# 		# Heapify the root.
# 		heapify(arr, n, largest)

# # The main function to sort an array of given size


# def heapSort(arr):
# 	n = len(arr)

# 	# Build a maxheap.
# 	for i in range(n//2 - 1, -1, -1):
# 		heapify(arr, n, i)

# 	# One by one extract elements
# 	for i in range(n-1, 0, -1):
# 		arr[i], arr[0] = arr[0], arr[i] # swap
# 		heapify(arr, i, 0)



def buildMaxHeap(arr, n):
 
    for i in range(n):
         
        # if child is bigger than parent
        if arr[i] > arr[int((i - 1) / 2)]:
            j = i
     
            # swap child and parent until
            # parent is smaller
            while arr[j] > arr[int((j - 1) / 2)]:
                (arr[j],
                 arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],
                                           arr[j])
                j = int((j - 1) / 2)
 
def heapSort(arr, n):
 
    buildMaxHeap(arr, n)
 
    for i in range(n - 1, 0, -1):
         
        # swap value of first indexed
        # with last indexed
        arr[0], arr[i] = arr[i], arr[0]
     
        # maintaining heap property
        # after each swapping
        j, index = 0, 0
         
        while True:
            index = 2 * j + 1
             
            # if left child is smaller than
            # right child point index variable
            # to right child
            if (index < (i - 1) and
                arr[index] < arr[index + 1]):
                index += 1
         
            # if parent is smaller than child
            # then swapping parent with child
            # having higher value
            if index < i and arr[j] < arr[index]:
                arr[j], arr[index] = arr[index], arr[j]
         
            j = index
            if index >= i:
                break


# Driver code
if __name__ == '__main__': 
    arr = []
    exe = []
    c = []    
    for j in range(0,21): 
        
        with open('input.txt','w') as f:
            for i in range(0,j*1000):
                f.write(str(random.randint(0,1000000))) 
                f.write("\n")
        
        with open('input.txt','r') as f:
            content = f.readlines()
        
        count = 0

        for val in content:
            arr.append(int(val)) 
            count += 1
        arr2 = arr 
        # st = time.perf_counter_ns() 
        # bubblesort(arr2)
        # en = time.perf_counter_ns()

        start = time.perf_counter_ns()
        heapSort(arr,len(arr))
        end = time.perf_counter_ns()
        
        c.append(count)
        exe.append((end - start))
        # exe_bub.append((en - st))

    # for i in range(0,20):
    #     print(f"Count:{c[i]} ----> Execution Time:{exe[i]}")
     
    
    l = [(math.log2(x+1)*x)*3000 for x in c]
    # bub = [(x*x)*10 for x in c]
    plt.plot(c,l)
    plt.plot(c,exe)
    # plt.plot(c,bub)


    plt.xlabel('No of inputs')
    plt.ylabel('Time taken (in ns)')
    plt.legend(["nlog(n)","Heap-Sort","n^2"])
    plt.title("Heap-Sort")
    plt.show()
