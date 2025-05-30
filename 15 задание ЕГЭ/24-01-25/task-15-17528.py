A = 0
f_usl = 1
for x in [k * 0.25 for k in range(-10000, 10000)]:
     P = 15 <= x <= 40
     Q = 21 <=  x <= 63
     f = P <= ((Q and (not A)) <= (not P))
     if f != f_usl:
         print(x)