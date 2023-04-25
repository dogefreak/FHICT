#!/usr/bin/env python2

from scapy.all import *
import os

# Get local IP and MAC addresses
local_ip = get_if_addr(conf.iface)
local_mac = get_if_hwaddr(conf.iface)

# Get gateway IP address
def get_default_gateway():
    with os.popen("route -n get default") as output:
        for line in output:
            if 'gateway' in line.lower():
                return line.split()[-1]

gateway_ip = get_default_gateway()

print("Local IP address: %s" % local_ip)
print("Local MAC address: %s" % local_mac)
print("Gateway IP address: %s" % gateway_ip)
