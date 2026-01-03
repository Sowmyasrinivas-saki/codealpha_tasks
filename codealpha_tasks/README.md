Cyber Security Internship Tasks – Practical Implementation

Overview
This repository contains the implementation and documentation of four core cybersecurity tasks completed as part of an internship program. Each task focuses on a different security domain, providing hands-on experience with real-world tools, concepts, and best practices used in the cybersecurity industry.

The tasks include network traffic analysis, phishing awareness, secure coding review, and intrusion detection system setup.

----------------------------------------------------------------

TASK 1: Basic Network Sniffer

Description
This task involves building a basic network packet sniffer using Python to capture and analyze network traffic. The goal is to understand how data flows across networks and how different protocols operate at various layers.

Objectives
- Capture live network packets
- Analyze packet structure and headers
- Identify source and destination IP addresses
- Understand TCP/IP communication
- Inspect payload data

Tools and Technologies
- Python
- Scapy library
- Windows OS

Key Features
- Real-time packet capture
- Displays protocol, ports, and IP addresses
- Extracts raw payload data
- Helps visualize live network communication

Learning Outcome
Gained practical understanding of packet-level communication and network protocols.

----------------------------------------------------------------

TASK 2: Phishing Awareness Training

Description
This task focuses on creating awareness about phishing attacks through educational content. It explains how attackers use social engineering techniques to trick users and how to identify and prevent phishing attempts.

Objectives
- Explain phishing attack types
- Identify phishing emails and fake websites
- Understand social engineering techniques
- Educate users on prevention strategies
- Test awareness using quizzes

Topics Covered
- Email phishing indicators
- URL and domain spoofing
- Fake login pages
- Social engineering tactics
- Best practices for online safety
- Interactive quiz questions

Learning Outcome
Developed the ability to recognize phishing attempts and educate others on cyber hygiene.

----------------------------------------------------------------

TASK 3: Secure Coding Review

Description
This task involves reviewing application source code to identify security vulnerabilities and implementing secure coding practices. A vulnerable version of the code is analyzed and then corrected.

Objectives
- Perform manual code review
- Identify common security vulnerabilities
- Apply secure coding standards
- Recommend remediation steps
- Document findings professionally

Vulnerabilities Identified
- Hardcoded credentials
- Lack of input validation
- Insecure authentication logic
- Poor error handling

Deliverables
- Vulnerable code file
- Code review document
- Secure, remediated code file

Learning Outcome
Learned how to audit code for security flaws and apply industry-standard secure coding techniques.

----------------------------------------------------------------

TASK 4: Network Intrusion Detection System (NIDS)

Description
This task involves setting up a Network Intrusion Detection System using Snort on a Windows environment. The system monitors network traffic and generates alerts for suspicious activity.

Objectives
- Install and configure Snort
- Create custom detection rules
- Validate configuration
- Monitor live network traffic
- Generate alerts for detected events

Tools and Technologies
- Snort (Windows)
- Npcap
- Windows OS
- Command Prompt (Administrator)

Key Features
- Rule-based intrusion detection
- Custom alert rules
- Real-time traffic monitoring
- Configuration validation and troubleshooting

Example Rule
alert tcp any any -> any 80 (msg:"HTTP Traffic Detected"; sid:1000001; rev:1;)

Learning Outcome
Gained hands-on experience with IDS setup, rule creation, and real-time network monitoring.

----------------------------------------------------------------

Conclusion
These tasks collectively strengthened practical knowledge of cybersecurity fundamentals including networking, threat awareness, secure development, and intrusion detection. The hands-on approach provided real-world exposure to tools and techniques used in professional cybersecurity environments.

Status
All four tasks have been successfully completed and tested.