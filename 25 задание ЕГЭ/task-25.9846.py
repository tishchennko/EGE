from fnmatch import *

for i in range(123405 - 123405 % 2025, 10 ** 8, 2025):
    if fnmatch(str(i), '12*34?5'):
        if i % 2025 == 0:
            print(i, i // 2025)
