from parser import LogParser
from detector import Detector
from alert_engine import AlertEngine

def run_pipeline(log_file, log_type):
    parser = LogParser()
    detector = Detector()
    alert_engine = AlertEngine()

    with open(log_file, "r") as f:
        for line in f:
            event = parser.parse(line.strip(), log_type)

            # Run detection rules
            brute_alert = detector.brute_force(event)
            error_alert = detector.error_spike(event)

            # Send alerts
            alert_engine.notify(brute_alert)
            alert_engine.notify(error_alert)

if __name__ == "__main__":
    # Example usage
    run_pipeline("sample_logs/auth.log", "auth")
    run_pipeline("sample_logs/access.log", "apache")
    run_pipeline("sample_logs/app.json", "json")
