def f(A):
    for x in range(1, 1000):
        x_17 = x % 17 == 0
        B = 80 <= x <= 100
        f = x_17 <= ((not B) or (A < x + 30))
        if f != 1:
            return 0
    return 1


for A in range(1, 1000):
    if f(A) == 1:
        print(A)