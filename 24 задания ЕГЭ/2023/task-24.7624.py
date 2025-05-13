with open('24_7624.txt') as file:
    data = file.readline()

data = data.replace('X', 'Z').replace('Y', 'Z')
while 'ZZ' in data:
    data = data.replace('ZZ', 'Z Z')

data = data.split()
print(len(max(data, key = len)))
