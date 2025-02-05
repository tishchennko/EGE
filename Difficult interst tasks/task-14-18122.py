def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 5556)[::-1]:
    n = 5 ** 150 + 5 ** 135 - x
    if convert(n, 5).count('4')== 134:
        print(int(x))
        break




