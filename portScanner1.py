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

def log_results(port, is_open):  
    with open("port_scan_results.txt", "a") as log_file:  
        status = "OPEN" if is_open else "CLOSED"  
        log_file.write(f"Port {port} is {status}\n") 
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

    total_ports = end_port - start_port + 1  
    for index, port in enumerate(range(start_port, end_port + 1)):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        socket.setdefaulttimeout(0.25) 
        try:  
            result = sock.connect_ex((target_ip, port))   
            is_open = result == 0  

            if is_open:  
                print(f"{Fore.RED}Port {port} is OPEN       {Fore.WHITE}<< CONNECTION SUCCESS")  
            else:  
                print(f"{Fore.GREEN}Port {port} is CLOSED     {Fore.WHITE}<< NO CONNECTION")  

            log_results(port, is_open) 
        except Exception as e:  
            print(f"{Fore.RED}Error: Couldn't connect to port {port}. Reason: {str(e)}")  
        finally:  
            sock.close()  

        progress = (index + 1) / total_ports * 100  
        print(f"{Fore.WHITE}Progress: {progress:.2f}%")  
        
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