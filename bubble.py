import time

def bubblesort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


if __name__ == "__main__":
    arr = []
    with open('input.txt','r') as f:
        content = f.readlines()
    count = 0    
    for val in content:
        count += 1
        arr.append(int(val))   
    start = 1000*time.time()
    bubblesort(arr)
    end = 1000*time.time()
    for val in arr:
        print(val, end=" ")
    print("Execution Time : ", round(end - start,5))
    print("Total : ",count)