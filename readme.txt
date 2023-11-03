This Python script allows you to scan a network
range and retrieve ARP information for active 
hosts. It uses the scapy library to send ARP 
requests and collect MAC addresses for the 
specified IP range.

Make sure to enter a valid network address format 
with a subnet prefix.

The success of this script depends on the 
availability of active hosts within the 
specified network range.

MAC addresses that are not available will 
not be displayed, and no 'unavailability' 
message will be shown.

A brief explanation of Ethernet to better understand this line of
code `[ether / arp_request for arp_request in arp_requests]`: In an Ethernet network, 
data is encapsulated within Ethernet frames, 
and an Ethernet frame consists of two main parts: 
the Ethernet header and the data. The Ethernet header contains 
information such as the MAC address of the sender and the MAC address 
of the receiver, the protocol type, and so on.

When you create an ARP packet, you need to encapsulate it 
within an Ethernet frame for it to be properly transmitted 
across the network. The line packets = [ether / arp_request for arp_request in arp_requests] 
uses the / operator sto combine these two objects, with the Ethernet object serving as 
the Ethernet frame header and the ARP object as the data payload.