for N in range(4, 10001):
    st = '5' + '2' * N
    while '52' in st or '2222' in st or '1122' in st:
        st = st.replace('52', '11', 1)
        st = st.replace('2222', '5', 1)
        st = st.replace('1122', '25', 1)
    if sum(map(int, st)) % 10 == 7:
        print(N)
        break
#5
