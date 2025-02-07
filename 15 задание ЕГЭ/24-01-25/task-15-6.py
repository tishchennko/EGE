def check(A):
    for x in range(90, 101):
        f = (x&79 != 0) and ((x&31 == 0) <= (x&A != 0))
        if f != 1:
            return 0
    return 1


for A in range(0, 1000):
    if check(A) == 1:
        print(A)
        break
