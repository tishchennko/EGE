
from fnmatch import *

for i in range(1746008 - 1746008 % 86513, 10 ** 20, 86513):
    if fnmatch(str(i), '17*46??8'):
        summ = sum(map(int, str(i)))
        if summ * .5 == int(summ ** .5):
            print(i, i // 86513)