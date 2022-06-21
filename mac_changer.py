#!/usr/bin/env python3

import subprocess

interface = "docker0"
original_mac = "02:42:fe:59:94:0e"
new_mac = "00:11:22:33:44:55"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + original_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)