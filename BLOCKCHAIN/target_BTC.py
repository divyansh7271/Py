
def newDifficulity(D,x):
    ratio = x/(20160*60)
    new_D = D*ratio
    print(new_D)
    
if __name__ == "__main__":     
    D = int(input())
    x = int(input("Avg Time for 1 Block Creation (Sec): "))*2016
    newDifficulity(D,x)