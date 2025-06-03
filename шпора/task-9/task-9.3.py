def f1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2) == 2 and cnt.count(1) == 4

def f2(arr):
    nepov = [i for i in arr if arr.count(i) == 1]
    pov = [i for i in arr if arr.count(i) > 1]
    return pov[0] >= sum(nepov) / 4


with open('09_9778 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, val in enumerate(data, start=1):
    if f1(val) and f2(val):
        print(pos)
        break