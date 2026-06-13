# Chapter 06 Summary

# 1. Celery - addTask.py

**What I Studied:**
I studied distributed task queues using Celery. I learned how Python functions can be converted into background tasks using a message broker.

**How I Executed:**
I created a Celery app with RabbitMQ broker and defined a task `add(x, y)` using `@app.task`. The function returns the sum of two numbers.

**End Uses:**
Used in background processing, web applications, async job execution, and distributed systems.

**Advantages:**
- Asynchronous task execution
- Scalable architecture
- Easy task definition
- Good for background jobs

**Disadvantages:**
- Requires RabbitMQ/Redis
- Worker must be running
- Complex setup
- Debugging is harder


# 2. Celery - addTask_main.py

**What I Studied:**
I studied how Celery tasks are triggered asynchronously using `.delay()`.

**How I Executed:**
I imported `add` from Celery task file and executed:
`add.delay(5, 5)` to send task to worker.

**End Uses:**
Used for background jobs like email sending, computations, and API task handling.

**Advantages:**
- Non-blocking execution
- Simple task calling
- Improves performance
- Decouples logic

**Disadvantages:**
- Requires worker process
- Broker dependency
- No immediate result
- Harder debugging


# 3. Pyro4 - first example (pyro_server.py)

**What I Studied:**
I studied Remote Procedure Call (RPC) using Pyro4. I learned how Python objects can be exposed over a network.

**How I Executed:**
I created a `Server` class and exposed `welcomeMessage()` using `@Pyro4.expose`. I registered the object with Pyro Name Server as `"server"` and started a daemon.

**End Uses:**
Used in distributed systems where methods are called remotely across machines.

**Advantages:**
- Easy RPC implementation
- Object-oriented remote access
- Name server simplifies discovery
- Clean abstraction

**Disadvantages:**
- Requires name server running
- Network dependency
- Security concerns
- Not very scalable for large systems


# 4. Pyro4 - first example (pyro_client.py)

**What I Studied:**
I studied how a client connects to a Pyro4 remote object using a proxy.

**How I Executed:**
I created a proxy:
`Pyro4.Proxy("PYRONAME:server")`
and called:
`welcomeMessage(name)` to receive response.

**End Uses:**
Used in distributed client-server RPC systems.

**Advantages:**
- Simple remote calls
- No socket handling needed
- Transparent communication
- Easy integration

**Disadvantages:**
- Server must be running
- Name server dependency
- Network latency
- Limited control over communication


# 5. Pyro4 - chainTopology.py

**What I Studied:**
I studied chain topology in distributed systems using Pyro4. I learned how multiple servers pass messages in a chain until it returns to the origin.

**How I Executed:**
Each node checks if it already exists in the message path. If not, it forwards the message to the next server using a Pyro proxy. If it returns to the starting node, the chain closes.

**End Uses:**
Used in pipeline systems, distributed workflows, token-ring communication, and message propagation systems.

**Advantages:**
- Demonstrates distributed chaining
- Good for pipeline design
- Modular structure
- Scalable topology

**Disadvantages:**
- Complex debugging
- Network dependency
- Chain failure breaks system
- Hard to trace execution flow


# 6. Pyro4 - client_chain.py

**What I Studied:**
I studied how a client initiates a distributed chain execution using Pyro name server lookup.

**How I Executed:**
I used:
`Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")`
and called:
`process(["hello"])` to start message propagation.

**End Uses:**
Used to trigger distributed workflows across multiple servers.

**Advantages:**
- Simple entry point
- Uses name server abstraction
- Easy chain execution start
- Clean client logic

**Disadvantages:**
- Requires all servers running
- Name server dependency
- Debugging is difficult
- Network delays affect execution


# 7. Pyro4 - server_chain_1.py

**What I Studied:**
I studied how a node in a distributed chain is implemented using Pyro4.

**How I Executed:**
Server 1 registers itself as `example.chainTopology.1`, connects to server 2, and starts a daemon loop.

**End Uses:**
Used as first node in distributed chain topology.

**Advantages:**
- Independent node
- Modular design
- Easy to scale
- Works in distributed environment

**Disadvantages:**
- Requires coordination
- Name must match exactly
- Dependency on other nodes
- Failure affects chain


# 8. Pyro4 - server_chain_2.py

**What I Studied:**
I studied intermediate node behavior in a Pyro4 chain system.

**How I Executed:**
Server 2 connects to server 3 and processes incoming messages before forwarding.

**End Uses:**
Used as relay node in distributed systems.

**Advantages:**
- Multi-hop communication
- Flexible structure
- Easy to extend
- Works as middleware node

**Disadvantages:**
- Single point failure risk
- Network dependency
- Debugging complexity
- Requires correct routing


# 9. Pyro4 - server_chain_3.py

**What I Studied:**
I studied final node behavior in a circular chain topology.

**How I Executed:**
Server 3 connects back to server 1, completing the loop and forming a circular chain.

**End Uses:**
Used in token-ring systems and circular distributed workflows.

**Advantages:**
- Completes loop structure
- Useful for cyclic workflows
- Scalable topology
- Demonstrates distributed recursion

**Disadvantages:**
- Risk of infinite loops
- Complex debugging
- Requires all nodes active
- Hard to monitor flow


# 10. Socket Programming - client.py

**What I Studied:**
I studied basic TCP socket communication between client and server.

**How I Executed:**
Client connects to server on port 9999 and receives current system time.

**End Uses:**
Used in basic client-server communication systems.

**Advantages:**
- Simple networking
- Lightweight communication
- Easy to implement
- Good learning example

**Disadvantages:**
- Blocking communication
- No concurrency
- Limited functionality
- No error handling


# 11. Socket Programming - client2.py

**What I Studied:**
I studied file transfer using socket programming.

**How I Executed:**
Client connects to server, sends message, receives file data in chunks, and saves it as `received.txt`.

**End Uses:**
Used in file transfer systems and network communication.

**Advantages:**
- Supports file transfer
- Works over TCP
- Simple implementation
- Useful in distributed systems

**Disadvantages:**
- No security/encryption
- Manual file handling
- Blocking I/O
- No error recovery


# 12. Socket Programming - server.py

**What I Studied:**
I studied TCP server handling multiple client connections sequentially.

**How I Executed:**
Server listens on port 9999 and sends current time to clients.

**End Uses:**
Used in time servers and simple APIs.

**Advantages:**
- Simple server design
- Easy to understand
- Lightweight
- Handles multiple connections

**Disadvantages:**
- Blocking server
- No concurrency
- Not scalable
- No authentication


# 13. Socket Programming - server2.py

**What I Studied:**
I studied advanced socket server with file transfer capability.

**How I Executed:**
Server listens on port 60000, receives client request, sends file in chunks, and closes connection.

**End Uses:**
Used in file sharing systems and network services.

**Advantages:**
- File transfer support
- Multi-step communication
- Simple protocol
- Real-world usage model

**Disadvantages:**
- No encryption
- Blocking I/O
- Limited scalability
- Manual protocol handling