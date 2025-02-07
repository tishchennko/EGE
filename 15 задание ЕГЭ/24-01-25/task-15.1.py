def check(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x * y < A) or (x < y) or (9 < x)
            if f != 1:
                return 0
    return 1


for A in range(0, 10_000):
    if check(A) == 1:
        print(A)
        break