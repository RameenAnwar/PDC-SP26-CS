# Chapter 06 – Distributed Computing

## Folder 1: CELERY
### 1) addTask.py
This file demonstrates creating a simple distributed task using Celery, where a function is registered as a task that can be executed asynchronously by a worker.

- **Celery**: A distributed task queue that runs functions asynchronously across workers.
- `Celery('addTask', broker='amqp://guest@localhost//')` creates a Celery app using RabbitMQ as the message broker.
- `@app.task` registers the `add(x, y)` function as a Celery task.
- Workers connected to the broker pick up and execute the task independently.

**Advantages:**
- Offloads work to background workers, freeing the main program.
- Easy to scale by adding more workers.

**Disadvantages:**
- Requires a running message broker (RabbitMQ) to work.
- Overkill for simple tasks that don't need distribution.

**Time behavior:**
- Task execution time depends on worker availability and broker speed.

### 2) addTask_main.py
This file is the entry point that triggers the Celery task defined in `addTask.py`.

- Imports `addTask` and calls `addTask.add.delay(5, 5)` to send the task to the broker.
- `.delay()` is a shortcut for submitting the task asynchronously without waiting for the result.
- The main program continues immediately after submitting, not waiting for completion.

**Advantages:**
- Non-blocking task submission keeps the main program responsive.

**Disadvantages:**
- No result is retrieved or checked here, so errors go unnoticed.

## Folder 2: PYRO4

### First Example
#### 1) pyro_server.py
This file creates a remote object server using Pyro4, exposing a method that clients can call over the network.

- **Pyro4**: A library that lets you call methods on remote Python objects as if they were local.
- `Server` class has a `welcomeMessage(name)` method decorated with `@Pyro4.expose` to make it accessible remotely.
- `Pyro4.Daemon()` creates the server; `Pyro4.locateNS()` finds the name server.
- The object is registered in the name server as `"server"` so clients can look it up by name.
- `daemon.requestLoop()` starts the server and waits for incoming calls.

**Advantages:**
- Makes remote method calls feel like local function calls.
- Name server removes the need to hardcode IP addresses.

**Disadvantages:**
- Requires a Pyro4 name server to be running separately.
- Not suitable for cross-language communication.

**Time behavior:**
- Server runs indefinitely waiting for client connections.

#### 2) pyro_client.py
This file connects to the Pyro4 server and calls the remote method.

- `Pyro4.Proxy("PYRONAME:server")` looks up the server object by name from the name server.
- Calls `server.welcomeMessage(name)` remotely and prints the returned greeting.
- The remote call looks identical to a local method call.

**Advantages:**
- Simple and readable client code.
- No need to manage sockets or protocols manually.

**Disadvantages:**
- Fails if the name server or server process is not already running.


### Second Example
#### 1) chainTopology.py
This file defines the `Chain` class, which represents a node in a circular chain of Pyro4 objects.

- Each `Chain` object has a name and knows the name of the next server in the chain.
- `process(message)` checks if the current node's name is already in the message.
- If yes, the chain has completed a full loop and returns a completion message.
- If no, it forwards the message to the next server and prepends its own name to the result.
- This creates a circular chain where messages travel from server to server until they return to the origin.

**Advantages:**
- Clean demonstration of chained distributed object communication.
- Easy to extend by adding more nodes to the chain.

**Disadvantages:**
- Circular chains can loop indefinitely if termination logic fails.
- Every node must be running for the chain to work.

**Time behavior:**
- Execution time grows with the number of hops in the chain.


#### 2) client_chain.py
This file starts the chain by sending an initial message to server 1.

- Connects to `example.chainTopology.1` via Pyro4 proxy.
- Calls `process(["hello"])` to start the message passing through the chain.
- Prints the full result showing every server the message passed through.


#### 3) server_chain_1.py / server_chain_2.py / server_chain_3.py
These three files each start one node in the chain topology.

- Each server registers itself with the Pyro4 name server under its own name (e.g. `example.chainTopology.1`).
- Each knows the name of the next server: 1 forwards to 2, 2 forwards to 3, 3 forwards back to 1.
- All three must be running simultaneously for the chain to function.
- `daemon.requestLoop()` keeps each server alive waiting for calls.


## Folder 3: SOCKET
### 1) client.py
This file connects to `server.py` and receives the current time from it.

- Creates a TCP socket and connects to the server using hostname and port 9999.
- `s.recv(1024)` receives up to 1024 bytes from the server.
- Decodes and prints the received timestamp, then closes the connection.

**Advantages:**
- Minimal client code that clearly shows the connect-receive-close pattern.

**Disadvantages:**
- Hardcoded port and no reconnection logic if the server is unavailable.

### 2) client2.py
This file connects to `server2.py`, sends a message, and saves the received file to disk.

- Connects to port 60000 and sends `'HelloServer!'` to trigger the file transfer.
- Opens `received.txt` in write mode and saves incoming data in chunks.
- Breaks out of the loop when no more data is received.
- Prints progress messages throughout and closes the connection cleanly.

**Advantages:**
- Shows full file download over a socket from scratch.
- Handles data in chunks so it works for large files too.

**Disadvantages:**
- No checksum or verification that the file was received correctly.

### 3) server.py
This file creates a basic TCP server that sends the current time to any connected client.

- `socket.socket(AF_INET, SOCK_STREAM)` creates a TCP socket.
- `bind()` and `listen(5)` set up the server to accept up to 5 queued connections.
- For each connection, the server sends the current timestamp using `time.ctime()` and closes the connection.
- Runs in an infinite loop accepting new clients continuously.

**Advantages:**
- Simple and lightweight server with no external dependencies.
- Demonstrates the full server lifecycle: bind, listen, accept, send, close.

**Disadvantages:**
- Handles one client at a time, not suitable for concurrent connections.
- No error handling for dropped connections.

**Time behavior:**
- Each client connection is handled instantly and closed right away.

### 4) server2.py
This file creates a TCP server that receives a message from a client and sends back the contents of a text file.

- Binds to port 60000 and waits for connections.
- On connection, reads the client's message and opens `mytext.txt`.
- Sends the file contents in 1024-byte chunks using a loop.
- Appends a thank-you message at the end before closing the connection.

**Advantages:**
- Demonstrates file transfer over a socket connection.
- Chunked reading handles files of any size.

**Disadvantages:**
- Handles only one client at a time.
- `f.close()` is inside the while loop which may cause issues on large files.

**Time behavior:**
- Transfer time depends on file size and network speed.


