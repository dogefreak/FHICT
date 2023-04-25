import re
import subprocess

# Get the list of network interfaces
interface_list = subprocess.check_output(["ifconfig", "-l"]).split()

# Loop through the network interfaces
for interface in interface_list:
    # Get the subnet mask for the current interface
    subnet_output = subprocess.check_output(["ifconfig", interface])
    subnet_match = re.search('netmask\s+0x(\w+)\s', subnet_output)

    if subnet_match:
        # Convert the subnet mask from hexadecimal to dotted decimal notation
        subnet_mask = ".".join([str(int(subnet_match.group(1)[i:i+2], 16)) for i in range(0, len(subnet_match.group(1)), 2)])
        print("Interface:", interface, "Subnet Mask:", subnet_mask)
