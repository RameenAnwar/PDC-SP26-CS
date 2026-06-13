# Import the socket module for network communication
import socket

# Create a default TCP socket (AF_INET, SOCK_STREAM are defaults)
s = socket.socket()

# Get the local machine's hostname (same machine as server)
host = socket.gethostname()

# Define the port number the server is listening on
port = 60000

# Connect to the server at the given host and port
s.connect((host, port))

# Send an initial message to the server (e.g., requesting a file)
# .encode() converts the string to bytes
s.send('HelloServer!'.encode())

# Open a file named 'received.txt' in binary write mode
# This file will store the data received from the server
with open('received.txt', 'wb') as f:
    print('file opened')
    
    # Continuously receive data from the server
    while True:
        print('receiving data...')
        
        # Receive up to 1024 bytes from the socket
        data = s.recv(1024)
        
        # If no data is received, the server has closed the connection
        if not data:
            break
        
        # Print the received data (decoded to string for display)
        print('Data=>', data.decode())
        
        # Write the received binary data to the file
        f.write(data)

# Explicitly close the file (not strictly needed inside 'with' block)
f.close()

# Print success message
print('Successfully get the file')

# Close the socket connection
s.close()

# Print connection closed message
print('connection closed')