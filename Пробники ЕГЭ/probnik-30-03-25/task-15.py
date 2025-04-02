def check(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = ((x + 2) <= 50) or (y < (x + 10)) or (x >= A)
            if f != 1:
                return 0
    return 1

for A in range(0, 1000):
    if check(A) == 1:
        print(A)