# Chapter # 6

---

## Celery

### 1. addTask.py

**Description:**
Defines a simple Celery task that adds two numbers. Celery is a distributed task queue that allows running tasks asynchronously using a message broker like RabbitMQ or Redis.

**How it Works:**
- `Celery('addTask', broker='amqp://...')` creates a Celery app connected to RabbitMQ broker
- `@app.task` decorator registers `add()` as a Celery task
- Task takes two numbers x and y and returns their sum

**Result:**
Registers `add` as an async task that can be called remotely via message broker.

**Advantages:**
- Tasks run asynchronously — main program doesn't wait
- Can distribute tasks across multiple workers
- Supports task scheduling and retries

**Disadvantages:**
- Requires RabbitMQ or Redis broker to be running
- Complex setup compared to simple function calls
- Overkill for small applications

**Where to Use:**
- Background job processing in web applications
- Email sending, report generation, data processing tasks
- Any long-running task that shouldn't block the main program

---

### 2. addTask_main.py

**Description:**
Calls the Celery `add` task asynchronously using `.delay()` — the task is sent to the broker queue and executed by a worker.

**How it Works:**
- Imports `addTask` module
- `addTask.add.delay(5, 5)` sends task to broker queue asynchronously
- Worker picks up task from queue and executes it
- Main program continues without waiting for result

**Result:**
Task is queued and executed by Celery worker — returns AsyncResult object.

**Advantages:**
- `.delay()` is simplest way to call async task
- Main program is not blocked
- Task result can be retrieved later if needed

**Disadvantages:**
- Requires Celery worker and broker to be running
- No immediate result — need to check AsyncResult later

**Where to Use:**
- Triggering background tasks from web requests
- Offloading heavy computation to worker processes

---

## Pyro4 — First Example

### 3. pyro_server.py

**Description:**
Creates a Pyro4 remote object server — exposes a `welcomeMessage` method that clients can call remotely over the network.

**How it Works:**
- `Server` class with `@Pyro4.expose` decorator makes method accessible remotely
- `Pyro4.Daemon()` creates server daemon
- `Pyro4.locateNS()` connects to Pyro name server
- Object registered with name "server" in name server
- `daemon.requestLoop()` starts listening for client calls

**Result:**
Server starts and prints its URI, waits for client connections and responds with welcome message.

**Advantages:**
- Simple way to expose Python objects as remote services
- Name server makes discovery easy — no hardcoded IPs
- Supports any Python object method remotely

**Disadvantages:**
- Requires Pyro name server to be running separately
- Not suitable for cross-language communication
- Python only

**Where to Use:**
- Distributed Python applications
- Remote procedure calls between Python processes
- Microservices written entirely in Python

---

### 4. pyro_client.py

**Description:**
Connects to the Pyro4 server using name server lookup and calls `welcomeMessage` method remotely.

**How it Works:**
- Takes user name as input
- `Pyro4.Proxy("PYRONAME:server")` looks up server in name server
- Calls `server.welcomeMessage(name)` as if it were a local function
- Prints the response received from remote server

**Result:**
Prints "Hi welcome [name]" received from the remote server.

**Advantages:**
- Remote call looks exactly like local function call
- Name server lookup avoids hardcoded server address
- Simple one-line proxy setup

**Disadvantages:**
- Server and name server must be running before client
- Network errors not handled in this basic example

**Where to Use:**
- Client side of any distributed Python application
- Calling remote Python services from local scripts

---

## Pyro4 — Second Example (Chain Topology)

### 5. chainTopology.py

**Description:**
Defines a `Chain` class that implements a chain topology — each node forwards a message to the next node until it comes back to the starting node.

**How it Works:**
- Each `Chain` object knows its own name and next server name
- `process()` checks if current node name is already in message
- If not — appends name to message and forwards to next server
- If yes — chain is complete, returns result
- Uses Pyro4 proxy to communicate with next server

**Result:**
Message travels through chain of servers (1→2→3→1) collecting node names until it returns to starting node.

**Advantages:**
- Clean chain pattern — each node only knows its neighbor
- Easy to extend by adding more nodes
- Demonstrates distributed object communication

**Disadvantages:**
- All servers must be running before client sends message
- Circular dependency can cause issues if a server goes down

**Where to Use:**
- Distributed pipeline processing
- Chain of responsibility pattern in distributed systems
- Message passing between multiple remote nodes

---

### 6. server_chain_1.py / server_chain_2.py / server_chain_3.py

**Description:**
Three server scripts that each run one node of the chain topology. Each server registers itself with the Pyro name server and forwards messages to the next server in chain.

**How it Works:**
- Each server creates a `Chain` object with its number and next server number
- Registers with name server as `example.chainTopology.N`
- `daemon.requestLoop()` starts listening for incoming calls
- Server 1 → Server 2 → Server 3 → back to Server 1

**Result:**
Each server starts and prints its name, waits for messages and forwards them to next node.

**Advantages:**
- Each server is independent — can run on different machines
- Easy to add more servers by following same pattern
- Clean separation of each node's logic

**Disadvantages:**
- All three servers must be running simultaneously
- Name server must also be running
- Complex startup process

