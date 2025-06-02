ans = []
for N in range(1, 100_000):
    r = bin(N)[2:]
    if int(r) % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if N <= 12:
        ans.append(r)
print(max(ans))