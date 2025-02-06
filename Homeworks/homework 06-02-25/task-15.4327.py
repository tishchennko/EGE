
from itertools import *

def f(x):
    P = 5 <= x <= 40
    Q = 41 <= x <= 54
    R = 6 <= x <= 53
    A = A1 <= x <= A2
    return ((not P) <= Q) and R and (not A)

ans = []
line = [x / 10 for x in range(5 * 10, 54 * 10)]

for A1, A2  in combinations(line, 2):
    if all(not f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))
