#!/usr/bin/env python3
import subprocess

subprocess.call("ifconfig docker0 down", shell=True)
subprocess.call("ifconfig docker0 hw ether 02:42:fe:59:94:0e", shell=True)
subprocess.call("ifconfig docker0 up", shell=True)