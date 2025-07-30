import os

DANGEROUS_EXTENSIONS = [".exe", ".js", ".scr", ".bat", ".cmd", ".vbs"]

def extract_attachments(msg, output_dir="attachments"):
    os.makedirs(output_dir, exist_ok=True)
    flagged_files = []

    for part in msg.walk():
        filename = part.get_filename()
        if filename:
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "wb") as f:
                f.write(part.get_payload(decode=True))
            if any(filename.lower().endswith(ext) for ext in DANGEROUS_EXTENSIONS):
                flagged_files.append(filename)
    return flagged_files
