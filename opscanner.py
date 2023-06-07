import socket
import os

def main():
    # Set the target IP address or hostname
    target = input("IP address or hostname:")  # Replace with the target IP address or hostname
    # Define a range of ports to scan
    print("Enter range of ports:\n")
    range_start = int(input("Start: "))
    range_end = int(input("End: "))
    # Replace with the desired range of ports to scan
    port_range = range(range_start, range_end) 

    
    def check_port(port):
        # Creates a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        # Attempt to connect to the port 
        result = sock.connect_ex((target, port))  

        if result == 0:
            print(f"Port {port} is open")
        
        sock.close()

    # Iterate over the range of ports
    for port in port_range:
        check_port(port)
        
    
if __name__ == "__main__":
    os.system("cls")
    print("Open Port Scanner version 1.0")
    main()
