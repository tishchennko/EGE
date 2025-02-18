from fnmatch import *

for i in range(30157-30157 % 2023, 10 ** 8, 2023):
    if fnmatch(str(i), '3?1*57'):
        if i % 2023 == 0:
            print(i, i // 2023)