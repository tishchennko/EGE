with open('24_4602.txt') as file:
    data = file.readline()

for i in 'AO':
    data = data.replace(i, 'A')
for i in 'BCD':
    data = data.replace(i, 'B')

data = data.replace('BA', '*')
for i in 'ABCDO':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key = len)))