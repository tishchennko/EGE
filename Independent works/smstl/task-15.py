def f(A):
    for x in range(1, 1000):
        a_100 = A % 100
        x_100 = 100 % x
        f = ((A + x) > (700 - A)) and ((a_100 + x_100) > 50)
        if f != 1:
            return 0
    return 1

for A in range(1, 10_000):
    if f(A) == 1:
        print(A)
        break