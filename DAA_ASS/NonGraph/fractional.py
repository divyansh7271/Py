def fractional_knapsack(values, weights, capacity):     
    ratio = [v / w for v, w in zip(values, weights)]
    ratio.sort(reverse=True)    

    max_value = 0

    fractions = [0] * len(values)
    

    for i in range(len(ratio)):
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]

        else:
            
            fractions[i] = capacity / weights[i]
            max_value += values[i] * fractions[i]
            break

    return max_value, fractions

# weights = [10, 40, 20, 30]
# values = [60, 40, 100, 120]
# capacity = 50

capacity = int(input("Capacity: "))
print("Input weights:")
weights = list(map(int, input().split()))

print("Input prices:")
values = list(map(int, input().split()))

max_value, fractions = fractional_knapsack(values, weights, capacity)

print('Max Profit : ', int(max_value)) 
