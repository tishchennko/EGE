with open('24_8510.txt') as file:
    data = file.readline()

data = data.replace('N', 'O').replace('P', 'O')
while 'OO' in data:
    data = data.replace('OO', 'O O')

data = data.split()
print(len(max(data, key = len)))