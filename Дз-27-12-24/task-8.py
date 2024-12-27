from itertools import product

alph = sorted('ЯНВАРЬ')

ans = []
for pos, val in enumerate(product(alph, repeat = 5), 1):
    val = ''.join(val)
    if 'Я' not in val[0] and val.count('Ь') == 1 and 'ЯЯ' not in val:
        ans.append(pos)
print(max(ans))