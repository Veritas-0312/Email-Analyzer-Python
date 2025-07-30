from parser import parse_email
from header_analysis import extract_ips, check_spf
from phishing_detector import extract_links, check_suspicious_links
from attachment_handler import extract_attachments
from report import save_report

def analyze_email(file_path):
    email_data = parse_email(file_path)

    # Header Analysis
    email_data["source_ips"] = extract_ips(email_data["headers"])
    email_data["spf_result"] = check_spf(email_data["headers"])

    # Phishing Analysis
    links = extract_links(email_data["body"] or "")
    email_data["links"] = links
    email_data["suspicious_links"] = check_suspicious_links(links)

    # Attachment Analysis
    from email import policy
    from email.parser import BytesParser
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    email_data["dangerous_attachments"] = extract_attachments(msg)

    # Save Report
    save_report(email_data)

if __name__ == "__main__":
    analyze_email("samples/test_email.eml")
    print("Analysis complete. See report.json")
