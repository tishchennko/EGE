def f(A):
    for x in range(1, 1000):
        f = ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x&58 == 0))
        if f == 1:
            return 0
    return 1

for A in range(43, 56):
    if f(A) == 1:
        print(A)
