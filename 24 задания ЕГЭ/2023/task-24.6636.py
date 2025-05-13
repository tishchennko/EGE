with open('24_6636.txt') as file:
    data = file.readline()

for i in '24':
    data = data.replace('2', '4')
for i in '135':
    data = data.replace('1', '5').replace('3', '5')

data = data.replace('45', '*')
for i in '12345':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))
