import random

with open('input.txt','w') as f:
    for i in range(0,300):
        f.write(str(random.randint(0,10000))) 
        f.write("\n")
