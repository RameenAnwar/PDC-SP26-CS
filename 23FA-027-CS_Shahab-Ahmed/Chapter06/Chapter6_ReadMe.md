# Celery Task Creation

# Description
This code demonstrates how to create a simple Celery task that performs addition asynchronously.

## What This Code Does
- Creates a Celery application  
- Connects to RabbitMQ using a broker URL  
- Defines a task named `add()`  
- Accepts two numbers as input  
- Returns the sum of the numbers  

## Execution Flow
1. Import `Celery`  
2. Create Celery application instance  
3. Connect to RabbitMQ broker  
4. Define task using `@app.task` decorator  
5. Task waits for execution requests  
6. Worker executes task when called  

## How to Execute
1. Install Celery:
   ```bash
   pip install celery
   ```

2. Install and start RabbitMQ

3. Start Celery worker:
   ```bash
   celery -A addTask worker --loglevel=info
   ```

4. Run task from another Python file:
   ```python
   import addTask
   result = addTask.add.delay(5, 5)
   ```

## End Use
Used for:
- Background processing  
- Distributed task execution  
- Asynchronous operations  

## When to Use
Use when:
- Tasks take time to execute  
- Background processing is needed  
- Workload should be distributed  

Avoid when:
- Immediate results are required  
- Simple synchronous execution is enough  

## How to Use
1. Create Celery app  
2. Configure broker connection  
3. Define task with `@app.task`  
4. Start worker process  
5. Call task using `.delay()` or `.apply_async()`  

## Advantages
- Asynchronous task execution  
- Scalable architecture  
- Supports distributed workers  

## Disadvantages
- Requires RabbitMQ or Redis  
- Additional setup and configuration  
- More complex than normal functions  

## One-Line Summary
This code creates a Celery task that adds two numbers and can be executed asynchronously by a worker.


# Celery Task Execution

## Description
This code demonstrates how to execute a Celery task asynchronously using `.delay()`.

## What This Code Does
- Imports a Celery task from `addTask.py`  
- Calls the task asynchronously using `delay()`  
- Passes two numbers as arguments (`5` and `5`)  
- Returns a task result object immediately without waiting for execution  

## Execution Flow
1. Import `addTask` module  
2. Call `add.delay(5, 5)`  
3. Celery sends task to the message broker  
4. Worker receives and executes task  
5. Result is stored in the backend  
6. Main program continues without waiting  

## How to Execute
1. Start Redis/RabbitMQ broker  
2. Start Celery worker:
   ```bash
   celery -A addTask worker --loglevel=info
   ```
3. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Background task processing  
- Distributed task execution  
- Asynchronous workloads  

## When to Use
Use when:
- Tasks take a long time to complete  
- Work should run in the background  
- Distributed processing is needed  

Avoid when:
- Immediate results are required  
- Tasks are very small and simple  

## How to Use
1. Define a Celery task  
2. Start a message broker  
3. Start Celery worker  
4. Call task using `.delay()`  
5. Retrieve result if needed  

## Advantages
- Asynchronous execution  
- Scalable and distributed  
- Improves application responsiveness  

## Disadvantages
- Requires broker setup  
- More complex architecture  
- Additional system resources needed  

## One-Line Summary
This program sends a Celery task to execute asynchronously in the background.


#------------------------------------------------------------------------------------------------------------------

# Pyro4 Client Application

## Description
This code demonstrates a Pyro4 client that connects to a remote server and invokes a method remotely.

## What This Code Does
- Takes user input (name)  
- Connects to a Pyro4 server using a Name Server  
- Creates a remote object proxy  
- Calls the server method `welcomeMessage()`  
- Displays the response received from the server  

## Execution Flow
1. Import `Pyro4`  
2. Ask user to enter a name  
3. Connect to remote server using:
   ```python
   Pyro4.Proxy("PYRONAME:server")
   ```
4. Call remote method:
   ```python
   server.welcomeMessage(name)
   ```
5. Receive response from server  
6. Print the returned message  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Start the Pyro4 server

4. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Remote Procedure Calls (RPC)  
- Distributed applications  
- Client-server communication  

## When to Use
Use when:
- Functions need to be executed on a remote machine  
- Building distributed systems  
- Client-server architecture is required  

Avoid when:
- Local execution is sufficient  
- Network communication is unnecessary  

## How to Use
1. Start Pyro Name Server  
2. Register server object  
3. Create client proxy using server name  
4. Call remote methods like local functions  

## Advantages
- Simple remote method calls  
- Easy distributed application development  
- Object-oriented communication  

## Disadvantages
- Requires network connectivity  
- Additional setup for Name Server  
- Communication overhead  

## One-Line Summary
This Pyro4 client connects to a remote server and executes a method using Remote Procedure Calls (RPC).


# Pyro4 Server Application

## Description
This code demonstrates a Pyro4 server that exposes a remote method and waits for client requests.

## What This Code Does
- Creates a server class with a remote method  
- Exposes `welcomeMessage()` for remote access  
- Starts a Pyro daemon  
- Registers the server with the Pyro Name Server  
- Waits for incoming client requests  
- Returns a welcome message to connected clients  

