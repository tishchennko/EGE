from fnmatch import *

for i in range(10 ** 7):
    if fnmatch(str(i), '31*567?'):
        if i:
            print(i)