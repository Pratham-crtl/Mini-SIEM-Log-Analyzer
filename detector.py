from datetime import datetime, timedelta
from collections import defaultdict

class Detector:
    def __init__(self):
        self.failed_logins = defaultdict(list)
        self.error_counts = defaultdict(int)

    def brute_force(self, event):
        ip = event.get("ip")
        timestamp = event.get("timestamp")
        if ip and timestamp:
            self.failed_logins[ip].append(datetime.strptime(timestamp, "%b %d %H:%M:%S"))
            # Sliding window: 2 minutes
            window = [t for t in self.failed_logins[ip] if t > datetime.now() - timedelta(minutes=2)]
            if len(window) > 5:
                return {"alert": "Brute Force Detected", "ip": ip, "count": len(window)}
        return None

    def error_spike(self, event):
        status = event.get("status")
        ip = event.get("ip")
        if status and status.startswith("5"):  # HTTP 500 errors
            self.error_counts[ip] += 1
            if self.error_counts[ip] > 10:
                return {"alert": "Error Spike Detected", "ip": ip, "errors": self.error_counts[ip]}
        return None
