def check(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = not((x < 7) or (y >= 3*x + A - 20) or (x >= 34)  or (y < 121))
            if f:
                return 0
    return 1


for A in range(0, 10_000):
    if check(A) == 1:
        print(A)
