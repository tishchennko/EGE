from string import *

alf = digits + ascii_lowercase

for x in alf[:25]:
    n1 = int(f'A4{x}7F2', 25)
    n2 = int(f'N{x}G5{x}H', 25)
    n3 = int(f'74{x}M26', 25)
    n4 = n1 + n2 + n3
    if n4 % 24 == 0:
        print(n4 // 24)