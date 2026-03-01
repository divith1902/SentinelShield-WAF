from flask import Flask, request
from waf_rules import check_sql_injection, check_xss, check_directory_traversal
from logger import log_event

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    data = request.args.get("input", "")
    ip = request.remote_addr

    if check_sql_injection(data):
        log_event(ip, "SQL Injection", data)
        return "Blocked: SQL Injection Detected!", 403

    if check_xss(data):
        log_event(ip, "XSS Attack", data)
        return "Blocked: XSS Attack Detected!", 403

    if check_directory_traversal(data):
        log_event(ip, "Directory Traversal", data)
        return "Blocked: Directory Traversal Detected!", 403

    return "Request Allowed"

if __name__ == "__main__":
    app.run(debug=True)