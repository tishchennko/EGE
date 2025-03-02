

def div(x):
    d = set()
    for i in range(2, int (x**0.5)+1):
        if x%i==0:
            d. add (i)
            d.add(x//i)
    return sorted(d)

for i in range (200_000_001,200_000_100):
    d = [i for i in div(x) if i%2!=0]
    if len(d)>=6:
        cnt += 1
        print (x, res[-6])
        if cnt == 5: break

