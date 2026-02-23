import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
m = 1
k = 40 
f = 0.025

t = np.arange(0,20,dt)
x = np.zeros(len(t))
v = np.zeros(len(t))

x[0] = 0.01
x[1] = 0.01

for n in range(1, len(t)-1):
    v[n] = (x[n] - x[n-1])/dt

    if v[n] < 0:
        F = f
    elif v[n] > 0:
        F = -f
    else:
        F = 0
    
    x[n+1] = ((dt**2)/m)*(F-k*x[n]) + 2*x[n] - x[n-1]


anal_x = np.zeros(len(t))
anal_x[0] = 0.01
for n in range(len(t)-1):
    anal_x[n] = 0.01*(np.cos(np.sqrt(k/m)*t[n])+np.sin(np.sqrt(k/m)*t[n]))

plt.plot(t,x)
plt.plot(t,anal_x)
plt.savefig("graph.png")
plt.show()