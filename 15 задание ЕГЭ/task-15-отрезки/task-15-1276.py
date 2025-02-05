A = 1
f_usl = 1
for x in[k * 0.25 for k in range(-1000,1000)]:
    P = 15 <= x <= 33
    Q = 35 <= x <= 48
    f = (A and (not Q)) <= (P or Q)
    if f == f_usl:
        print(x)