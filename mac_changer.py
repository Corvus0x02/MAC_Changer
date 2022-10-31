#!/usr/bin/env python3
# Quick Python script for changing the MAC Address on a *nix host, uses native ifconfig command. Similar to macchanger on Kali
# Reference https://dnschecker.org/mac-lookup.php for more information on MAC addresses and to search for MAC addresses that may be whitelisted in a network/environment
# Requires root/admin privileges on the device

#Imports
import subprocess
import optparse
import re

#Function to intake user provided arguments
def get_arguments():
    parser = optparse.OptionParser()
    #Interface argument
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    #New MAC address argument
    parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC to change the interface to")
    (options, arguments) = parser.parse_args()
    #Error handling
    if not options.interface:
        #code to handle error
        parser.error("[-] Please specify an interface. Use --help for more info.")
    elif not options.new_mac:
        #code to handle error
        parser.error("[-] Please specify a new mac address. Use --help for more info.")
    return options

#Function to change the devices MAC address. Uses provided interface and MAC address
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#Function to get the current MAC address for a provided interface
def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return "[-] Could not read MAC address"

#Get the user arguments
options = get_arguments()
#Set the current MAC and print it to the terminal
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

#Change the MAC on the target interface
change_mac(options.interface, options.new_mac)

#Check if successful
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[-] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")