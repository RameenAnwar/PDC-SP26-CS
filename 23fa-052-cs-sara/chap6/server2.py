

# Import socket library for network communication
import socket

# Set port number for server to listen on
port = 60000

# Create a socket object 
s = socket.socket()

# Get local machine name (computer name)
host = socket.gethostname()

# Bind socket to host and port 
s.bind((host, port))

# Start listening for connections
# 15 = maximum 15 clients can wait in queue
s.listen(15)

# Print message that server is ready
print('Server listening....')

# Infinite loop - server runs forever
while True:
    
    # Accept a client connection
    # conn = new socket for this client
    # addr = client's address (IP, port)
    conn, addr = s.accept()
    
    # Print client address when connected
    print('Got connection from', addr)
    
    # Receive data from client (max 1024 bytes)
    # This is usually a request or filename
    data = conn.recv(1024)
    
    # Print what client sent
    print('Server received', repr(data.decode()))
    
    # Filename to send to client
    filename = 'mytext.txt'
    
    # Open file in binary mode for reading
    f = open(filename, 'rb')
    
    # Read first 1024 bytes of file
    l = f.read(1024)
    
    # Loop while there is data to read
    while (l):
        # Send chunk of file to client
        conn.send(l)
        print('Sent', repr(l.decode()))
        
        # Read next 1024 bytes
        l = f.read(1024)
    
    # Close the file
    f.close()
    
    # Print message that sending is done
    print('Done sending')
    
    # Send thank you message to client
    conn.send('-> Thank you for connecting'.encode())
    
    # Close connection with this client
    conn.close()
# output:
# Server listening....

# [Server is now waiting for client connections on port 60000]
# Server listening....

# Got connection from ('127.0.0.1', 54322)

# Server received 'Hello Server!'

# Sent 'This is line 1 of mytext.txt file'
# Sent 'This is line 2 of mytext.txt file'
# Sent 'This is line 3 of mytext.txt file'

# Done sending
    