def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(1) == 6:
        return 0
    else: return 1

def f2(arr):
    nechet = [3 for i in arr if i % 2 != 0]
    if nechet.count(3) == 3:
        return 1
    else:
        return 0

with open('9_6262.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if (f1(i) and not f2(i)) or (not f1(i) and f2(i)):
        cnt += 1
print(cnt)


