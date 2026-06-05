# TCP Socket Client in Python

## Description
This code demonstrates a simple TCP client that connects to a server, receives data, and displays it.

## What This Code Does
- Creates a TCP socket  
- Connects to a server using hostname and port number  
- Receives data from the server  
- Closes the connection  
- Prints the received message (current time from server)  

## Execution Flow
1. Create a TCP socket using:
   ```python
   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ```
2. Get local machine hostname  
3. Connect to server on port `9999`  
4. Receive up to 1024 bytes of data  
5. Close socket connection  
6. Decode received data and print output  

## How to Execute
1. Start the socket server first  
2. Open terminal in this folder  
3. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Client-server communication  
- Network programming  
- Receiving data from remote servers  
- Distributed applications  

## When to Use
Use when:
- A client needs to communicate with a server  
- Data must be received over a network  
- Building TCP-based applications  

Avoid when:
- No network communication is required  
- Local processing is sufficient  

## How to Use
1. Create a socket object  
2. Connect to server using `connect()`  
3. Receive data using `recv()`  
4. Close connection using `close()`  
5. Process received data  

## Advantages
- Simple client-server communication  
- Reliable data transfer using TCP  
- Easy to implement  

## Disadvantages
- Requires a running server  
- Network delays may occur  
- Connection errors must be handled  

## One-Line Summary
This TCP socket client connects to a server, receives data, and displays the server response.



# TCP Socket File Transfer Client

## Description
This code demonstrates a TCP client that connects to a server, receives a file, and saves it locally.

## What This Code Does
- Creates a socket connection to a server  
- Sends a request message (`HelloServer!`)  
- Receives file data from the server  
- Stores received data in `received.txt`  
- Closes the connection after file transfer is complete  

## Execution Flow
1. Create a socket object  
2. Connect to server on port `60000`  
3. Send greeting message:
   ```python
   HelloServer!
   ```
4. Open `received.txt` in write-binary mode  
5. Receive data in chunks of 1024 bytes  
6. Write received data into the file  
7. Stop when no more data is received  
8. Close file and socket connection  

## How to Execute
1. Start the file server first  
2. Open terminal in this folder  
3. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- File transfer applications  
- Client-server communication  
- Downloading files from servers  
- Network-based file sharing  

## When to Use
Use when:
- Files need to be transferred over a network  
- A client must download data from a server  
- Building file-sharing applications  

Avoid when:
- No file transfer is required  
- Local file access is sufficient  

## How to Use
1. Create a socket connection  
2. Send request to server  
3. Open destination file  
4. Receive data using `recv()`  
5. Write data to file  
6. Close file and connection  

## Advantages
- Simple file transfer implementation  
- Reliable TCP communication  
- Can handle large files in chunks  

## Disadvantages
- Requires active server connection  
- No error handling for failed transfers  
- Transfer speed depends on network performance  

## One-Line Summary
This TCP socket client downloads a file from a server and saves it locally as `received.txt`.



# TCP Socket Time Server

## Description
This code demonstrates a simple TCP server that sends the current system time to connected clients.

## What This Code Does
- Creates a TCP server socket  
- Binds the server to port `9999`  
- Listens for incoming client connections  
- Accepts client requests continuously  
- Sends the current date and time to the client  
- Closes the client connection after sending data  

## Execution Flow
1. Create a TCP socket  
2. Get local machine hostname  
3. Bind socket to port `9999`  
4. Start listening for connections using `listen(5)`  
5. Wait for a client connection using `accept()`  
6. Get current system time  
7. Send time to the client  
8. Close client connection  
9. Continue waiting for new clients  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python server.py
   ```
3. Run the client program in another terminal

## End Use
Used for:
- Client-server communication  
- Network programming practice  
- Time synchronization services  
- TCP server implementation learning  

## When to Use
Use when:
- Multiple clients need information from a server  
- Building network-based applications  
- Learning socket programming  

Avoid when:
- No network communication is required  
- Local execution is sufficient  

## How to Use
1. Create server socket  
2. Bind using `bind()`  
3. Start listening using `listen()`  
4. Accept connections using `accept()`  
5. Send data using `send()`  
6. Close client connection after processing  

## Advantages
- Simple TCP server implementation  
- Supports multiple client connections  
- Reliable communication using TCP  

## Disadvantages
- Handles clients sequentially  
- No concurrency support  
- Limited error handling  

## One-Line Summary
This TCP socket server waits for client connections and sends the current system time to each connected client.



# TCP Socket File Transfer Server

## Description
This code demonstrates a TCP server that sends a file to a connected client.

## What This Code Does
- Creates a TCP server socket  
- Waits for client connections on port `60000`  
- Receives a request from the client  
- Opens `mytext.txt` file  
- Sends file contents to the client in chunks  
- Sends a final thank-you message  
- Closes the connection  

## Execution Flow
1. Create a socket object  
2. Bind socket to port `60000`  
3. Start listening for client requests  
4. Accept a client connection  
5. Receive client message  
6. Open `mytext.txt` in binary mode  
7. Read file data in chunks of 1024 bytes  
8. Send file data to client using `send()`  
9. Send completion message  
10. Close client connection  

## How to Execute
1. Place `mytext.txt` in the same folder  
2. Open terminal in this folder  
3. Run:
   ```bash
   python server.py
   ```
4. Run the client program from another terminal

## End Use
Used for:
- File transfer systems  
- Client-server communication  
- Network file sharing  
- Data distribution over TCP  

## When to Use
Use when:
- Files need to be shared across a network  
- A server must send data to clients  
- Building file transfer applications  

Avoid when:
- File sharing is not required  
- Local file access is sufficient  

## How to Use
1. Create server socket  
2. Bind to a port  
3. Listen for incoming clients  
4. Open file in binary mode  
5. Send file contents using `send()`  
6. Close connection after transfer  

## Advantages
- Simple file transfer implementation  
- Reliable data delivery with TCP  
- Supports large file transfer in chunks  

## Disadvantages
- Handles one client at a time  
- Limited error handling  
- No encryption or security features  

## One-Line Summary
This TCP socket server sends the contents of a file to connected clients over a TCP connection.
