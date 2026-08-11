import csv
import os

def generate_alerts(flagged_ips, output_file="reports/incidents.csv"):
    """
    Append alerts to incidents.csv with severity levels.
    """
    os.makedirs("reports", exist_ok=True)
    with open(output_file, 'a', newline='') as f:
        writer = csv.writer(f)
        for ip, count in flagged_ips.items():
            severity = "HIGH" if count >= 10 else "MEDIUM"
            writer.writerow([ip, count, severity])
