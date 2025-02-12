from itertools import*

def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = A1 <= x <= A2
    return (Q <= (not R)) and (A) and (not P)

ans = []
line = [x / 6 for x in range(9 * 6, 42 * 6)]

for A1, A2 in combinations(line, 2):
    if all(not f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))
#20