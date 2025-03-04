from fnmatch import *

chet = '02468'
nechet = '13579'
for i in range(123405 - 123405 % 21025, 21025):
    if fnmatch(str(i), '123*4?5'):
        if i % 21025 == 0 and (i for i in chet) == (i for i in nechet):
            print(i, i // 2658)
