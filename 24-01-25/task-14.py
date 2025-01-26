from string import *

alp = digits + ascii_lowercase

for x in alp[:22]:
    a = int(f'A23{x}AC0',22)
    b = int(f'GB{x}21670', 22)
    ab = a + b
    if ab % 21 == 0:
        print(ab//22)