from fnmatch import *

for i in range(161, 10**8,161):
    if fnmatch(str(i), '12*4?65'):
        if i % 161 == 0:
            print(i, i // 161)