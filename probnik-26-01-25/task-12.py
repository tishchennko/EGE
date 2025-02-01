for n in range(1, 100_000):
    st = '>' + '0' * 21 + '1' * n + '2' * 11
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '1>')
    if sum(map(int, st[:-1])) % n == 0:
        print(n)