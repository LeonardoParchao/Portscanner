# Port Scanner

Port Scanner is an open-source Python script that allows you to perform network port scanning on a target host. It helps identify open ports and the associated services running on those ports.

## Features

- Scans a range of ports on a specified target host.
- Identifies open ports and their associated services.
- Performs banner grabbing to provide additional information about the services.
- User-friendly command-line interface.

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/port-scanner.git
   ```

2. Navigate to the project directory:

   ```shell
   cd port-scanner
   ```

3. Run the script:

   ```shell
   python port_scanner.py
   ```

4. Follow the on-screen instructions to enter the target host and the range of ports to scan.

## License

This project is open source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code in accordance with the terms of the license.

## Contributing

Contributions to this project are welcome! If you find a bug, have an enhancement in mind, or would like to suggest new features, please open an issue or create a pull request. For more information, please refer to the [Contribution Guidelines](CONTRIBUTING.md).

## Acknowledgments

- This project uses the `socket` module in Python for network communication.
- Service names and port associations are based on the common ports dictionary.
- Banner grabbing is used to gather additional service information.

---

**Disclaimer:** This tool is intended for educational and network administration purposes. Ensure you have proper authorization before scanning any network or system that you do not own or have explicit permission to scan. Unauthorized scanning may violate applicable laws and regulations.
