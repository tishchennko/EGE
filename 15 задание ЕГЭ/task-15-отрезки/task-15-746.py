A = 1
f_usl = 1
for x in[k * 0.25 for k in range(-1000,1000)]:
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    f = (A <= P) or Q
    if f == f_usl:
        print(x)

