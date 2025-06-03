def f1(arr):
    return arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] > arr[6]

def f2(arr):
    return (min(arr) + max(arr)) / 2 > (sum(arr) - max(arr) - min(arr)) / 5



with open('9_21704.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break

