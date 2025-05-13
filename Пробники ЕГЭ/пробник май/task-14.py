from string import *

alf = digits + ascii_uppercase
ans = []
for x in alf[:16]:
    for y in alf[:16]:
        f1 = int(f'27A{x}23', 16)
        f2 = int(f'8{y}E5D2', 16)
        f3 = f1 + f2
        if f3 % 5 == 0:
            ans.append(int(x, 16) + int(y, 16))
print(max(ans))