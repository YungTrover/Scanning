import subprocess


def run_nikto(target, port):
    print(f"Running Nikto scan on {target}:{port}")
    command = ["nikto", "-h" , f"{target}:{port}"]
    subprocess.run(command)
    