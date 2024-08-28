import subprocess

def log_and_run(command, section_name, log_file):
    """
    Runs a command and logs the output to both the console and a file.

    Parameters:
    - command: The command to run as a list.
    - section_name: A string describing the current section (e.g., "Nmap Scan Results").
    - log_file: The path to the log file where output will be saved.
    """
    with open(log_file, 'a') as file:
        # Write the section divider
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"{section_name}\n")
        file.write("=" * 50 + "\n\n")

        # Run the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # Stream the output to both the console and the file
        for line in iter(process.stdout.readline, b''):
            decoded_line = line.decode('utf-8')
            print(decoded_line, end='')
            file.write(decoded_line)
        
        process.stdout.close()
        process.wait()
