with open('24_1866.txt') as file:
    data = file.readline()

while 'ad' in data or 'da' in data:
    data = data.replace('ad', 'a d').replace('da', 'd a')

data = data.split()

print(len(max(data, key = len)))
