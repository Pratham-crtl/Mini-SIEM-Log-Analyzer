import re

def parse_auth_log(file_path):
    """
    Parse auth.log and extract failed login attempts.
    Returns a list of dicts: [{'ip': 'x.x.x.x', 'timestamp': 'YYYY-MM-DD HH:MM:SS'}]
    """
    events = []
    with open(file_path, 'r') as f:
        for line in f:
            if "Failed password" in line:
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    timestamp = " ".join(line.split()[0:3])  # e.g., Aug 11 22:10:01
                    events.append({"ip": ip, "timestamp": timestamp})
    return events
