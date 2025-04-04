from itertools import permutations


def f_1(arr):
    return max(arr) < sum(arr) - max(arr)

def f_2(arr):
    return max(arr) + min(arr) == sum(arr) - max(arr) - min(arr)

def f_3(arr):
    for i in permutations(arr):
        if sum(i[2:]) == sum(i[:2]):
            return True
    return False

with open('9_4589.txt') as file:
    data= [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f_1(i) and f_2(i) and f_3(i):
        cnt += 1
print(cnt)













