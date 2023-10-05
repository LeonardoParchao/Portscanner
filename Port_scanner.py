import socket

# Define common ports and their corresponding service names
common_ports = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
}

def scan_ports(target_host, start_port, end_port):
    open_ports = {}

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Set a timeout for the connection attempt
                result = sock.connect_ex((target_host, port))
                if result == 0:
                    open_ports[port] = common_ports.get(port, "Unknown Service")
                    # Perform banner grabbing to get more information
                    banner = sock.recv(1024).decode("utf-8").strip()
                    open_ports[port] += f" ({banner})"
        except KeyboardInterrupt:
            print("Scan aborted by user.")
            break
        except socket.error:
            pass  # Ignore socket errors (e.g., connection refused)

    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("Open ports on {}:".format(target_host))
        for port, service in open_ports.items():
            print(f"Port {port}: {service}")
    else:
        print("No open ports found on {}.".format(target_host))
