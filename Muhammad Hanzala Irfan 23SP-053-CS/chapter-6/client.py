import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

# Set the port number
port = 9999

# Connect to the server
s.connect((host, port))

# Receive up to 1024 bytes from the server
tm = s.recv(1024)

# Close the connection
s.close()

print("Time connection server: %s" % tm.decode('ascii'))