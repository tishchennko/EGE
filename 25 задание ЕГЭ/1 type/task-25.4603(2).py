from fnmatch import fnmatch

print()

for i in range(12347 - 12347 % 141, 10**8, 141):
    if fnmatch(str(i), '1234*7'):
        if i % 141 == 0:
            print(i, i // 141)