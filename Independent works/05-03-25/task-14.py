from string import *

alf =  digits + ascii_uppercase

for p in range(16, 37):
    num1 = int(f'17496', p)
    num2 = int(f'91F83', p)
    num3 = int(f'D9543', p)
    num4 = num1 + num2 + num3
    if num4 % 12 == 0:
        print(int((num4 // 12)))
