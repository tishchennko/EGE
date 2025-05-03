ans = []
for N in range(1, 100_000):
    s = bin(N)[2:]
    s = s.replace('0', '*', ).replace('1', '!')
    s = s.replace('*', '1' ).replace('!', '0')
    s = '1' + s
    if s.count('1') % 2 != 0:
        s = s + '1'
    else:
        s = s + '0'
    R = int(s, 2)
    if R > 180:
        ans.append(N)
print(min(ans))

