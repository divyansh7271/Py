
def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)


# 4 2 2 8 3 3 1          - array
# 0 1 2 3 4 5 6 7 8 9 10 - index_of_count
# 0 1 2 2 1 0 0 0 1 0 0  - count
# 0 1 3 5 6 6 6 6 7 7 7  - cummulative count