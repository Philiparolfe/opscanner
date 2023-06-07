# Open Port Scanner
This script is a simple Open Port Scanner written in Python. It allows you to scan a range of ports on a target IP address or hostname and determine if they are open or closed.

# Prerequisites
Python 3.x
socket module (should be available in the standard library)
# Usage
Clone or download the script to your local machine.
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script using the command python open_port_scanner.py.
Enter the target IP address or hostname when prompted.
Specify the range of ports you want to scan by providing the starting and ending port numbers.
The script will iterate over the specified port range and display the open ports, if any.
Please note that this script requires proper authorization and should be used for legal and ethical purposes only.

# Example
```
$ python open_port_scanner.py
Open Port Scanner version 1.0
IP address or hostname: example.com
Enter range of ports:
Start: 1
End: 100

Port 22 is open
Port 80 is open
Port 443 is open
``` python
# Notes
The script utilizes the socket module to create a socket object and attempt connections to the specified ports.
A timeout of 1 second is set for each connection attempt.
If a connection is successful (result code 0), the script will print that the port is open.
The script is designed to be a basic implementation and may not account for all scenarios or handle errors extensively.
Please use this script responsibly and ensure you have the necessary permissions before scanning any target network or system.
