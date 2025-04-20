from ipaddress import ip_network, ip_address

ip = ip_address('99.8.254.232')
for mask in range(16, 25):
    net = ip_network(f'{ip}/{mask}', False)
    if ip not in (net.broadcast_address, net.network_address):
        for i in net:
            i = f'{int(i):032b}'
            if i[:16].count('1') > i[16:].count('1'):
                break
        else:
            print(net.netmask)