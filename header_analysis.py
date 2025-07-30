import re

def extract_ips(headers):
    received_headers = headers.get("Received", "")
    ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
    return re.findall(ip_pattern, str(received_headers))

def check_spf(headers):
    spf = headers.get("Received-SPF", "")
    if "pass" in spf.lower():
        return "PASS"
    elif "fail" in spf.lower():
        return "FAIL"
    return "NONE"
