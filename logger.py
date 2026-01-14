from datetime import datetime

def log_packet(packet, status):
    with open("firewall.log", "a") as f:
        f.write(f"{datetime.now()} | {status} | {packet.summary()}\n")
