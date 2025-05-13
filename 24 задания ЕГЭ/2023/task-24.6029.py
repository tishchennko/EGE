with open('24_6029.txt') as fil:
    data = fil.readline()

data = data.replace('EF', '*').replace('FE', '*')
for i in 'EDF':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key = len)))
