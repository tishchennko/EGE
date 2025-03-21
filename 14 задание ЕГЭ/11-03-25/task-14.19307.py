

n = 15625**16 - (3125**3 * 25 ** 19) + 625 ** 4 - 2005
res = ''
while n:
    res += str(n % 5)
    n //= 5
print(res.count('0'))
#38

