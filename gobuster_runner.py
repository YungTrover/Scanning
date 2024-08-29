import subprocess
 

def run_gobuster(target, port):
    print(f"Running Gobuster on {target}")
    default_wordlist = "/usr/share/wordlists/dirb/common.txt"
    use_custom_wordlist = input("Would you like to use a custom wordlist? (y/N): ").strip().lower()

    if use_custom_wordlist == 'y':
        custom_wordlist = input("Please enter the path to the wordlist you would like to use").strip
        wordlist = custom_wordlist if custom_wordlist else default_wordlist
    else:
        wordlist = default_wordlist

    command = ["gobuster", "dir", "-u ", f"http://{target}:{port}/", " -w" , wordlist ]
    subprocess.run(command)