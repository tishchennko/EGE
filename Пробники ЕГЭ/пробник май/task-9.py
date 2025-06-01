def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(2) == 4 and cnt.count(1) == 2:
        return 1
    else:
        return 0

def f2(arr):
    pov = [i for i in arr if arr.count(i) > 1]
    nepov = [i for i in arr if arr.count(i) == 1]
    a = 1
    for i in nepov:
        a *= i
    if max(pov) ** 2 > a:
        return 1
    else:
        return 0


with open('9_18134.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)
