# Import the built-in socket library to handle low-level network communications
import socket

# Create a default socket object 's' 
# By default, without arguments, it initializes as an IPv4 (AF_INET) and TCP (SOCK_STREAM) socket
s = socket.socket()

# Automatically retrieve the local machine's hostname/network identity
host = socket.gethostname()

# Define the network port number (60000) where the file transfer server is listening
port = 60000

# Establish a TCP connection to the server using the host and port tuple
s.connect((host, port))

# Send an initial greeting/handshake string 'HelloServer!' to the server after encoding it into bytes
s.send('HelloServer!'.encode())

# Open (or create) a local file named 'received.txt' in 'wb' (write binary) mode
# The 'with' statement ensures the file is safely managed and automatically flushed
with open('received.txt', 'wb') as f:
    print('file opened')
    
    # Start an infinite loop to read incoming data streams continuously from the network socket
    while True:
        print('receiving data...')
        
        # Read the incoming data stream chunk in packets of up to 1024 bytes
        data = s.recv(1024)
        
        # If 'data' is empty, it means the server has finished sending the file and closed the connection
        if not data:
            # Exit the infinite loop immediately
            break
            
        # Decode the binary chunk into a human-readable string and display it in the console
        print('Data=>', data.decode())
        
        # Write the raw binary chunk directly into the open 'received.txt' file
        f.write(data)

# Inform the user that the loop ended and the entire file has been completely downloaded
print('Successfully get the file')

# Explicitly close the socket link to free up system port 60000 and network resources
s.close()
print('connection closed')