# Chapter 06 : Distributed Computing using Celery, Pyro4 and Socket Programming

# CELERY EXAMPLES

## 1. addTask.py

### What I learned

This file creates a Celery application and defines a distributed task named `add()`. The task can be executed asynchronously through a message broker.

### How to execute

Start RabbitMQ service first.

```bash
celery -A addTask worker --loglevel=info
```

### End use

Used for background processing and distributed task execution.

### When and how to use

Used when time-consuming operations should execute separately from the main application.

### Summary

Basic Celery task implementation.

### Advantages

* Asynchronous execution
* Scalable architecture
* Better performance

### Disadvantages

* Requires RabbitMQ or Redis
* Additional setup required

---

## 2. addTask_main.py

### What I learned

This file sends a task request to Celery workers using the `delay()` method.

### How to execute

```bash
python addTask_main.py
```

### End use

Used to submit tasks to Celery workers.

### When and how to use

Used whenever background processing is needed.

### Summary

Celery task producer.

### Advantages

* Simple task invocation
* Non-blocking execution

### Disadvantages

* Requires active worker process

---

# PYRO4 EXAMPLES

## 3. pyro_server.py

### What I learned

This program creates a Pyro4 server and registers a remote object with the Pyro Name Server. The server provides a method called `welcomeMessage()`.

### How to execute

Start Pyro Name Server:

```bash
pyro4-ns
```

Then start server:

```bash
python pyro_server.py
```

### End use

Used to provide remote services through RPC.

### When and how to use

Used when applications need to access methods running on another machine or process.

### Summary

Basic Pyro4 server implementation.

### Advantages

* Easy RPC implementation
* Object-oriented communication

### Disadvantages

* Requires Name Server

---

## 4. pyro_client.py

### What I learned

This client connects to the Pyro server and remotely invokes the `welcomeMessage()` function.

### How to execute

```bash
python pyro_client.py
```

### End use

Used to access server-side functionality remotely.

### When and how to use

Used in distributed applications requiring remote object communication.

### Summary

Basic Pyro4 client.

### Advantages

* Easy remote method invocation
* Minimal code

### Disadvantages

* Depends on server availability

---

# PYRO4 CHAIN TOPOLOGY EXAMPLE

## 5. chainTopology.py

### What I learned

This file contains the core logic of chain topology. Each server forwards a received message to another server until the chain completes.

### How to execute

Used internally by chain servers.

### End use

Used for studying distributed message passing.

### When and how to use

Used when requests must travel through multiple processing nodes.

### Summary

Chain routing logic implementation.

### Advantages

* Demonstrates distributed communication
* Shows message propagation

### Disadvantages

* Failure of one node affects the chain

---

## 6. server_chain_1.py

### What I learned

Acts as the first node of the chain and forwards requests to Server 2.

### How to execute

```bash
python server_chain_1.py
```

### End use

Entry point of chain topology.

### When and how to use

Used for distributed routing experiments.

### Summary

Chain node 1.

### Advantages

* Demonstrates message forwarding

### Disadvantages

* Dependent on next node

---

## 7. server_chain_2.py

### What I learned

Acts as the second node in the chain and forwards requests to Server 3.

### How to execute

```bash
python server_chain_2.py
```

### End use

Intermediate processing node.

### When and how to use

Used in chain-based communication models.

### Summary

Chain node 2.

### Advantages

* Supports distributed communication

### Disadvantages

* Additional network overhead

---

## 8. server_chain_3.py

### What I learned

Acts as the final node and forwards requests back to Server 1 to complete the chain.

### How to execute

```bash
python server_chain_3.py
```

### End use

Final node in chain communication.

### When and how to use

Used to study circular message routing.

### Summary

Chain node 3.

### Advantages

* Demonstrates complete chain processing

### Disadvantages

* Debugging becomes difficult in larger chains

---

## 9. client_chain.py

### What I learned

This client starts the communication process and receives the final response after passing through all chain servers.

### How to execute

```bash
python client_chain.py
```

### End use

Used to test chain topology.

### When and how to use

Used during distributed system experimentation.

### Summary

Chain topology client.

### Advantages

* Demonstrates full workflow

### Disadvantages

* All servers must be running

---

# SOCKET PROGRAMMING EXAMPLES

## 10. server.py

### What I learned

This server sends the current date and time to connected clients.

### How to execute

```bash
python server.py
```

### End use

Used to understand basic client-server communication.

### When and how to use

Used in introductory networking applications.

### Summary

Simple socket time server.

### Advantages

* Easy to understand
* Basic networking concepts

### Disadvantages

* Limited functionality

---

## 11. client.py

### What I learned

This client connects to the server and receives the current system time.

### How to execute

```bash
python client.py
```

### End use

Used to receive information from a server.

### When and how to use

Used when learning TCP client implementation.

### Summary

Socket time client.

### Advantages

* Lightweight communication

### Disadvantages

* Depends on server availability

---

## 12. server2.py

### What I learned

This server transfers the contents of a text file (`mytext.txt`) to connected clients.

### How to execute

```bash
python server2.py
```

### End use

Used for file transfer applications.

### When and how to use

Used when files need to be shared over a network.

### Summary

Socket file transfer server.

### Advantages

* Demonstrates file transmission
* Practical networking example

### Disadvantages

* No encryption
* No authentication

---

## 13. client2.py

### What I learned

This client receives the file sent by the server and saves it as `received.txt`.

### How to execute

```bash
python client2.py
```

### End use

Used to download files from a server.

### When and how to use

Used in basic file-sharing applications.

### Summary

Socket file transfer client.

### Advantages

* Simple implementation
* Demonstrates file reception

### Disadvantages

* No security controls

---

## 14. mytext.txt

### What I learned

Contains sample text data used by the file transfer server.

### End use

Acts as the source file for transmission.

### Summary

Input file used in file-sharing demonstration.

---

## 15. received.txt

### What I learned

This file stores the contents received from the server.

### End use

Output file generated after successful file transfer.

### Summary

Received file generated by the client.

---