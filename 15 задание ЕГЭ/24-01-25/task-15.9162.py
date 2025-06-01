def f(a, b, c):
    if a * b > c :
        return 1
    return 0

def check(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            n = (not f(x, y, A + 13)) <= f(28, y, 520) or f(x, 25, 800)
            if n != 1:
                return 0
    return 1

for A in range(-100, 100):
    if check(A) == 1:
        print(A)