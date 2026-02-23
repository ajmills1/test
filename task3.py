import random
import numpy as np

def f(x,y):
    return x**2 + y**2 

a = 1
b = 1
N = 10**6
counter = 0

for n in range(N):
    x = random.uniform(-a,a)
    y = random.uniform(-b,b)
    v = f(x,y)

    if v <= 1:
        counter += 1

pi = 4*(counter/N)
print(pi)