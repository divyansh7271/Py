import time

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
    with open('input.txt','r') as f:
        content = f.readlines()
    count = 0   
    for val in content:
        print(val, end=" ")
        arr.append(int(val)) 
        count += 1
    start = 1000*time.time()    
    mergesort(arr)
    end = 1000*time.time()
    for i in arr:
        print(i, end=" ")
    print()
    print('execution time : ', round((end-start),5))
    print('total : ', count)



