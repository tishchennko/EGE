
A = 0
f_usl = 0
for x in[k * 0.25 for k in range(-1000, 10000)]:
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    f = not(((not B) <= C) <= A)
    if f != f_usl:
        print(x)
