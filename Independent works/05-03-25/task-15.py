from itertools import *

def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <=A2
    return P <= ((Q and (not A)) <= (not P))

ans = []
line = [x / 10 for x in range(15 * 10, 63 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
       ans.append(A2 - A1)
print(min(ans))