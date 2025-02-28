import socket  
from datetime import datetime  
from colorama import init, Fore, Style  

init(autoreset=True)  
def print_header():  
    print(f"""  
    {Fore.RED}{Style.BRIGHT}  
    ╔═════════════════════════════════════════════════════╗  
    ║              PORT SCANNER TOOL                       ║  
    ║                     by PYTHON_TO_FLY                 ║  
    ╚═════════════════════════════════════════════════════╝  
    """)
def print_footer(duration):
    print(f"""  
    {Fore.MAGENTA}{Style.BRIGHT}  
    ╔══════════════════════════════════════════╗  
    ║            SCAN COMPLETED                ║  
    ╚══════════════════════════════════════════╝  
    {Fore.YELLOW}Time taken: {duration}
    ═══════════════════════════════════════════  
    """)  
def port_scanner(target, start_port, end_port):   
    print(f"{Fore.YELLOW}Scanning ports for {target} in the range {start_port} to {end_port}")  
    start_time = datetime.now()
    try:  
        target_ip = socket.gethostbyname(target)  
    except socket.gaierror:  
        print(f"{Fore.RED}Error: The domain name is not valid.")  
        return  
    print(f"{Fore.GREEN}IP address of {target}: {target_ip}\n")  
    print(f"{Fore.CYAN}Starting port scan...\n")  
    print(f"{Fore.WHITE}-----------------------------------------------")  
    for port in range(start_port, end_port + 1):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        socket.setdefaulttimeout(.25)  
        result = sock.connect_ex((target_ip, port))   
        if result == 0:  
            print(f"{Fore.RED}Port {port} is OPEN       {Fore.WHITE}<< CONNECTION SUCCESS")  
        else:  
            print(f"{Fore.GREEN}Port {port} is CLOSED     {Fore.WHITE}<< NO CONNECTION")  
        sock.close()
        print(f"{Fore.WHITE}-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--")  
    end_time = datetime.now()
    duration = end_time - start_time  
    print_footer(duration)  
if __name__ == "__main__":
    print_header()
    target_host = input("Enter the target IP address or domain name: ")  
    start_port = int(input("Enter the starting port: "))  
    end_port = int(input("Enter the ending port: "))  
    port_scanner(target_host, start_port, end_port)
