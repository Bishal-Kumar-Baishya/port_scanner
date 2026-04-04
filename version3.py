import threading
import socket
import sys

def scan_port(ip_addr, port):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        result = s.connect_ex((ip_addr, port))
        if (result == 0):
            try:
                banner = s.recv(1024).decode()
                print(f"Port {port} is open, with banner {banner}")
                
            except:
                print(f"Port {port} is open, No banner")

    except socket.error:
        print("Network/Internet issue")

    finally:
        s.close()


def get_target():
    ip_addr = input("Enter the ip address: ")

    try:
        socket.gethostbyname(ip_addr)

    except socket.gaierror:
        print("Enter a valid ip address")
        sys.exit()

    return ip_addr


def main():
    ip = get_target()
    i = 1
    while (i != 1025):
        t = threading.Thread(target=scan_port, args=(ip, i))
        t.start()
        i += 1

if __name__ == "__main__":
    print("Starting port scanner")
    main()