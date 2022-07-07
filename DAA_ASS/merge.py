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

if __name__ == '__main__': 
    arr = []
    exe_mer = []
    c = []    
    for j in range(0,21): 
        
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
        
        start = time.perf_counter_ns()
        mergesort(arr)
        end = time.perf_counter_ns()
        
        c.append(count)
        exe_mer.append((end - start))
     
    
    l = [(math.log2(x+1)*x)*1300 for x in c]
    plt.plot(c,l)
    plt.plot(c,exe_mer)


    plt.xlabel('No of inputs')
    plt.ylabel('Time taken (in ns)')
    plt.legend(["nlog(n)","Merge-Sort","n^2"])
    plt.title("Merge-Sort")
    plt.show()
