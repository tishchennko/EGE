def f1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(1) == 5


def f2(arr):
    cnt = [1 for i in arr if i % 2 == 0]
    ans = [1 for i in arr if i % 2 != 0]
    if len(cnt) > len(ans):
        return 1
    return 0

def f3(arr):
    chet = [i for i in arr if i % 2 == 0]
    nechet = [i for i in arr if i % 2 != 0]
    if sum(chet) < sum(nechet):
        return 1
    return 0

with open('9_5489.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i) and f3(i):
        cnt += 1
print(cnt)

