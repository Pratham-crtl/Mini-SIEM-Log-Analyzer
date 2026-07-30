from colorama import Fore, Style
import csv

class AlertEngine:
    def __init__(self, csv_file="reports/incidents.csv"):
        self.csv_file = csv_file

    def notify(self, alert):
        if not alert:
            return
        severity = alert.get("alert", "Unknown")
        ip = alert.get("ip", "N/A")
        print(Fore.RED + f"[ALERT] {severity} from {ip}" + Style.RESET_ALL)

        # Append to CSV
        with open(self.csv_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=alert.keys())
            writer.writerow(alert)
