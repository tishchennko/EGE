from fnmatch import fnmatch

for i in range(2023 - 2023 % 2023, 10 **9, 2023):
    s = str(i)
    if fnmatch(s, '20*23'):
        if sum(map(int, s)) % 7 == 0 and sum(map(int, s)) < 20:
            print(s)