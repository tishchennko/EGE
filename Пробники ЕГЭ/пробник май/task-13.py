from ipaddress import ip_network

for mask in range(33):
    net1 = ip_network(f'200.154.190.12/{mask}', False)
    net2 = ip_network(f'200.154.184.0/{mask}', False)
    if net1.network_address == net2.network_address:
        print(net1.netmask)