## Execution Flow
1. Create `Server` class  
2. Define remote method `welcomeMessage()`  
3. Create Pyro daemon  
4. Locate Pyro Name Server  
5. Register server object with daemon  
6. Register object name (`server`) in Name Server  
7. Display generated URI  
8. Start request loop and wait for client calls  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Run the server:
   ```bash
   python server.py
   ```

4. Run the client program in another terminal

## End Use
Used for:
- Remote Procedure Calls (RPC)  
- Distributed systems  
- Client-server applications  
- Remote object communication  

## When to Use
Use when:
- Remote method execution is needed  
- Building distributed applications  
- Multiple clients need access to shared services  

Avoid when:
- Local execution is sufficient  
- Network communication is unnecessary  

## How to Use
1. Create server class  
2. Expose methods using `@Pyro4.expose`  
3. Register object with daemon  
4. Register object name with Name Server  
5. Start request loop using `requestLoop()`  
6. Connect through a Pyro4 client  

## Advantages
- Simple RPC implementation  
- Object-oriented communication  
- Easy client-server development  

## Disadvantages
- Requires Name Server setup  
- Network dependency  
- Additional communication overhead  

## One-Line Summary
This Pyro4 server exposes a remote method that clients can call over a network using RPC.


# Pyro4 Chain Topology

## Description
This code demonstrates a Chain Topology using Pyro4, where remote objects forward messages to each other in sequence until the chain is completed.

## What This Code Does
- Defines a remote `Chain` object  
- Connects to another remote server in the chain  
- Receives and forwards messages between servers  
- Tracks visited servers using a message list  
- Detects when the chain returns to the starting server  
- Returns the complete traversal path  

## Execution Flow
1. Create a `Chain` object with:
   - Server name  
   - Next server name  
2. Receive a message list  
3. Connect to the next server using Pyro4 Proxy  
4. Check if current server already exists in message:
   - If yes, chain is complete  
   - If no, continue forwarding  
5. Add current server name to message list  
6. Forward message to next server  
7. Return results through the chain  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Start all chain topology servers

4. Run the client application:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Distributed systems  
- Message routing  
- Network topology simulations  
- Remote object communication  

## When to Use
Use when:
- Messages must pass through multiple servers  
- Distributed workflows are required  
- Network routing behavior is being simulated  

Avoid when:
- Direct client-server communication is sufficient  
- No forwarding logic is needed  

## How to Use
1. Create multiple `Chain` objects  
2. Register each object with Pyro Name Server  
3. Define next server for each node  
4. Send a message to the first node  
5. Allow automatic forwarding through the chain  

## Advantages
- Demonstrates distributed message routing  
- Easy to extend with more nodes  
- Useful for topology simulations  

## Disadvantages
- Network dependency  
- More complex than direct communication  
- Failure of one node can break the chain  

## One-Line Summary
This Pyro4 chain topology forwards messages through multiple remote objects until the chain returns to the starting node.



# Pyro4 Chain Topology Client

## Description
This code demonstrates a Pyro4 client that starts a message traversal through a chain of remote objects.

## What This Code Does
- Connects to the first node in the chain topology  
- Sends an initial message list containing `"hello"`  
- Invokes the remote `process()` method  
- Receives the final traversal result  
- Prints the complete chain path  

## Execution Flow
1. Import Pyro4 library  
2. Create proxy for chain node:
   ```python
   PYRONAME:example.chainTopology.1
   ```
3. Send initial message:
   ```python
   ["hello"]
   ```
4. Remote nodes process and forward the message  
5. Final result is returned to the client  
6. Print the returned chain information  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Start all chain topology server nodes

4. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Testing chain topology  
- Distributed message routing  
- Remote object communication  
- Network simulation  

## When to Use
Use when:
- A client needs to initiate a chain process  
- Testing distributed workflows  
- Verifying communication between nodes  

Avoid when:
- Direct server communication is sufficient  
- No chain traversal is required  

## How to Use
1. Create proxy to first chain node  
2. Call `process()` method  
3. Pass initial message list  
4. Receive and display final result  

## Advantages
- Simple client implementation  
- Demonstrates distributed communication  
- Easy to test chain topology  

## Disadvantages
- Depends on running server nodes  
- Requires Name Server setup  
- Network failures can interrupt execution  

## One-Line Summary
This Pyro4 client starts a message traversal through a chain of remote objects and displays the final result.


# Pyro4 Chain Topology Server

## Description
This code creates a server node in a Pyro4 Chain Topology and registers it with the Pyro Name Server.

## What This Code Does
- Creates a chain node with a current server and next server  
- Registers the node as a remote Pyro object  
- Publishes the object in the Pyro Name Server  
- Waits for incoming requests from clients or other chain nodes  
- Forwards messages to the next server in the chain  

## Execution Flow
1. Import Pyro4 and `chainTopology` module  
2. Define:
   - Current server = `"1"`  
   - Next server = `"2"`  
3. Create server name:
   ```python
   example.chainTopology.1
   ```
