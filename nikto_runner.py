import subprocess
from output import log_and_run

def run_nikto(target, port, log_file):
    print(f"Running Nikto scan on {target}:{port}")
    command = ["nikto", "-h" , f"{target}:{port}"]
    log_and_run(command, log_file)
    