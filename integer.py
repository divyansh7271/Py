import math
import time
import random
from unittest import result
import matplotlib.pyplot as plt
from numpy import append
MAXSIZE = 900
STEPS = 90

def fitlen(x, y):
    """ make x, y to become same length. 
    x and y are string, binary shape.  """
    m, n = len(x), len(y)
    if (m < n):
        x = '0' * (n - m) + x
    else:
        y = '0' * (m - n) + y
    return x, y

def add(x, y):
    x = int(x,2)
    y = int(y,2)
    result = str(bin(x+y))[2:]
    return result


def multiply(x, y):
        """ given x and y are string, binary values.
        returns multiplied value as a integer. """
        x, y = fitlen(x, y)
        n = len(x)
        if n == 0: return 0
        if n == 1: return int(x) & int(y)

        # len(xl): n // 2, len(xr): (n - n // 2)
        xl, xr = x[:n // 2], x[n // 2:]
        yl, yr = y[:n // 2], y[n // 2:]

        # each term is a integer.
        p1 = multiply(xl, yl)
        p2 = multiply(xr, yr)
        p3 = multiply(add(xl, xr), add(yl, yr))
        return p1 * (1 << 2 * (n - n // 2)) + (p3 - p1 - p2) * (1 << (n - n // 2)) + p2

n = []
et = []
# n2_x = []
# n2_y = []
n16_x = []
n16_y = []
for i in range(0,MAXSIZE+1, STEPS):
    x = str(bin(random.randint(i, 10**i)))[2:]
    y = str(bin(random.randint(i, 10**i)))[2:]
    start = time.perf_counter_ns()
    z = multiply(x, y)
    end = time.perf_counter_ns()
    n.append(len(x))
    executionTime = end - start
    et.append(executionTime)
    # n2_x.append(len(x))
    # n2_y.append(i*i)
    n16_x.append(len(x))
    n16_y.append((i**(1.6))*22000)
# print(n)
    # print(et)
# # print(n2_y)
# print(n16_y)

plt.plot(n, et, label="Integer Multiplication")
# plt.plot(n2_x, n2_y, label="n^2")
plt.plot(n16_x, n16_y, label="n^1.6")
plt.xlabel('Size(n)')
plt.ylabel('Time Taken')
plt.title('Integer Multiplication')
plt.legend()
plt.show()    

# x = int(input())
# y = int(input())

# x = str(bin(x))[2:]
# y = str(bin(y))[2:]

# print("Product of ",x,y," = ",multiply(x,y))

