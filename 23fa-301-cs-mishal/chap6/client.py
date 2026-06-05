# client.py - A simple TCP client that connects to a time server

# Import the socket module for network communication
import socket

# Create a socket object
# AF_INET = IPv4 address family, SOCK_STREAM = TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine's hostname (e.g., "localhost" or actual name)
host = socket.gethostname()

# Define the port number the server is listening on
port = 9999

# Connect to the server at the given host and port
s.connect((host, port))

# Receive data from the server (up to 1024 bytes)
# This call blocks until data arrives
tm = s.recv(1024)

# Close the socket connection
s.close()

# Print the received time string
# .decode('ascii') converts bytes to ASCII string
print("Time connection server: %s" % tm.decode('ascii'))

# output
# Time connection server:Fri Jun 5 11:06:03 2026
