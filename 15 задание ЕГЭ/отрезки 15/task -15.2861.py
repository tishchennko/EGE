from itertools import *

def f(x):
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    A = A1 <= x <= A2
    return Q <= ((P == Q) or ((not P) <= A))

ans = []
line = [x / 10 for x in range(69 * 10, 114 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))