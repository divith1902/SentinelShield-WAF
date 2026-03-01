import re

def check_sql_injection(data):
    patterns = [
        r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
        r"(\bOR\b|\bAND\b).*(=)",
        r"UNION.*SELECT",
    ]
    for pattern in patterns:
        if re.search(pattern, data, re.IGNORECASE):
            return True
    return False


def check_xss(data):
    patterns = [
        r"<script.*?>.*?</script>",
        r"javascript:",
        r"onerror=",
    ]
    for pattern in patterns:
        if re.search(pattern, data, re.IGNORECASE):
            return True
    return False


def check_directory_traversal(data):
    if "../" in data or "..\\" in data:
        return True
    return False