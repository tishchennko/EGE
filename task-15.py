def check(A):
    for x in range(0, 100_000):
        x_a = (x % A == 0)
        x_10 = (x % 10 == 0)
        x_12 = (x % 12 == 0)
        f = (A < 50) and ((not x_a) <= ((x_10) <= (not x_12)))
        if f != 1:
            return 0
    return 1

for A in range(1, 100_000):
    if check(A) == 1:
        print(A)