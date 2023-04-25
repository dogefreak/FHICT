#!/usr/bin/env python2

from scapy.all import *

# Get local IP and MAC addresses
local_ip = get_if_addr(conf.iface)
local_mac = get_if_hwaddr(conf.iface)

print("Local IP address: %s" % local_ip)
print("Local MAC address: %s" % local_mac)
