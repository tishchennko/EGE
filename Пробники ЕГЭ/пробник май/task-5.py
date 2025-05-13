res = set()
for R in range(100, 1001):
    N = bin(R)[2:]
    while '0' in N:
        N = N.replace('0', '')
    N = int(N, 2)
    res.add(N)
print(len(res))

