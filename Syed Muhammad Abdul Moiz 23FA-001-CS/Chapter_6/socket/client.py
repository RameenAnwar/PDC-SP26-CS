# client.py
# Import the built-in socket library to enable low-level network communications
import socket

# Create a new socket object 's'
# socket.AF_INET specifies that we are using IPv4 addresses
# socket.SOCK_STREAM specifies that we are using TCP (reliable, connection-oriented protocol)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Automatically fetch the host name or network identity of the local computer running this script
host = socket.gethostname()

# Define the network port number on which the server is actively listening (must match the server's port)
port = 9999

# Initiate a TCP connection request to the server using the designated host address and port number tuple
s.connect((host, port))

# Block execution and wait to receive incoming data from the server (up to a maximum buffer size of 1024 bytes)
tm = s.recv(1024)

# Close the socket connection to free up the system's network resources and ports
s.close()

# Decode the raw binary stream data received from the server into a human-readable 'ascii' string and print it
print("Time connection server:%s" % tm.decode('ascii'))