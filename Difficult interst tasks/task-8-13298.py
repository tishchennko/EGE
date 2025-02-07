from itertools import product

alph = sorted('ПРИВЫЧКА')

ans =[]
for pos, val in enumerate(product(alph, repeat = 5), 1):
    val = ''.join(val)
    if val.count('П') == 1 and val.count('Р') == 1 and val.count('И') == 1 and val.count('В') == 1 \
        and val.count('Ы') == 1 and val.count('Ч') == 1 and val.count('К') == 1 and \
            val.count('А') == 1 and