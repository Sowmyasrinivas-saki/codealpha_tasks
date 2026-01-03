Network Intrusion Detection System (NIDS) using Snort on Windows

Overview
This project demonstrates the setup and configuration of a Network Intrusion Detection System (NIDS) using Snort on a Windows environment. The objective is to monitor network traffic, detect suspicious or malicious activities, and generate alerts based on custom detection rules.

The project focuses on understanding how IDS works, configuring Snort correctly on Windows, handling configuration challenges, and validating detection through custom rules.

Objectives
- Set up Snort as a network-based intrusion detection system
- Configure and validate Snort configuration files
- Create and test custom intrusion detection rules
- Monitor live network traffic and generate alerts
- Understand IDS concepts, rule-based detection, and alerting mechanisms

Tools and Technologies
- Snort (Windows version)
- Windows 10/11
- Command Prompt (Administrator)
- Notepad++ or any text editor
- WinPcap / Npcap (packet capture driver)

Project Structure

Snort-NIDS/
├── README.md
├── requirements.txt
├── snort.conf (configured Snort configuration file)
├── rules/
│   └── local.rules (custom detection rules)
└── screenshots/ (optional screenshots of alerts and logs)

Configuration Summary
- Unsupported Linux-only preprocessors were disabled to ensure Windows compatibility
- Only local.rules is enabled to keep configuration minimal and stable
- Custom rules are written to detect basic network activities
- Configuration is validated using Snort test mode

Example Custom Rule
alert tcp any any -> any 80 (msg:"HTTP Traffic Detected"; sid:1000001; rev:1;)

How to Run
1. Open Command Prompt as Administrator
2. Validate configuration:
   snort -T -c C:\Snort\etc\snort.conf
3. Identify network interface:
   snort -W
4. Run Snort in live mode:
   snort -i <interface_number> -c C:\Snort\etc\snort.conf -A console

Learning Outcomes
- Practical understanding of IDS architecture
- Hands-on experience with Snort rule creation
- Knowledge of packet inspection and alert generation
- Experience troubleshooting real-world IDS configuration issues

Status
Completed and tested successfully on Windows environment.