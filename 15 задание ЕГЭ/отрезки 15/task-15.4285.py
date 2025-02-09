from itertools import *

def f(x):
    P = 25 <= x <= 240
    Q = 175 <= x <= 300
    R = 270 <= x <= 340
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)

ans = []
line = [x / 10 for x in range(24 * 10, 345 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))