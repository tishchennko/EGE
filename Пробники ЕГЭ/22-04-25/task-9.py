def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(2) == 2:
        return 1
    else:
        return 0

def f2(arr):
    otric = [abs(i) for i in arr if i < 0]
    polozh = [i for i in arr if i > 0]
    if sum(otric) > sum(polozh):
        return 1
    else:
        return 0

with open('9_18174.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)