from itertools import product

alph = sorted('ЯНВАРЬ')

res = []
for pos, val in enumerate(product(alph, repeat = 5), 1):
    val = ''.join(val)
    if val[0] != 'Я' and val.count('Ь') == 1 and 'ЯЯ' not in val:
        res.append(pos)
print(max(res))