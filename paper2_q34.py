import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x**2

def ff(x):
    return 3*x**2 + 4*x


def one_sided(x, n):
    h = np.linspace(0.1,0.0000001, n)
    dfdx = np.zeros(len(h))

    for t in range(len(h)):
        dfdx[t] = (f(x + h[t]) - f(x))/(h[t])

    error = np.zeros(len(h))

    for t in range(len(h)):
        error[t] = ff(x) - dfdx[t]
    

    plt.plot(h,dfdx)
    plt.ylabel("df/dx")
    plt.xlabel("h")
    plt.title("One-sided difference")
    plt.savefig("2q3o.png")
    plt.cla()

    plt.plot(h,error)
    plt.ylabel("absolute error")
    plt.xlabel("h")
    plt.title("Error of one-sided difference")
    plt.savefig("2q3oe.png")
    plt.cla()
  

def symmetric_difference(x, n):
    h = np.linspace(0.1,0.0000001, n)
    dfdx = np.zeros(len(h))

    for t in range(1,len(h)-1):
        dfdx[t] = (f(x + h[t]) - f(x - h[t]))/(2*h[t])
    
    error = np.zeros(len(h))

    for t in range(1,(len(h)-1)):
        error[t] = ff(x) - dfdx[t]

    plt.plot(h[1:-1], dfdx[1:-1])
    plt.ylabel("df/dx")
    plt.xlabel("h")
    plt.title("Symmetric difference")
    plt.savefig("2q3s.png")
    plt.cla()

    plt.plot(h[1:-1], error[1:-1])
    plt.ylabel("Absolute error")
    plt.xlabel("h")
    plt.title("Error in symmetric difference")
    plt.savefig("2q3se.png")
    plt.cla()


def complex_step(x, n)
one_sided(3,120)
symmetric_difference(3,120)