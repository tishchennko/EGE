from itertools import *

def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

ans = []
line = [x / 10 for x in range(25 * 10, 118 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
       ans.append(A2 - A1)
print(max(ans))