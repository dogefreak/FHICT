#!/usr/bin/env python2

import os
import re

# Get local IP, MAC address, and subnet mask
output = os.popen('ifconfig').read()
local_ip_match = re.search('inet (.*?)\s', output)
local_mac_match = re.search('ether (.*?)\s', output)
subnet_mask_match = re.search('netmask (.*?)\s', output)

local_ip = local_ip_match.group(1)
local_mac = local_mac_match.group(1)
subnet_mask = subnet_mask_match.group(1)

# Get default gateway IP address
output = os.popen('netstat -rn').read()
gateway_ip_match = re.search('default\s+(.*?)\s', output)

if gateway_ip_match:
    gateway_ip = gateway_ip_match.group(1)
else:
    gateway_ip = None

print("Local IP address: %s" % local_ip)
print("Local MAC address: %s" % local_mac)
print("Subnet mask: %s" % subnet_mask)
print("Gateway IP address: %s" % gateway_ip)
