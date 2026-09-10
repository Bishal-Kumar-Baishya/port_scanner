import socket
import colorama 
from concurrent.futures import ThreadPoolExecutor

colorama.init(autoreset=True)

def scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        if ( s.connect_ex((ip, port)) == 0 ):
            try:
                s.sendall(b"\r\n")
                banner = s.recv(1024).decode("utf-8", errors="replace").strip()
                print(colorama.Fore.GREEN + f"[+] Port {port} is open, with banner {banner}")

            except (socket.timeout, ConnectionResetError, OSError):
                print(colorama.Fore.GREEN + f"[+] Port {port} is open (No banner)")

    except socket.error:
        print(colorama.Fore.RED + f"[-] Network issue")

    finally:
        s.close()

def get_IP(): 
    while True: 
        IP_addr = input("Enter a IP to scan: ")
        try:
            socket.gethostbyname(IP_addr)
            return IP_addr

        except socket.gaierror:
            print(colorama.Fore.RED + f"Enter a valid IP address!")
            continue

def main():
    ip = get_IP()

    with ThreadPoolExecutor(max_workers=200) as pool:
        pool.map(lambda p: scan(ip, p), range(1,1025))

if __name__ == "__main__": 
    print(colorama.Fore.CYAN + "[*] Starting port scanner...") 
    main()