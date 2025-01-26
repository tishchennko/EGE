def check(A):
    for x in range(1, 10 ** 6):
        x_2 = (x % 2 == 0)
        x_3 = (x % 3 == 0)
        f = ((x_2) <= (not(x_3)))or (x + A >= 80)
        if f != 1:
             return 0
    return 1

for A in range(1, 1000):
    if check(A) == 1:
        print(A)
        break
