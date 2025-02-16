def f(A):
    for x in range(90, 101):
        f = (not(x & 79 == 0)) and ((x & 31 == 0) <= (not(x & A == 0)))
        if f != 1:
            return 0
    return 1

for A in range(0, 1000):
    if f(A) == 1:
        print(A)
        break
#32
