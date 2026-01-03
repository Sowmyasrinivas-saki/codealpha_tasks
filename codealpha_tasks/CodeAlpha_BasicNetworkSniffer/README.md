TASK 1: Basic Network Sniffer

Overview
This project implements a basic network packet sniffer using Python to capture and analyze live network traffic. The objective is to understand how data flows across a network, how packets are structured, and how common protocols operate at different layers of the TCP/IP model.

The sniffer captures packets in real time and displays key information such as source and destination IP addresses, protocols, ports, and raw payload data.

Objectives
- Capture live network packets
- Analyze packet headers and structure
- Identify source and destination IP addresses
- Understand TCP, UDP, and IP protocols
- Inspect raw payload data
- Learn fundamentals of network traffic analysis

Tools and Technologies
- Python
- Scapy library
- Windows Operating System
- Command Prompt / Terminal

Project Structure
Basic-Network-Sniffer/
├── network_sniffer.py
├── README.md
└── screenshots/ (optional output samples)

How It Works
The program uses the Scapy library to sniff network packets in real time. Each captured packet is analyzed to extract:
- Source IP address
- Destination IP address
- Protocol type (TCP/UDP)
- Source and destination ports
- Raw payload data (if available)

The extracted information is displayed in a readable format on the console.

Example Output
Source IP        : 192.168.1.233
Destination IP   : 40.104.68.34
Protocol         : TCP
Source Port      : 52216
Destination Port : 443
Payload (Raw)    : <binary data>

How to Run
1. Install Python
2. Install required library:
   pip install scapy
3. Run the script with administrator privileges:
   python network_sniffer.py

Note: Administrator permissions are required for packet sniffing.

Learning Outcomes
- Gained practical understanding of packet-level communication
- Learned how network protocols function in real time
- Understood packet sniffing concepts and limitations
- Developed hands-on experience with Scapy
- Improved knowledge of network security fundamentals

Status
Task completed and tested successfully.
