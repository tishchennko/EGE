def check(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x + y <= 22) or (y <= x - 6) or (y >= A)
            if f != 1:
                return 0
    return 1

for A in range(0, 10_000):
    if check(A) == 1:
        print(A)