**Where to Use:**
- Distributed pipeline where each stage runs on different machine
- Chain of processing nodes in parallel systems

---

### 7. client_chain.py

**Description:**
Client that initiates the chain topology by sending a message to server 1 and receiving the complete chain result.

**How it Works:**
- Creates proxy to `example.chainTopology.1` (server 1)
- Calls `process(["hello"])` to start the chain
- Message travels through all servers and returns
- Prints complete result showing path through all nodes

**Result:**
Prints chain result showing message passed through all nodes — "passed on from 1", "passed on from 2", "passed on from 3", "complete at 1".

**Advantages:**
- Single call triggers entire chain automatically
- Result shows complete path message took through chain

**Disadvantages:**
- All servers must be running before client call
- Long chain increases latency

**Where to Use:**
- Testing distributed chain topology
- Triggering multi-stage distributed pipelines

---

## Socket

### 8. server.py

**Description:**
Basic TCP socket server that accepts client connections and sends current time to each connected client.

**How it Works:**
- Creates TCP socket with `AF_INET` (IPv4) and `SOCK_STREAM` (TCP)
- Binds to hostname and port 9999
- Listens for up to 5 connections
- On each connection — sends current timestamp and closes connection
- Runs in infinite loop accepting new clients

**Result:**
Prints connected client address and sends current time string to each client.

**Advantages:**
- Simple and lightweight — no external libraries needed
- Works with any TCP client
- Easy to understand basic socket communication

**Disadvantages:**
- Single-threaded — handles one client at a time
- No error handling for disconnections
- Not suitable for production use

**Where to Use:**
- Learning basic TCP socket programming
- Simple time or data server for local network
- Foundation for building more complex network apps

---

### 9. client.py

**Description:**
Basic TCP socket client that connects to the time server and receives current time.

**How it Works:**
- Creates TCP socket and connects to server hostname on port 9999
- Receives up to 1024 bytes from server
- Decodes received bytes and prints the time
- Closes connection after receiving

**Result:**
Prints "Time connection server: [current time]" received from server.

**Advantages:**
- Simple 5-line client — easy to understand
- No external dependencies needed

**Disadvantages:**
- Hardcoded port — must match server
- No error handling if server is not running

**Where to Use:**
- Testing socket server connectivity
- Simple data retrieval from local network server

---

### 10. server2.py

**Description:**
File transfer server — reads a text file and sends its contents to any connected client over TCP socket.

**How it Works:**
- Binds to port 60000 and listens for connections
- On connection — reads `mytext.txt` in chunks of 1024 bytes
- Sends each chunk to client until file is fully sent
- Sends thank you message and closes connection

**Result:**
Sends contents of mytext.txt to connected client and prints each sent chunk.

**Advantages:**
- Demonstrates file transfer over sockets
- Chunk-based sending handles large files efficiently

**Disadvantages:**
- File name hardcoded — only sends mytext.txt
- Single-threaded — one client at a time
- Bug: `f.close()` inside while loop closes file too early

**Where to Use:**
- Basic file sharing over local network
- Learning file transfer using sockets

---

### 11. client2.py

**Description:**
File transfer client — connects to server2 and receives file contents, saving them to a local file.

**How it Works:**
- Connects to server on port 60000
- Sends "HelloServer!" message to initiate transfer
- Receives data in 1024 byte chunks in a loop
- Writes each chunk to `received.txt`
- Closes file and connection when transfer complete

**Result:**
Creates `received.txt` with contents received from server, prints each chunk as it arrives.

**Advantages:**
- Saves received data directly to file
- Loop handles large files in chunks

**Disadvantages:**
- No progress indicator for large files
- No error handling if connection drops mid-transfer

**Where to Use:**
- Receiving files over local network
- Learning client-side socket file transfer

---

## Socket — Celery Tasks

### 12. addTask.py (socket folder)

**Description:**
Same as Celery addTask but uses `pyamqp` broker URL format. Defines an `add` task using Celery connected to RabbitMQ.

**How it Works:**
- Creates Celery app named 'tasks' with pyamqp broker
- `@app.task` registers `add(x, y)` as async task
- Returns sum of x and y when executed by worker

**Result:**
Registers add task with Celery — ready to be called asynchronously.

**Advantages:**
- Same as Celery addTask — async task execution
- `pyamqp` is more explicit broker URL format

**Disadvantages:**
- Requires RabbitMQ broker running
- Worker must be started separately

**Where to Use:**
- Background addition tasks in distributed system
- Testing Celery setup with simple math task

---

### 13. addTask_main.py (socket folder)

**Description:**
Calls the Celery add task asynchronously — same pattern as Celery folder but imports from socket folder's addTask.

**How it Works:**
- Imports `add` function from `addTask`
- `add.delay(5, 5)` sends task to broker queue
- Task executed asynchronously by Celery worker

**Result:**
Task queued for async execution — worker computes 5+5=10 in background.

**Advantages:**
- Simple demonstration of async task calling
- Non-blocking execution

**Disadvantages:**
- Requires running broker and worker
- No result retrieved in this example

**Where to Use:**
- Triggering async tasks from main application
- Testing Celery task queue setup

---