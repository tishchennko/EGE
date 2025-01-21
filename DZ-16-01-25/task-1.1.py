from itertools import*

graph = 'DE DG GA AF GF FH HE HC CB BE BD'.split()
mat = '234 157 147 138 268 58 23 456'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+ 1) in mat [i.index(y)] for x,y in graph):
        print(*i)