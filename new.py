class Item:

    def __init__(self,weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.cost = value // weight
    def __lt__(self, other):
        return self.cost < other.cost

class GreedyKnapsack:

    @staticmethod
    def knapsack(weight, value, capacity):

        profit = 0
        items = []
        for i in range(len(weight)):
            items.append(Item(weight[i], value[i], i))

        items.sort(reverse = True)

        for i in items:
            wt = i.weight
            val = i.value

            if capacity - wt >= 0:
                profit += val
                capacity -= wt

            else:
                frac = capacity / wt
                capacity = int(capacity - wt * frac)
                profit += val * frac
                break
        
        print("Total profit : ",profit)


weight = [10, 40, 20, 30]
value = [60, 40, 100, 120]
capacity = 50

print('Weight : ',weight)
print('Value : ',value)

GreedyKnapsack.knapsack(weight, value, capacity)