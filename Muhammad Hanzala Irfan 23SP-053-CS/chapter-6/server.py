import socket
import time

# Create a new socket using AF_INET (IPv4) and SOCK_STREAM (TCP)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

# Set the port number
port = 9999

# Bind the socket to host and port
serversocket.bind((host, port))

# Listen for incoming connections (max 5 in queue)
serversocket.listen(5)

print("Server is listening on port", port)

while True:
    # Accept a connection; returns (socket, address)
    clientsocket, addr = serversocket.accept()

    print("Connected with [addr],[port] %s" % str(addr))

    # Get the current time
    currentTime = time.ctime(time.time()) + "\r\n"

    # Send the current time to the client
    clientsocket.send(currentTime.encode('ascii'))

    # Close the client socket
    clientsocket.close()