#!/usr/bin/env python3
# original_mac = "02:42:fe:59:94:0e"
# new_mac = "00:11:22:33:44:55"

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m","--mac", dest="new_mac",help="The new MAC to change the interface to")

parser.parse_args()
print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])