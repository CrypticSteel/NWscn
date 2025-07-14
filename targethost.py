import ipaddress
import re

def target():
    ip = input ("Enter IP or FQDN: ")
    print(f"Scanning: {ip}")

target()