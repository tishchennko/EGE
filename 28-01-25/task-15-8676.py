def f(B):
    for x in range(1, 1000):
        f = ((x&500 != 0) and (x&200 == 0)) <= (x&B != 0)
        if f != 1:
            return 0
    return 1

for B in range(0, 1000):
    if f(B) == 1:
        print(B)