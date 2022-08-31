
import time
import matplotlib.pyplot as plt
import random

def countingSort(array):
    size = len(array)
    output = [0] * size
    mx = max(array) + 1
    count = [0] * mx
    # print(f"{mx} ->max and {size} ->size")

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, mx):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

if __name__ == '__main__': 
    array = []
    exe_mer = []
    c = []    
    for j in range(1,21): 
        
        with open('input.txt','w') as f:
            for i in range(1,j*1001):
                f.write(str(random.randint(8*i,10*i))) 
                f.write("\n")
        
        with open('input.txt','r') as f:
            content = f.readlines()
        
        count = 0

        for val in content:
            array.append(int(val)) 
            count += 1 
        
        start = time.perf_counter_ns()
        countingSort(array)
        end = time.perf_counter_ns()
        
        c.append(count)
        exe_mer.append((end - start))
     
    
    l = [x*4000 for x in c]
    plt.plot(c,l)
    plt.plot(c,exe_mer)
    plt.xlabel('No of inputs')
    plt.ylabel('Time taken (in ns)')
    plt.legend(["n","Counting-sort"])
    plt.title("Counting_sort")
    plt.show()
