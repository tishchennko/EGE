from string import ascii_uppercase

with open('') as file:
    data = file.readline()

for i in ascii_uppercase[2:]:
    data = data.replace(i, ' ')

data = data.split()
ans = 0
for i in data:
    i = i.rstrip('13579B').lstrip('0')
    ans = max(len(i), ans)

print(ans)
