N = 49**7 + 7**20 - 28
c = 0
while N:
    if N % 7 == 6:
        c += 1
    N //= 7
print(c)