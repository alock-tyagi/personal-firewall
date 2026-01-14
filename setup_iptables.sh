#!/bin/bash

sudo iptables -A INPUT -p tcp --dport 23 -j DROP
sudo iptables -A INPUT -s 192.168.1.100 -j DROP

#to make it executable
chmod +x setup_iptables.sh
