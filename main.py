import socket
from datetime import datetime
import pyfiglet
import sys
from termcolor import colored
import subprocess

s_time = datetime.now().strftime('%H:%M:%S')

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# define the target: do this as a command line argument
if len(sys.argv) == 2:
    # translate the hostname to ipv4
    target_address = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid argument amount ~ python main.py 192.168.0.1")

open_ports = []

# add a banner
print("-" * 50)
print(f"[*]Scanning Target Host: {target_address}")
print("-" * 50)

try:
    # scan every port from 1 to 65535
    for ports in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # will return an error indicator
        result = sock.connect_ex((target_address, ports))
        if result == 0: # if there's no exception then the port is open
            print("port", end=' ')
            print(colored(f"[+] {ports}", 'green'), end=' ') # end will allow us to merge prints onto one line!
            print("is open!")
            open_ports.append(ports)
            sock.close()
        else:
            print("port", end=' ')
            print(colored(f"[-] {ports}", 'red'), end=' ')
            print("is closed!")

except socket.gaierror as gerror:
    print("Host name cannot be resolved!")
    sys.exit()
except socket.error as serror:
    print("Server stopped responding!")
    sys.exit()
except KeyboardInterrupt as kerror:
    print(open_ports)
    print("exiting application...")

print(f"List of open ports on network {target_address}: ", end=' ')
print(colored(f"{open_ports}", 'green'))








            
