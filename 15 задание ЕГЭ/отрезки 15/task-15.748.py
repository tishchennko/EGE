from itertools import *

def f(x):
    P = 44 <= x <= 49
    Q = 28 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [x / 10 for x in range(28 * 10, 53 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))