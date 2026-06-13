# server2.py - A TCP server that sends a file to any connecting client

import socket

# Define the port number (must match client)
port = 60000

# Create a default TCP socket (AF_INET, SOCK_STREAM)
s = socket.socket()

# Get the local machine's hostname
host = socket.gethostname()

# Bind the socket to the host and port
s.bind((host, port))

# Listen for incoming connections, allow up to 15 pending connections
s.listen(15)

print('Server listening....')

# Infinite loop: keep accepting clients
while True:
    # Accept a new client connection
    conn, addr = s.accept()
    print('Got connection from', addr)

    # Receive initial data from the client (e.g., "HelloServer!")
    data = conn.recv(1024)
    print('Server received', repr(data.decode()))

    # Name of the file to send
    filename = 'mytext.txt'

    # Open the file in binary read mode
    f = open(filename, 'rb')

    # Read and send the file in chunks of 1024 bytes
    l = f.read(1024)
    while l:
        conn.send(l)                     # send chunk
        print('Sent', repr(l.decode()))  # print chunk as string
        l = f.read(1024)                 # read next chunk

    # Close the file after all data sent
    f.close()
    print('Done sending')

    # Send a final thank‑you message
    conn.send('-> Thank you for connecting'.encode())

    # Close the client connection
    conn.close()

#     output
# Server listening...
# Got connection from ('127.0.0.1', 36520)
# Server received 'HelloServer!'
# Sent 'hello!!!'
# Done sending