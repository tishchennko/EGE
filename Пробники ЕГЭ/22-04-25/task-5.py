cnt = 0
for N in range(1, 1000000):
    R = hex(N)[2:]
    if R.count('b') % 2 == 0:
        R = '1' + R
    else:
        R = R + '1'
    R = int(R, 16)
    if 10 <= R <= 99:
        cnt += 1
print(cnt)


