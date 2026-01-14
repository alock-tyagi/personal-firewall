import json
from logger import log_packet
from scapy.layers.inet import IP, TCP, UDP, ICMP

with open("rules.json") as f:
    rules = json.load(f)

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if src_ip in rules["blocked_ips"]:
            log_packet(packet, "BLOCKED_IP")
            return

        if TCP in packet:
            if packet[TCP].dport in rules["blocked_ports"]:
                log_packet(packet, "BLOCKED_PORT")
                return

        log_packet(packet, "ALLOWED")
