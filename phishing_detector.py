import re
from urllib.parse import urlparse

SUSPICIOUS_DOMAINS = ["paypal.com.fake", "secure-login.xyz", "update-info.click"]

def extract_links(text):
    url_pattern = r"(https?://[^\s]+)"
    return re.findall(url_pattern, text)

def check_suspicious_links(links):
    flagged = []
    for link in links:
        domain = urlparse(link).netloc
        if any(susp in domain for susp in SUSPICIOUS_DOMAINS):
            flagged.append(link)
    return flagged
