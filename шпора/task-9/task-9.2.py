def f1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2) == 4 and cnt.count(1) == 3

def f2(arr):
    return arr.count(max(arr)) == 1

with open('9_9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]


for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break
