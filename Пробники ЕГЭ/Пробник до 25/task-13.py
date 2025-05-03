from ipaddress import *

ip1 = ip_address('111.81.192.0')
ip2 = ip_address('111.81.208.27')
for m in range(33):
    net = ip_network(f'{ip2}/{m}', False)
    if ip1 == net.network_address:
        print(net.netmask)
