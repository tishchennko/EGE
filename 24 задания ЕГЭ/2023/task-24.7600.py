with open('24_7600.txt') as file:
    data = file.readline()

data = data.replace('Q', 'S').replace('R', 'S')
while 'SS' in data:
    data = data.replace('SS', 'S S')

data = data.split()
print(len(max(data, key = len)))