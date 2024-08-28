#main.py

import sys
import argparse
from port_scanner import port_scan
from nmap_runner import run_nmap
from gobuster_runner import run_gobuster
from nikto_runner import run_nikto
import output


def main():
    parser = argparse.ArgumentParser(description="All in one Portscanner!!!")
    parser.add_argument("target" , help="Target IP or hostname you are trying to scan")
    parser.add_argument("-n", "--nmap", action="store_true", help="Run an nmap scan on the open ports found")
    parser.add_argument("-k", "--nikto", action="store_true", help="Run a nikto scan on the main website")
    parser.add_argument("-g", "--gobuster", action="store_true", help="Run agobuster scan to find subdirectories on the target")
    parser.add_argument("-p", "--port", type=int, help="Specify the port to run nikto and Gobuser on (Default is 80).")
    parser.add_argument("-o", "--output", default="scan_results.log", help="Specify an output location for the results (Default= scan_results.log).")


    args = parser.parse_args()

    target = args.target
    port = args.port if args.port else 80
    log_file = args.output

    open_ports = port_scan(target)


    if args.nmap:
        run_nmap(target, open_ports, log_file)

    if args.nikto:
        run_nikto(target, port, log_file)

    if args.gobuster:
        run_gobuster(target, port, log_file)


    print("Scanning Complete. Results saved to ", log_file)


if __name__ == "__main__":
    main()