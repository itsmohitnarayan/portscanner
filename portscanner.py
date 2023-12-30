import socket
import threading
from queue import Queue

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    
    if result == 0:
        print(f"Port {port} is OPEN")

def worker(target, port_queue):
    while True:
        port = port_queue.get()
        if port is None:
            break
        scan_port(target, port)
        port_queue.task_done()

def scan_ports(target, start_port, end_port, num_threads):
    print(f"Scanning target {target} from port {start_port} to {end_port} using {num_threads} threads")

    port_queue = Queue()

    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(target, port_queue))
        thread.start()
        threads.append(thread)

    port_queue.join()

    for _ in range(num_threads):
        port_queue.put(None)

    for thread in threads:
        thread.join()

def main():
    print("-" * 70)
    print("Advanced Port Scanner")
    print("-" * 70)

    target = input("Enter the target (IP address or hostname): ").strip()
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    num_threads = int(input("Enter the number of threads: "))

    scan_ports(target, start_port, end_port, num_threads)

if __name__ == "__main__":
    main()
