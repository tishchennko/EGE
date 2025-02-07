def f(A):
    for x in range(1, 1000):
        f = (x & 1097 == 0) <= ((x & 2047 != 0) <= (x & A != 0))
        if f != 1:
            return 0
    return 1

for A in range(1, 10_000):
    if f(A) == 1:
        print(A)
        break