import email
from email import policy
from email.parser import BytesParser

def parse_email(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    metadata = {
        "subject": msg["subject"],
        "from": msg["from"],
        "to": msg["to"],
        "date": msg["date"],
        "message_id": msg["message-id"],
        "headers": dict(msg.items()),
        "body": get_body(msg)
    }
    return metadata

def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_content()
    else:
        return msg.get_content()
    return None
