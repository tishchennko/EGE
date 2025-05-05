ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    R = R + str(sum(map(int, R)) % 2)
    R = R + str(sum(map(int, R)) % 2)
    R = int(R ,2)
    if R > 253:
        ans.append(N)
print(min(ans))