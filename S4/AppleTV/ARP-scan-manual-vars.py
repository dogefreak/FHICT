from scapy.all import *

subnet = '255.255.255.0'
gateway = '192.168.1.0'

# Convert subnet mask to CIDR notation
cidr = sum(bin(int(x)).count('1') for x in subnet.split('.'))
ip_range = '{}{}'.format(gateway, '/{}'.format(cidr))

arp = ARP(pdst=ip_range)
ether = Ether(dst='ff:ff:ff:ff:ff:ff')
packet = ether/arp

result = srp(packet, timeout=2, verbose=0)[0]

clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print(clients)
