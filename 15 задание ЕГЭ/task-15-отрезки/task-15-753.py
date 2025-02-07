A = 1
f_usl = 1
for x in[k * 0.25 for k in range(-10000,10000)]:
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    f = (P == Q) <= (not A)
    if f == f_usl:
        print(x)