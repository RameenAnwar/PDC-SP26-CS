# server.py - A simple TCP server that sends the current time to connected clients

# Import the socket module for network communication
import socket
# Import the time module to get the current time
import time

# Create a TCP socket object (IPv4, TCP protocol)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine's hostname (e.g., "localhost" or actual name)
host = socket.gethostname()

# Define the port number the server will listen on
port = 9999

# Bind the socket to the host and port so it can accept connections
serversocket.bind((host, port))

# Start listening for incoming connections
# The argument 5 is the maximum number of queued connections (backlog)
serversocket.listen(5)

# Infinite loop: keep accepting and handling clients
while True:
    # Accept a new client connection
    # clientsocket is a new socket object for communicating with the client
    # addr is the client's address (IP and port)
    clientsocket, addr = serversocket.accept()
    
    # Print the client's address when connected
    # Note: There's a slight formatting error; correct would be f"{addr}" or similar
    print("Connected with [addr],[port]%s" % str(addr))
    
    # Get the current time as a human-readable string, add a newline
    currentTime = time.ctime(time.time()) + "\r\n"
    
    # Send the time string to the client (encode to bytes)
    clientsocket.send(currentTime.encode('ascii'))
    
    # Close the client socket (one connection = one time response)
    clientsocket.close()

    #output
    # Connected with[addr],[port]('127.0.0.1', 33340)