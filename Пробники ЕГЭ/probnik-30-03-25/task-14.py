ans = []
for x in range(1, 2031):
    n = 2 ** 2025 + 2 ** 2024 - 2 ** 2021 - x
    res = ''
    while n:
        res += str(n % 4)
        n //= 4
    ans.append([x, res.count('0')])
ans = sorted(ans, key=lambda x: (x[1], x[0]))
print(ans[-1])