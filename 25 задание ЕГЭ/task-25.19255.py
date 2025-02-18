from fnmatch import *

for i in range(5401037 - 5401037 % 18579, 10 ** 10, 18579):
    if fnmatch(str(i), '54?1?3*7'):
        if i % 18579 == 0:
            print(i, i // 18579)