import os
import re
import socket
import struct

interfaces = ['en0', 'en1']

def get_subnet_mask(mask):
    # Convert the mask to an integer
    mask_int = int(mask, 16)

    # Convert the mask to dotted decimal format
    mask_dotted = socket.inet_ntoa(struct.pack('>I', mask_int))

    return mask_dotted

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
