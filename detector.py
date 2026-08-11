from collections import Counter

def detect_failed_logins(events, threshold=3):
    """
    Detect IPs with failed login attempts above threshold.
    Returns dict: {ip: count}
    """
    ip_counts = Counter([event['ip'] for event in events])
    flagged = {ip: count for ip, count in ip_counts.items() if count >= threshold}
    return flagged
