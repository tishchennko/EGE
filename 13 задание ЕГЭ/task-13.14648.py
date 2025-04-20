

from ipaddress import ip_address, ip_network

ip = ip_address('218.48.192.0')
cnt = 0
for mask in range(16, 25):
    net = ip_network(f'218.48.192.56/{mask}', False)
    if net.num_addresses >= 502 and ip == net.network_address:
        cnt += 1
print(cnt)