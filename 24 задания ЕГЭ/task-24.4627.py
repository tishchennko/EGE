with open('24_4627.txt') as file:
    data = file.readline()

data = data.replace('NPO', '*').replace('PNO', '*')
for i in 'NOP':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key = len)))

