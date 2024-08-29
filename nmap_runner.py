import subprocess


def run_nmap(target, open_ports):
    ports = ','.join(str(port) for port in open_ports)
    additional_flags = input("Please enter any additional flags for nmap you would like to use. Leave blank for default.")
    print(f"Running nmap on {target} for ports: {ports}")
    command = ['nmap', "-p" , ports, target]
    if additional_flags:
        command.extend(additional_flags.split())
    subprocess.run(command)