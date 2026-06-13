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
