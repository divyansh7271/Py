import time
import matplotlib.pyplot as plt
import random

def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var   
              
def bucket_sort(input_list):
    max_value = max(input_list)
    print(max_value,end=" ")
    size = max_value/len(input_list)
    print(size)
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        print(f"j -- >{j}")
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    final_output = []    
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

# if __name__ == '__main__': 
#     exe_mer = []
#     c = []    
#     for i in range(2, 1300, 90):
#         array = []
#         for j in range(0, i):
#             temp = random.uniform(0,1)
#             array.append(temp)
            
#         start = time.perf_counter_ns()
#         bucket_sort(array)
#         end = time.perf_counter_ns()
        
#         c.append(i)
#         exe_mer.append((end - start))
     
    
#     l = [x*3000 for x in c]
#     plt.plot(c,l)
#     plt.plot(c,exe_mer)
#     plt.xlabel('No of inputs')
#     plt.ylabel('Time taken (in ns)')
#     plt.legend(["n","Bucket-sort"])
#     plt.title("Bucket_sort")
#     plt.show()
arr = []
for i in range(10):
    arr.append(random.uniform(0,1))

arr = bucket_sort(arr)
print()
print()

for val in arr:
    print(val )

