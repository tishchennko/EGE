def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            for z in range(1, 1000):
                z_115 = x % 115 == 0
                y_78 = x % 78 == 0
                x_51 = x % 51 == 0
                x_a = x % A == 0
                f = (z_115 or y_78 or x_51) <= x_a
                if f != 1:
                    return 0
    return 1

for A in range(1, 1000):
    if f(A) == 1:
        print(A)
