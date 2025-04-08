from ipaddress import ip_network

net = ip_network('143.168.72.213/255.255.255.240', False)

for i in net:
    print(i, f'{int(i):032b}')