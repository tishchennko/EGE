from itertools import *

ans = []
for r in range(3):
    for i in product('0123456789', repeat = r):
        i = ''.join(i)
        for v in '0123456789':
            num = int('12' + i + '4' + v + '65')
            if num % 161 == 0:
                ans.append([num, num // 161])
ans = sorted(ans)
for x in ans:
    print(*x)
