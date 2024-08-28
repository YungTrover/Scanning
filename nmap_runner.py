import subprocess
from output import log_and_run

def run_nmap(target, open_ports, log_file):
    ports = ','.join(str(port) for port in open_ports)
    additional_flags = input("Please enter any additional flags for nmap you would like to use. Leave blank for default.")
    print(f"Running nmap on {target} for ports: {ports}")
    command = ['nmap', "-p" , ports, target]
    if additional_flags:
        command.extend(additional_flags.split())
    log_and_run(command, log_file)