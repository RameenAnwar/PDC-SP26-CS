# Chapter 6: Distributed Python

## Introduction
Distributed computing refers to a system where multiple computers or processes work together over a network to solve a problem. Python provides several tools and libraries to build distributed applications — from low-level **socket programming** for direct network communication, to high-level frameworks like **Celery** for distributed task queues and **Pyro4** for remote object communication. This chapter explores how Python programs can communicate, share work, and coordinate across different machines or processes over a network.

## Advantages
- Tasks can be distributed across multiple machines for massive scalability
- Independent services can run on separate machines and communicate over a network
- Fault tolerance — if one node fails, others can continue
- Enables microservices and cloud-based architectures
- Celery and Pyro4 abstract away low-level networking complexity

## Disadvantages
- More complex to set up and debug than local parallel programs
- Network latency can reduce performance
- Requires careful handling of failures, timeouts, and retries
- Security concerns when exposing services over a network
- Dependencies on external services (message brokers, name servers) add overhead

## Requirements
```
pip install celery pyro4
```
- Celery requires a message broker like **RabbitMQ** (`amqp://guest@localhost//`)
- Pyro4 requires a running **Pyro name server** (`python -m Pyro4.naming`)

---

## Topics Covered

---

### 1. Socket Programming — Time Server (`server.py` / `client.py`)

#### Description
Implements a basic **client-server** communication using Python's `socket` module. The server binds to a port, listens for connections, and sends the current time to any client that connects. The client connects to the server, receives the time string, and prints it.

#### Key Concepts
- `socket.socket(AF_INET, SOCK_STREAM)` — creates a TCP socket
- `socket.gethostname()` — gets the local machine name
- `serversocket.bind((host, port))` — binds the server to an address and port
- `serversocket.listen(5)` — listens for up to 5 queued connections
- `serversocket.accept()` — accepts an incoming connection
- `clientsocket.send()` / `s.recv()` — sends and receives data

#### Advantages
- Very lightweight, no external libraries needed
- Full control over the communication protocol
- Works across any network (local or internet)

#### Disadvantages
- Low-level — developer must handle all protocol details manually
- No built-in support for encryption or authentication
- Harder to scale to many simultaneous clients

#### Use Cases
- Simple client-server applications
- Custom network protocols
- IoT device communication
- Chat applications and real-time data streaming

---

### 2. Socket Programming — File Transfer (`server_file.py` / `client_file.py`)

#### Description
Extends socket communication to transfer a file from server to client. The server reads a file (`mytext.txt`) in chunks of 1024 bytes and sends it over the socket. The client receives the chunks and writes them to a new file (`received.txt`). After transfer, the server sends a thank-you message.

#### Key Concepts
- `f.read(1024)` — reads file in chunks to handle large files
- `conn.send(l)` — sends binary data over socket
- `s.recv(1024)` — receives data in chunks
- `open('received.txt', 'wb')` — writes received binary data to file
- Loop continues until no more data is received (`if not data: break`)

#### Advantages
- Can transfer files of any size using chunked reading
- Simple and dependency-free
- Works over any TCP network

#### Disadvantages
- No error handling or checksum verification
- No progress tracking for large files
- Vulnerable to partial transfers if connection drops

#### Use Cases
- File sharing between machines on a network
- Sending logs or reports from remote servers
- Backup and data synchronization tools

---

### 3. Celery — Distributed Task Queue (`addTask.py` / `addTask_run.py` / `tasks.py`)

#### Description
Demonstrates distributed task execution using **Celery**. A simple `add(x, y)` function is decorated with `@app.task` and registered with Celery using RabbitMQ as the message broker. The client calls `add.delay(5, 5)` which sends the task to a worker process asynchronously. The worker executes it independently and returns the result.

#### Key Concepts
- `Celery('appName', broker='amqp://guest@localhost//')` — creates a Celery app with a broker
- `@app.task` — registers a function as a distributed task
- `add.delay(x, y)` — sends the task to a worker asynchronously
- The broker (RabbitMQ) acts as a message queue between client and worker
- Workers run separately and process tasks from the queue

#### Advantages
- Tasks run asynchronously without blocking the main program
- Easy to scale by adding more workers
- Built-in support for retries, scheduling, and monitoring
- Works across multiple machines

#### Disadvantages
- Requires a running message broker (RabbitMQ or Redis)
- More complex setup compared to simple threading
- Overkill for small or simple applications

#### Use Cases
- Background job processing (sending emails, generating reports)
- Distributed data processing pipelines
- Scheduled and periodic tasks (cron-like jobs)
- Microservice task delegation

---

### 4. Pyro4 — Remote Objects (`server_pyro.py` / `client_pyro.py`)

#### Description
Uses **Pyro4** (Python Remote Objects) to expose a Python object as a remote service. The server creates a `Server` class with a `welcomeMessage()` method, registers it with Pyro's name server, and waits for calls. The client connects using `Pyro4.Proxy()` and calls the method as if it were a local object.

#### Key Concepts
- `@Pyro4.expose` — marks a method as remotely callable
- `Pyro4.Daemon()` — creates a Pyro server daemon
- `Pyro4.locateNS()` — finds the running Pyro name server
- `daemon.register(obj)` — registers an object with the daemon
- `ns.register("name", uri)` — registers the object in the name server
- `Pyro4.Proxy("PYRONAME:server")` — client connects to remote object by name

#### Advantages
- Call remote methods just like local Python methods
- Name server handles address resolution automatically
- Clean and Pythonic API for distributed objects

#### Disadvantages
- Requires a running Pyro name server
- Not suitable for cross-language communication
- Less commonly used compared to REST or gRPC in modern systems

#### Use Cases
- Distributed Python applications on a local network
- Remote procedure calls between Python services
- Building simple distributed systems without REST APIs

---

### 5. Pyro4 — Chain Topology (`chainTopology.py` / `server_1.py` / `server_2.py` / `server_3.py` / `client_chain.py`)

#### Description
Implements a **chain topology** using Pyro4 where three server objects (1 → 2 → 3 → 1) are connected in a ring. A message is passed from one server to the next. Each server forwards the message to the next in the chain and records its name. When the message returns to the starting server, the chain is complete. The client initiates the chain by calling `process(["hello"])` on server 1.

#### Key Concepts
- Each `Chain` object knows its own name and the name of the next server
- `Pyro4.core.Proxy("PYRONAME:example.chainTopology.X")` — connects to next server
- `message.append(self.name)` — each server adds itself to the message
- When the originating server's name is found in the message, the chain is closed
- Three separate server scripts (`server_1.py`, `server_2.py`, `server_3.py`) run independently

#### Advantages
- Demonstrates real distributed object communication across multiple processes
- Chain pattern is extensible — easy to add more nodes
- Each server is independent and loosely coupled

#### Disadvantages
- All three servers and the name server must be running simultaneously
- Complex to set up and debug
- A failure in any node breaks the entire chain

#### Use Cases
- Pipeline processing where each stage transforms data and passes it on
- Distributed workflow engines
- Token ring network simulations
- Middleware and message routing systems

