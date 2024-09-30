from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP  # Import the necessary layers


def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"\n[+] New Packet: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        # Check for TCP, UDP, or ICMP protocols
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print("Protocol: TCP")
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            print(f"Payload (Hex): {bytes(tcp_layer).hex()}")
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print("Protocol: UDP")
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
            print(f"Payload (Hex): {bytes(udp_layer).hex()}")
        elif packet.haslayer(ICMP):
            icmp_layer = packet[ICMP]
            print("Protocol: ICMP")
            print(f"Type: {icmp_layer.type}")
            print(f"Code: {icmp_layer.code}")
        else:
            print("Other IP-based protocol")

        print("-" * 50)


def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=False, filter="ip")


if __name__ == "__main__":
    main()
