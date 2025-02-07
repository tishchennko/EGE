A = 1
f_usl = 1
for x in[k * 0.25 for k in range(-1000,1000)]:
    P = 23 <= x <= 45
    Q = 34 <= x <= 56
    f = (not A) or (not P) and Q
    if f == f_usl:
        print(x)