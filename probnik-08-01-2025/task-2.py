print('x y w z f')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f = (x or (not y) and ((not x) == z) and w)
                if f == 1:
                    print(x, y, w, z, int(f))
