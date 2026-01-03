import re
import matplotlib.pyplot as plt
from collections import Counter

alert_file = r"C:\Snort\log\alert.ids"

alerts = []

with open(alert_file, "r") as file:
    for line in file:
        match = re.search(r"\[\*\*\] (.*?) \[\*\*\]", line)
        if match:
            alerts.append(match.group(1))

if not alerts:
    print("No alerts found.")
    exit()

counter = Counter(alerts)

plt.figure()
plt.bar(counter.keys(), counter.values())
plt.xticks(rotation=45, ha="right")
plt.title("Snort Alerts")
plt.tight_layout()
plt.show()
