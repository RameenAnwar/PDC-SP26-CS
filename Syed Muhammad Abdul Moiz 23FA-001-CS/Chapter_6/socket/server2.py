# server .py

# Import the built-in socket library to handle low-level network communications
import socket

# Define the network port number (60000) where this application will host its service
port = 60000

# Create a default socket object 's' (initializes automatically as an IPv4 TCP socket)
s = socket.socket()

# Automatically fetch the host name or network identity of the local computer running this script
host = socket.gethostname()

# Bind/assign the socket configuration to the specific host address and port 60000 combo
s.bind((host, port))

# Put the server into active listening mode, allowing a queue backlog of up to 15 pending connections
s.listen(15)
print('Server listening....')

# Start an infinite loop to keep the server continuously up and running for incoming client links
while True:
    # Block execution until a client connects; returns a new socket 'conn' for the session and client 'addr'
    conn, addr = s.accept()
    print('Got connection from', addr)
    
    # Receive the initial handshake greeting from the client (up to 1024 bytes)
    data = conn.recv(1024)
    # Print the raw representation of the decoded string message received from the client
    print('Server received', repr(data.decode()))
    
    # Define the local target file name that the server intends to send over the network
    filename = 'mytext.txt'
    
    # Open the file 'mytext.txt' in 'rb' (read binary) mode to read raw bytes securely
    f = open(filename, 'rb')
    
    # Read the first chunk of data from the file (up to 1024 bytes)
    l = f.read(1024)
    
    # Start a loop to read and send the file data in blocks as long as data exists ('l' is not empty)
    while (l):
        # Send the current 1024-byte chunk over the network socket to the connected client
        conn.send(l)
        # Print a verification tracking statement showing exactly what data block was just transmitted
        print('Sent', repr(l.decode()))
        
        # Read the next 1024-byte chunk from the file to continue processing the loop
        l = f.read(1024)
        
    # Close the file system resource safely after the entire file has been read completely
    f.close()
    print('Donesending')
    
    # Send a final encoded string message thanking the client for the socket transaction
    conn.send('->Thank you for connecting'.encode())
    
    # Safely shut down and close the active client session socket connection after all communication ends
    conn.close()