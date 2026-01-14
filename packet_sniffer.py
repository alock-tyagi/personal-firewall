from scapy.all import sniff
from firewall import process_packet

def start_sniffing():
    sniff(prn=process_packet, store=False)
