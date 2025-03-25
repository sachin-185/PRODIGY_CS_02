from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    """Function to process captured packets."""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            proto_name = "TCP"
        elif UDP in packet:
            proto_name = "UDP"
        elif ICMP in packet:
            proto_name = "ICMP"
        else:
            proto_name = f"Other ({protocol})"
        
        print(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {proto_name}")

        # Display payload if available
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = packet[TCP].payload if TCP in packet else packet[UDP].payload
            if payload:
                print(f"Payload: {bytes(payload)}\n")

# Disclaimer for ethical use
print("Packet Sniffer for Educational Purposes Only.")
print("Ensure you have permission before sniffing network traffic.\n")

# Sniff packets on the default interface (first 5 packets)
sniff(prn=packet_callback, count=3, store=False)
