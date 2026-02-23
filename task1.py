def f(x):
    return x**3 + x**2

def integral(a,b,n,x,w):
    sum = 0
    for t in range(n):
        sum += w[t]*f(x[t])

    int = (b-a)*sum
    return print(int)

integral(0,10,2,(0,10),(0.5,0.5))
integral(0,10,3,(0,5,10),(1/6,2/3,1/6))
integral(0,10,2,(0,5.7735),(0.5,0.5))