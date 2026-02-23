def find_pi(N):
    import random
    a = 1
    b = 1
    N = N
    counter = 0

    def f(x,y):
        return x**2 + y**2 

    for n in range(N):
        x = random.uniform(-a,a)
        y = random.uniform(-b,b)
        v = f(x,y)

        if v <= 1:
            counter += 1

    pi = 4*(counter/N)
    return print(pi)

find_pi(10**5)