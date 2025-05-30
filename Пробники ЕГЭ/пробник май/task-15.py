from itertools import *

def f(x):
    P = 254 <= x <= 800
    Q = 410 <= x <= 823
    A = A1 <= x <= A2
    return (P and (not A)) <= Q

ans = []
line = [x/ 10 for x in range(254 * 10, 823 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))