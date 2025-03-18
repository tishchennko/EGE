def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x - 3*y < A) or (y > 400) or (x > 56)
            if f != 1:
                return 0
    return 1

for A in range(1, 1000):
    if f(A) == 1:
        print(A)
        break
#54