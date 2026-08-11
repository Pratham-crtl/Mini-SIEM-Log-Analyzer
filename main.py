import os
import pandas as pd
import matplotlib.pyplot as plt
from parser import parse_auth_log
from detector import detect_failed_logins
from alert_engine import generate_alerts

def main():
    os.makedirs("reports", exist_ok=True)

    # Step 1: Parse logs
    events = parse_auth_log("sample_logs/auth.log")

    # Step 2: Detect anomalies
    flagged_ips = detect_failed_logins(events)

    # Step 3: Save failed login report
    report_file = "reports/failed_login_report.csv"
    df = pd.DataFrame(list(flagged_ips.items()), columns=["IP", "Failed_Attempts"])
    df.to_csv(report_file, index=False)

    # Step 4: Generate chart
    chart_file = "reports/failed_login_chart.png"
    df.plot(kind="bar", x="IP", y="Failed_Attempts", legend=False)
    plt.title("Failed Login Attempts per IP")
    plt.ylabel("Attempts")
    plt.tight_layout()
    plt.savefig(chart_file)

    # Step 5: Generate alerts
    generate_alerts(flagged_ips)

    print("Reports generated in /reports folder.")

if __name__ == "__main__":
    main()
