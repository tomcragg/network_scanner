#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    #create instance of scapy ARP object
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    #print a list of fields that can be changed
    #scapy.ls(scapy.ARP())

scan("10.0.2.1/24")