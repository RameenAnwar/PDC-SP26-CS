# server.py
# Import the built-in socket library for networking and time library for fetching system clock data
import socket
import time

# Create a new server socket object 'serversocket'
# socket.AF_INET specifies IPv4 addressing scheme
# socket.SOCK_STREAM specifies TCP, ensuring reliable data delivery
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Automatically retrieve the local machine's hostname or network name
host = socket.gethostname()

# Define a specific network port number (9999) where this service will be hosted
port = 9999

# Bind/assign the socket to the specific host address and port number combination so traffic can route here
serversocket.bind((host, port))

# Put the server into listening mode, setting the backlog queue to allow up to 5 pending connection requests
serversocket.listen(5)

# Start an infinite loop to continuously accept and process incoming client connections
while True: 
    # Block execution and wait for a client request; returns a new socket object for communication and the client's address
    clientsocket, addr = serversocket.accept()
    
    # Print a tracking log to the server console showing the IP address and source port of the connected client
    print("Connected with[addr],[port]%s" % str(addr))
    
    # Get the current system time, convert it into a readable string format, and append standard network carriage return lines (\r\n)
    currentTime = time.ctime(time.time()) + "\r\n"
    
    # Send the time string to the connected client after encoding it into raw binary 'ascii' bytes
    clientsocket.send(currentTime.encode('ascii'))
    
    # Close the dedicated client socket to end the session cleanly since the data has been delivered
    clientsocket.close()