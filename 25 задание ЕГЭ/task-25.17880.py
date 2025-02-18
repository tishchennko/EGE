from fnmatch import *

for i in range(30120145 - 30120145 % 1917, 10**10, 1917):
    if fnmatch(str(i), '3?12?14*5'):
        if i % 1917 == 0:
            print(i, i // 1917)

