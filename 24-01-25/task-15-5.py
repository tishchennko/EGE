def check(A):
    for x in range(1, 10000):
        f = (x & A == 0) or (x & 37 != 0) or (x & 12 != 0)
        if f != 1:
            return 0
    return 1


for A in range(1, 10000):
    if check(A) == 1:
        print(A)
