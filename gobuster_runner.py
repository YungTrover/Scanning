import subprocess
import re
 
def is_IP(target):
    ip_pattern = re.compile(r'^\d{1,3},\.d{1,3}\.d{1,3}\.\d{1,3}$')
    return bool(ip_pattern.match(target))


def run_gobuster(target, port):
    print(f"Running Gobuster on http://{target}:{port}/ ")
    default_wordlist = "/usr/share/wordlists/dirb/common.txt"
    scan_type  = input("Would you like to check for subdomains or for directories on the target? (Dns/Dir): ").strip().lower()
      

    if scan_type not in ['dns', 'dir', '']:
        print("Invalid selection. Defaulting to directory scan.")
        scan_type = 'dir'

    if scan_type == 'dns' and is_IP(target):
        print("""Subdomain scans can only be performed on hostnames and not IPs.
               Please try again with a hostname (example.com)
              Defaulting to directory scan.""")
        scan_type = 'dir'
        

    use_custom_wordlist = input("Would you like to use a custom wordlist? (y/n): ").strip().lower()

    if use_custom_wordlist == 'y':
        custom_wordlist = input("Please enter the path to the wordlist you would like to use: ").strip()
        wordlist = custom_wordlist if custom_wordlist else default_wordlist
    else:
        wordlist = default_wordlist

    if scan_type == 'dns':
            command = ["gobuster", "dns", "-d", target, "-w", wordlist]
    else:
        command = ["gobuster", "dir", "-u", f"http://{target}:{port}/", "-w" , wordlist ]


    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("Gobuster not found. Please ensure that you have it installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"An error occured while running Gubuser {e}")