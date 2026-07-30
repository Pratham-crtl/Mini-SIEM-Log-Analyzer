import json
import re

class LogParser:
    def __init__(self):
        self.parsers = {
            "apache": self.parse_apache,
            "auth": self.parse_auth,
            "windows": self.parse_windows,
            "json": self.parse_json
        }

    def parse(self, log_line, log_type):
        if log_type in self.parsers:
            return self.parsers[log_type](log_line)
        return {"raw": log_line}

    def parse_apache(self, line):
        # Example: 192.168.1.10 - - [30/Jul/2026:19:59] "GET /index.html" 200
        match = re.match(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*"(?P<method>\w+) (?P<url>.*?)".* (?P<status>\d+)', line)
        if match:
            return match.groupdict()
        return {"raw": line}

    def parse_auth(self, line):
        # Example: Jul 30 19:59:01 server sshd[1234]: Failed password for root from 192.168.1.20
        match = re.match(r'^(?P<timestamp>\w+ +\d+ \d+:\d+:\d+).*Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)', line)
        if match:
            return match.groupdict()
        return {"raw": line}

    def parse_windows(self, line):
        # Example: Windows Security Event Log (simplified)
        return {"event": line}

    def parse_json(self, line):
        try:
            return json.loads(line)
        except:
            return {"raw": line}
