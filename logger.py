from datetime import datetime

def log_event(ip, attack_type, payload):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} | IP: {ip} | Attack: {attack_type} | Payload: {payload}\n")