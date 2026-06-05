
# Import socket library for network communication
import socket

# Create a socket object 
# AF_INET = Use IPv4 internet address
# SOCK_STREAM = Use TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name (your computer's name)
# This could be "localhost" or "DESKTOP-7OAL6MQ"
host = socket.gethostname()

# Set port number (must match server's port)
# Port 9999 is where server is listening
port = 9999

# Connect to the server (like dialing a phone number)
# Waits until server accepts connection
s.connect((host, port))

# Receive data from server
# recv(1024) = receive maximum 1024 bytes of data
# This line WAITS until data arrives
tm = s.recv(1024)

# Close the connection (hang up the phone)
s.close()

# Print the received message
# .decode('ascii') converts bytes to readable text
# % tm.decode('ascii') inserts the message into the string
print("Time connection server:%s" % tm.decode('ascii'))
# output:

# Time connection server:Current time: 2026-06-05 20:30:25
