import ipaddress
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

ip_add_range = input("Provide the address range as provided in this example (e.g., 192.168.0.0/24): ")


try:
    network_add, prefixe = ip_add_range.split('/')
    network_add = f"{network_add}/{prefixe}"

    # Convert network_add to an IPv4 object
    network = ipaddress.IPv4Network(network_add, strict=False)
except ValueError:
    print("Invalid network address format. Expected example: 192.168.0.0/24")

print(f"Sending ARP requests to {network}")

#Create a list that includes IP addresses within the specified range, excluding the network address and the broadcast address, by using the hosts method.
ipList = []
for ip in network.hosts():
    ipList.append(str(ip))

#Creating ARP requests for IP address resolution
arp_requests = [ARP(pdst=ip) for ip in ipList]
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packets = [ether / arp_request for arp_request in arp_requests]
responses, unanswered = srp(packets, timeout=3, verbose=0)

#display the IP-MAC address pairs.
for sent, received in responses:
    mac_address = received.psrc
    print(f"IP Address: {mac_address} ==>  MAC Address: {received.hwsrc}")
