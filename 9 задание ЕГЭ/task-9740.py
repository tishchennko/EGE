def f1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3) == 3 and cnt.count(1) == 4

def f2(arr):
    pov = [i for i in arr if arr.count(i) > 1]
    nepov = [i for i in arr if arr.count(i) == 1]
    return sum(nepov) / 4 <= pov[0]


with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)