This firewall captures packets at the network interface level using Scapy.
Packets are analyzed based on protocol headers and filtered using rule sets.
iptables adds kernel-level blocking for enhanced security.

personal-firewall/
│
├── README.md
├── firewall.py
├── rules.json
├── logger.py
├── packet_sniffer.py
├── requirements.txt
├── setup_iptables.sh
└── docs/
    ├── architecture.md
    ├── screenshots.md
    
