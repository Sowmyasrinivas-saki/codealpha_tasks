from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_handler(packet):

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print("\n==============================")
        print(f"Source IP        : {src_ip}")
        print(f"Destination IP   : {dst_ip}")

        # TCP packets
        if TCP in packet:
            print("Protocol         : TCP")
            print(f"Source Port      : {packet[TCP].sport}")
            print(f"Destination Port : {packet[TCP].dport}")

            payload = bytes(packet[TCP].payload)
            if payload:
                print(f"Payload (Raw)    : {payload[:50]}")

        # UDP packets
        elif UDP in packet:
            print("Protocol         : UDP")
            print(f"Source Port      : {packet[UDP].sport}")
            print(f"Destination Port : {packet[UDP].dport}")

            payload = bytes(packet[UDP].payload)
            if payload:
                print(f"Payload (Raw)    : {payload[:50]}")

        # ICMP packets
        elif ICMP in packet:
            print("Protocol         : ICMP")
            print("Payload          : ICMP Control Message")

# Start sniffing
sniff(prn=packet_handler, store=False)
