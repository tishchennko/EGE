from ipaddress import ip_network

for mask in range(16, 25):
    net = ip_network(f'152.65.245.132/{mask}', False)
    cnt = 0
    for i in net:
        i = f'{int(i):032b}'
        if i[:16].count('0') >= i[16:].count('0'):
            cnt += 1
    if cnt == len(list(net)):
        print(mask)
        break