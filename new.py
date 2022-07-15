
from math import log2
import random
import matplotlib.pyplot as plt
import time
from math import log2
def heapify(arr, n, i):
    largest = i

    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    else:
        largest = i

    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n , largest)

def heapsort(arr):

    n = len(arr)

    start_index = n//2 - 1

    for i in range(start_index, 0-1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]

          heapify(arr, i, 0)
    
'''
#Test
array = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

heapsort(array)

print(array)
'''

arr = []
ext = []
s = []
time_complexity = []

for size in range(3000, 33000, 3000):

    s.append(size)
    arr = [x for x in range(1, size+1)]
    random.shuffle(arr)

    start = time.time_ns_ns()
    heapsort(arr)
    end = time.time_ns_ns()

    total_time = end - start
    ext.append(total_time)

    tc = size * (log2(size))*340
    time_complexity.append(tc)

    # print('Sorted array: {}'.format(array))

plt.plot(s, ext, label = "Heapsort")
plt.plot(s, time_complexity, label = "nlogn")
plt.xlabel("size")
plt.ylabel("time")
plt.title("Heapsort")
plt.legend()
plt.show()