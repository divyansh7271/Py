
H = [0]*50
size = -1

def parent(i) :

  return (i - 1) // 2

def leftChild(i) :

  return ((2 * i) + 1)

def rightChild(i) :

  return ((2 * i) + 2)
  
def shiftUp(i) :

  while (i > 0 and H[parent(i)] < H[i]) :
    
    # Swap parent and current node
    swap(parent(i), i)
  
    # Update i to parent of i
    i = parent(i)
    
def shiftDown(i) :

  maxIndex = i
  
  # Left Child
  l = leftChild(i)
  
  if (l <= size and H[l] > H[maxIndex]) :
  
    maxIndex = l
  
  # Right Child
  r = rightChild(i)
  
  if (r <= size and H[r] > H[maxIndex]) :
  
    maxIndex = r
  
  # If i not same as maxIndex
  if (i != maxIndex) :
  
    swap(i, maxIndex)
    shiftDown(maxIndex)
    
def Insert(p) :
  
  global size
  size = size + 1
  H[size] = p
  
  # Shift Up to maintain
  # heap property
  shiftUp(size)

def Extract_Max() :
  
  global size
  result = H[0]
  
  # Replace the value
  # at the root with
  # the last leaf
  H[0] = H[size]
  size = size - 1
  
  shiftDown(0)
  return result

def Increase_key(i,p) :

  oldp = H[i]
  H[i] = p
  
  if (p > oldp) :
  
    shiftUp(i)

  else :
  
    shiftDown(i)

def Max() :

  return H[0]

def Remove(i) :

  H[i] = Max() + 1
  
  # Shift the node to the root
  # of the heap
  shiftUp(i)
  Extract_Max()

def swap(i, j) :
  
  temp = H[i]
  H[i] = H[j]
  H[j] = temp
  

if __name__ == "__main__":
    Insert(45)
    Insert(20)
    Insert(14)
    Insert(12)
    Insert(31)
    Insert(7)
    Insert(11)
    Insert(13)
    Insert(7)

    i = 0

    # Priority queue before extracting max
    print("Priority Queue : ", end = "")
    while (i <= size) :

        print(H[i], end = " ")
        i += 1

    print()

    
