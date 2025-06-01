with open('24_2421.txt') as file:
    data = file.readline()

data = data.replace('D', '*')
for i in 'ABCEF':
    data = data.replace(i, ' ')




