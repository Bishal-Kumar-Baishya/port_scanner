import socket

ip_addr = input("Enter the ip address: ")

i = 1
while (i != 1025):
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((ip_addr, i))

    if (result == 0):
        print(f"Port {i} is open")

    i += 1
    s.close()