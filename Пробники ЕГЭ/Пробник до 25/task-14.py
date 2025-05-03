ans = []
for x in range(2, 2026):
    s = 5 ** 2025 + 5 ** 200 - x
    res = ''
    while s:
        res += str(s % 5)
        s //= 5
    ans.append([res.count('4'), x])
print(max(ans))

