from cmath import log, sqrt
import math
import time
import matplotlib.pyplot as plt
import random


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]
        
        mergesort(L)
        mergesort(R)

        i = j = k = 0


        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                k += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# def bubblesort(arr):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] > arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp            

if __name__ == '__main__': 
    arr = []
    exe_mer = []
    exe_bub = []
    c = []    
    for j in range(0,31): 
        
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
        mergesort(arr)
        end = time.perf_counter_ns()
        
        c.append(count)
        exe_mer.append((end - start))
        # exe_bub.append((en - st))

    # for i in range(0,20):
    #     print(f"Count:{c[i]} ----> Execution Time:{exe[i]}")
     
    
    l = [(math.log2(x+1)*x)*3000 for x in c]
    # bub = [(x*x)*10 for x in c]
    plt.plot(c,l)
    plt.plot(c,exe_mer)
    # plt.plot(c,bub)


    plt.xlabel('No of inputs')
    plt.ylabel('Time taken (in ns)')
    plt.legend(["nlog(n)","Merge-Sort","n^2"])
    plt.title("Merge-Sort")
    plt.show()
