def f(A):
    for x in range(1, 1000):
        x_10 = (x % 10 == 0)
        x_26 = (x % 26 == 0)
        f = ((x_10) and (x_26) and (x >= 300)) <= (A <= x)
        if f != 1:
            return 0
    return 1

for A in range(0, 1000):
    if f(A) == 1:
        print(A)