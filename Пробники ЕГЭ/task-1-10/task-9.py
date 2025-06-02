def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(3) == 3 and cnt.count(1) == 4:
        return 1
    else:
        return 0

def f2(arr):
    res = [i for i in arr]
    res = sorted(res)
    if res:
        return 1
    else:
        return 0

with open('9_ok_11946.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if (f1(i) and not f2(i)) or (not f1(i) and f2(i)):
        cnt += 1
print(cnt)

