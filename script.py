import pandas as pd
import matplotlib.pyplot as plt
import re

# Load sample logs
with open("sample_logs.txt", "r") as f:
    logs = f.readlines()

# Extract failed login attempts
failed_attempts = []
for line in logs:
    if "Failed password" in line:
        ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if ip_match:
            failed_attempts.append(ip_match.group(1))

# Convert to DataFrame
df = pd.DataFrame(failed_attempts, columns=["IP"])
summary = df["IP"].value_counts().reset_index()
summary.columns = ["IP", "Failed_Attempts"]

# Save CSV report
summary.to_csv("reports/failed_login_report.csv", index=False)

# Plot bar chart
plt.figure(figsize=(8,6))
plt.bar(summary["IP"], summary["Failed_Attempts"], color="red")
plt.xlabel("IP Address")
plt.ylabel("Failed Login Attempts")
plt.title("Failed Login Attempts per IP")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/failed_login_chart.png")
plt.show()
