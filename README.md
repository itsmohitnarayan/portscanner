```markdown
# Simple Python Port Scanner

![GitHub](https://img.shields.io/github/license/yourusername/PortScanner)

A simple Python command-line port scanner that allows you to scan a target host for open ports within a specified range using multi-threading.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features

- Scan a target host for open ports in a specified range.
- Utilizes multi-threading for faster port detection.
- Supports both IP addresses and domain names as target hosts.

## Getting Started

### Prerequisites

To run the port scanner, you need to have Python 3 installed on your system.

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/PortScanner.git
   cd PortScanner
   ```

2. Run the port scanner with the following command:

   ```sh
   python3 portscanner.py TARGET START_PORT END_PORT
   ```

   Replace `TARGET`, `START_PORT`, and `END_PORT` with your desired target host and port range.

## Usage

To use the Simple Python Port Scanner, follow the format below:

```sh
python3 portscanner.py TARGET START_PORT END_PORT
```

- `TARGET`: The target host you want to scan. This can be either an IP address or a domain name.
- `START_PORT`: The starting port number for the scan.
- `END_PORT`: The ending port number for the scan.

For example:

```sh
python3 portscanner.py example.com 80 100
```

This command will scan ports 80 to 100 on the host "example.com" (or its corresponding IP address) and report which ports are open.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please create an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Please note that scanning networks and systems without proper authorization may be illegal or against the terms of service of your network provider. Use this tool responsibly and only on systems and networks you have explicit permission to scan.

---

**Disclaimer:** This project is provided for educational and informational purposes only. The author is not responsible for any misuse or unlawful use of this tool.
```

Replace `yourusername` in the GitHub badges and URLs with your actual GitHub username and adjust the project structure and content as needed.
