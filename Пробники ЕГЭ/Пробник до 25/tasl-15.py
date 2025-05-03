def check(A):
    for x in range(-15, 1000):
        for y in range(-15, 1000):
            f = ((A < x) or (x**2 - 7*x + 10 > 0)) and ((A >= y) or (y**2 + 7*y + 12 > 0))
            if f != 1:
                return 0
    return 1

cnt = 0
for A in range(-15, 1000):
    if check(A) == 1:
        cnt += 1
print(cnt)

