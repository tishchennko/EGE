def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(2) == 2 and cnt.count(1) == 4:
        return 1
    return 0

def f2(arr):
    pov = [i for i in arr if arr.count(1) > 1]
    nepov = [i for i in arr if arr.count(i) == 1]
    if max(pov) ** 2 > nepov[0] * nepov[1] * nepov[2] * nepov[3]:
        return 1
    return 0

with open('') as file:
    data = [list(map(int, i.split())) for i in file]
