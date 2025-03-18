def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True
ans = []
for n in range(3, 1001):
    st = '>' + 25 * '0' + n * '1' + 25 * '2'
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '1>', 1)
    if is_prime(sum(map(int, st[:-1]))):
        ans.append(n)
print(min(ans))
#7