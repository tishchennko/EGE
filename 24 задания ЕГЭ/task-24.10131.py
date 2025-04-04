with open('24_10131.txt') as file:
    s = open('24_10131.txt').readline()

p = {}
c = mx = 0

for i in range(len(s)):

    c += {'A': 1, 'B': -1}.get(s[i], 0)

    if c == 0:
        mx = i + 1

    mx = max(mx, i-p.get(c, 10**50))

    p[c] = p.get(c, i)

print(mx)