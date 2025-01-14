
A = 0
x = 1

for i in[k * 0.25 for k in range(-10000, 10000)]:
    P = 15 <= i <= 40
    Q = 21 <= i <= 63
    f = P <= (((Q) and (not A)) <= (not P))
    if f != x:
        print(i)
