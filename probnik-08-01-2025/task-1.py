from itertools import permutations

graph = 'EH HG HB BG GC CF BD DF DE FA EA'.split()
matri = '367 568 18 58 247 127 156 234'.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
        if all(str(i.index(x) + 1) in matri[i.index(y)] for x,y in graph):
            print(*i)
