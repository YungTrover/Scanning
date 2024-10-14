import socket
from datetime import datetime

def port_scan(target):
    open_ports = []
    print('-' * 50)
    print("Scanning target: " + target)
    print("Scan started at: " + str(datetime.now()))
    
    try:
        # Attempt to resolve the hostname to an IP address
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n Hostname could not be resolved. Please check the target input.")
        return []

    try:
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print("Port {} is open".format(port))
                open_ports.append(port)
            s.close()
    except KeyboardInterrupt:
        print("\n You have stopped the scan.\n")
        return []
    except socket.error:
        print("\n The server is not responding.")
        return []

    return open_ports
