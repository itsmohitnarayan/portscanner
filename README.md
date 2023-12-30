---

# PORT SCANNER

This is an advanced port scanner written in Python. The scanner utilizes multithreading to scan ports concurrently, providing faster results. Users can input the target, start port, end port, and the number of threads for parallel scanning.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [License](#license)

## Introduction

This Python Simple Port Scanner is a command-line tool that allows you to scan a target host or IP address for open ports within a specified range. It utilizes multithreading to improve scanning speed and efficiently check multiple ports simultaneously.

## Features

- Scan a target host or IP address for open ports.
- Specify a range of ports to scan.
- Utilizes multithreading for faster scanning.
- Displays open ports if found during the scan.
- **Multithreading:** Utilizes threading for parallel port scanning.
- **User Input:** Takes user input for the target, start port, end port, and number of threads.
- **Concurrent Scanning:** Scans multiple ports concurrently for faster results.

## Prerequisites

- Python 3.x
- Required Python libraries (socket, threading, queue)

## How to Use

1. Clone the repository or download the `portscanner.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `portscanner.py`.
4. Run the script using the following command:

    ```bash
    python portscanner.py
    ```

5. Follow the prompts to enter the target, start port, end port, and number of threads.

## Example

```bash
python portscanner.py

- Advanced Python Port Scanner
Enter the target (IP address or hostname): example.com
Enter the starting port: 1
Enter the ending port: 100
Enter the number of threads: 5
Scanning target example.com from port 1 to 100 using 5 threads
Port 22 is OPEN
Port 80 is OPEN
...
Scan completed. Shutting down program.
```

## License

This project is open-source and is provided under the MIT License. You are free to use, modify, and distribute the code as needed, following the terms of the MIT License.