4. Create Pyro daemon  
5. Create `Chain` object  
6. Register object with daemon  
7. Locate Pyro Name Server  
8. Register object name and URI  
9. Print startup message  
10. Start request loop using `daemon.requestLoop()`  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Run the server:
   ```bash
   python server1.py
   ```

4. Start remaining chain servers (server2, server3, etc.)

5. Run the client application

## End Use
Used for:
- Distributed systems  
- Chain topology implementation  
- Message forwarding  
- Remote object communication  

## When to Use
Use when:
- Building a chain of interconnected servers  
- Simulating network routing  
- Implementing distributed workflows  

Avoid when:
- Direct client-server communication is enough  
- No message forwarding is required  

## How to Use
1. Create a `Chain` object  
2. Specify current and next server names  
3. Register object with Pyro daemon  
4. Register service in Name Server  
5. Start request loop to accept requests  

## Advantages
- Supports distributed message routing  
- Easy to add more chain nodes  
- Demonstrates RPC-based communication  

## Disadvantages
- Requires multiple server instances  
- Depends on Name Server availability  
- More complex than direct communication  

## One-Line Summary
This Pyro4 server acts as a node in a chain topology and forwards messages to the next remote server.



# Pyro4 Chain Topology Server 2

## Description
This code creates the second server node in a Pyro4 Chain Topology and forwards messages to Server 3.

## What This Code Does
- Creates a chain node with current server `"2"`  
- Sets next server as `"3"`  
- Registers the node as a remote Pyro object  
- Publishes the service in the Pyro Name Server  
- Waits for requests from other chain nodes  
- Forwards messages to the next server in the chain  

## Execution Flow
1. Import Pyro4 and `chainTopology` module  
2. Set:
   - Current server = `"2"`  
   - Next server = `"3"`  
3. Create service name:
   ```python
   example.chainTopology.2
   ```
4. Create Pyro daemon  
5. Create `Chain` object  
6. Register object with daemon  
7. Locate Pyro Name Server  
8. Register object name and URI  
9. Print startup message  
10. Start request loop using `daemon.requestLoop()`  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Run the server:
   ```bash
   python server2.py
   ```

4. Ensure Server 1 and Server 3 are also running

5. Run the client application

## End Use
Used for:
- Distributed systems  
- Chain topology communication  
- Message forwarding between nodes  
- Remote procedure calls (RPC)  

## When to Use
Use when:
- Building multi-node communication chains  
- Simulating routing behavior  
- Creating distributed workflows  

Avoid when:
- Direct communication is sufficient  
- No chain forwarding is required  

## How to Use
1. Define current and next server IDs  
2. Create a `Chain` object  
3. Register it with Pyro daemon  
4. Register service in Name Server  
5. Start request loop to handle incoming messages  

## Advantages
- Supports scalable chain topologies  
- Easy node-to-node communication  
- Demonstrates distributed RPC concepts  

## Disadvantages
- Requires multiple running servers  
- Dependent on Name Server  
- Failure of one node affects the chain  

## One-Line Summary
This Pyro4 server represents the second node in a chain topology and forwards messages to Server 3.



# Pyro4 Chain Topology Server 3

## Description
This code creates the third server node in a Pyro4 Chain Topology and forwards messages back to Server 1, completing the chain.

## What This Code Does
- Creates a chain node with current server `"3"`  
- Sets next server as `"1"`  
- Registers the node as a remote Pyro object  
- Publishes the service in the Pyro Name Server  
- Waits for incoming requests  
- Forwards messages back to Server 1 to complete the topology loop  

## Execution Flow
1. Import Pyro4 and `chainTopology` module  
2. Set:
   - Current server = `"3"`  
   - Next server = `"1"`  
3. Create service name:
   ```python
   example.chainTopology.3
   ```
4. Create Pyro daemon  
5. Create `Chain` object  
6. Register object with daemon  
7. Locate Pyro Name Server  
8. Register object name and URI  
9. Print startup message  
10. Start request loop using `daemon.requestLoop()`  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Run the server:
   ```bash
   python server3.py
   ```

4. Ensure Server 1 and Server 2 are also running

5. Run the client application

## End Use
Used for:
- Distributed systems  
- Ring/chain topology implementation  
- Message routing simulation  
- Remote procedure calls (RPC)  

## When to Use
Use when:
- Building cyclic communication topologies  
- Simulating network routing paths  
- Testing distributed workflows  

Avoid when:
- Direct communication is sufficient  
- No multi-node communication is needed  

## How to Use
1. Define current and next server IDs  
2. Create a `Chain` object  
3. Register object with Pyro daemon  
4. Register service in Name Server  
5. Start request loop to handle requests  

## Advantages
- Completes the chain topology loop  
- Supports distributed message routing  
- Demonstrates RPC communication across nodes  

## Disadvantages
- Requires all chain nodes to be active  
- Dependent on Name Server availability  
- Failure of one server can break the chain  

## One-Line Summary
This Pyro4 server acts as the third node in the chain topology and forwards messages back to Server 1, completing the communication loop.


#------------------------------------------------------------------------------------------------------------------

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
