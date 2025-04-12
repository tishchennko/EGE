ans = []
for x in range(1, 112):
    a = x * 111 ** 3 + 3 * 111 ** 2 + 2 * 111 + 1
    b = 1 *  211 ** 3 + 7 * 211 ** 2 + x * 211 + 4
    c = a + b
    if c % 111 == 0:
        ans.append([c // 111, x])
print(ans)