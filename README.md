# 📧 Email Analyzer

A simple Python tool for analyzing `.eml` email files — extracts metadata, checks headers, detects suspicious links, and flags dangerous attachments.

## Features
- Extracts subject, sender, recipients, and date
- Finds IP addresses from headers
- Checks SPF authentication results
- Detects suspicious/malicious URLs
- Extracts and flags dangerous attachments
- Saves results in JSON format

## Project Structure
email_analyzer/
│── main.py # Runs the full analysis
│── parser.py # Parses email content
│── header_analysis.py # Extracts IPs and SPF results
│── phishing_detector.py # Detects suspicious URLs
│── attachment_handler.py # Extracts risky attachments
│── report.py # Saves JSON reports
│── samples/ # Sample .eml files


## Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/email-analyzer.git
   cd email-analyzer
2. Place .eml files in samples/.

3. Run:
python main.py

4. View report.json for results.
