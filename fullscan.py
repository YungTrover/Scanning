import sys
import argparse
import subprocess
from port_scanner import port_scan
from nmap_runner import run_nmap
from nikto_runner import run_nikto
from gobuster_runner import run_gobuster

def capture_output(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()

def main():
    parser = argparse.ArgumentParser(description="Network scanning script with optional modules.")
    parser.add_argument("target", help="Target IP or hostname to scan")
    parser.add_argument("-n", "--nmap", action="store_true", help="Run nmap on found open ports")
    parser.add_argument("-k", "--nikto", action="store_true", help="Run Nikto on the target")
    parser.add_argument("-g", "--gobuster", action="store_true", help="Run Gobuster on the target")
    parser.add_argument("-p", "--port", type=int, help="Specify port to run Nikto and Gobuster (default: 80)")
    parser.add_argument("-o", "--output", default="scan_results.log", help="Specify output log file (optional)")

    args = parser.parse_args()

    target = args.target
    port = args.port if args.port else 80  # Default port is 80
    output_file = args.output

    output = ""

    # Always run port scan
    open_ports = port_scan(target)
    output += f"\nPorts found open: {', '.join(str(port) for port in open_ports)}\n"

    # Conditionally run nmap if -n flag is set
    if args.nmap:
        output += "\n" + "=" * 50 + "\nNmap Scan Results\n" + "=" * 50 + "\n"
        output += capture_output(["nmap", "-p", ",".join(str(port) for port in open_ports), target])

    # Conditionally run Nikto if -k flag is set
    if args.nikto:
        output += "\n" + "=" * 50 + "\nNikto Scan Results\n" + "=" * 50 + "\n"
        output += capture_output(["nikto", "-h", f"{target}:{port}"])

    # Conditionally run Gobuster if -g flag is set
    if args.gobuster:
        output += "\n" + "=" * 50 + "\nGobuster Scan Results\n" + "=" * 50 + "\n"
        wordlist = "/usr/share/wordlists/dirb/common.txt"  # Update this path as needed
        output += capture_output(["gobuster", "dir", "-u", f"http://{target}:{port}", "-w", wordlist])

    # Print output to console
    print(output)

    # Save output to file if specified
    if output_file:
        with open(output_file, 'w') as file:
            file.write(output)
        print(f"\nResults saved to {output_file}")
    else:
        with open(output_file, 'w') as file:
            file.write(output)
        print(f"\n Results saved to scan_results.log")

if __name__ == "__main__":
    main()
