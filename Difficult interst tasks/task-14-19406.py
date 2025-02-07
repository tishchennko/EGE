from string import digits, ascii_uppercase

alph =  digits + ascii_uppercase

for x in alph[1:35]:
    num1 = int(f'6{x}QR{x}', 35)
    num2 = int(f'{x}59SH', 35)
    num3 = int(f'PH{x}69YW', 35)
    num = num1 + num2 + num3
    count = [0] * 10
    for i in str(num):
        count[int(i)] += 1
    digit = 9 - count[::-1].index(max(count))
    if num % digit**2 == 0:
        print(num // digit**2)

