def f(A):
    for x in range(1, 100):
        x_7 = x % 7 == 0
        x_13 = x % 13 == 0
        f = ((not x_7) and x_13) <= (x > A - 40)
        if f != 1:
            return 0
    return 1

ans = []
for A in range(1, 100):
    if f(A) == 1:
        ans.append(A)
print(max(ans))
#52