A = 1
f_usl = 1
for x in[k * 0.25 for k in range(-1000,1000)]:
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    f = (A <= P) or Q
    if f == f_usl:
        print(x)