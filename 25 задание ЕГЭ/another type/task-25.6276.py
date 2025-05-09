
from fnmatch import fnmatch

for i in range(2023, 10 ** 10, 2023):
    i = str(i)
    if fnmatch(str(i), '1?1?1?1*1'):
        if sum(map(int, i)) == 22:
            print(i)
