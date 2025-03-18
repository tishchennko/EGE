from string import *

for x in range(1, 2006)[::-1]:
    n = 4 ** 163 * 5 + 12**62 - x
    res= ''
    while n:
        res += str(n % 5)
        n //= 5
    if res.count('1') < res.count('4'):
        print(x)
        break
#2000