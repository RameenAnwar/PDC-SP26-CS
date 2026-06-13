# Chapter 06

---

## 1. Celery – Asynchronous Task Queue System

### Purpose

Celery is used to run tasks in the background so the main program does not stop or slow down. It is mainly helpful for handling long-running or heavy processes in an efficient way.

### How to Use

- Set up a Celery application with a message broker (RabbitMQ/Redis)
- Define tasks using `@app.task` decorator
- Start worker process separately from the main program
- Execute tasks using `.delay()` or `.apply_async()`

### Concepts Covered

- Asynchronous execution
- Producer–consumer model
- Message broker communication
- Task queue system
- Distributed worker processing

### Advantages

- Improves overall application speed
- Non-blocking execution flow
- Easily scalable system
- Efficient task handling

### Disadvantages

- Needs external broker setup
- Configuration can be complicated
- Debugging is not very simple
- Not suitable for small/simple projects

---

## 2. Pyro4 – Remote Method Invocation (RMI)

### Purpose

Pyro4 is used to access and call functions of remote objects over a network as if they are local functions.

### How to Use

- Create a server object and expose its methods
- Register the object using Pyro daemon
- Use Name Server to locate objects
- Call remote methods using `Pyro4.Proxy()`

### Concepts Covered

- Remote Procedure Calls (RPC)
- Distributed object communication
- Client-server architecture
- Name server lookup mechanism
- Network-based method execution

### Advantages

- Simple remote communication
- Object-oriented design approach
- Hides network complexity
- Easy to use remote function calls

### Disadvantages

- Depends on stable network connection
- Security issues if not handled properly
- Requires Name Server setup
- Slower compared to local calls

---

## 3. Pyro4 Chain Topology (Distributed Ring System)

### Purpose

This model is used to show how messages are passed between multiple connected nodes in a circular (ring-like) structure.

### How to Use

- Create multiple Pyro nodes (servers)
- Connect each node to the next one
- Send a message from the first node
- Message travels through all nodes until it returns

### Concepts Covered

- Distributed system structure
- Message passing technique
- Ring/chain network topology
- Workflow pipeline processing
- Node-to-node communication

### Advantages

- Useful for workflow-based systems
- Shows distributed coordination clearly
- Good for sequential processing tasks

### Disadvantages

- One node failure can break system flow
- Hard to debug in circular loops
- Not suitable for large-scale systems
- Delay increases with number of nodes

---

## 4. Socket Programming – Client Server Model

### Purpose

Socket programming is used for direct communication between client and server using TCP/IP protocol.

### How to Use

- Create a socket connection
- Bind server to a specific IP and port
- Listen for incoming client requests
- Use send and receive functions for data transfer

### Concepts Covered

- TCP/IP networking
- Client-server communication model
- Socket-based data transfer
- Stream communication
- File and time sharing systems

### Advantages

- Full control over network communication
- Lightweight and fast execution
- Useful for real-time applications
- Flexible implementation

### Disadvantages

- Low-level programming complexity
- Requires manual error handling
- Not easily scalable
- Security must be handled by developer

---

## Final Conclusion

This chapter explains the basic ideas of distributed systems using Python. It includes background task execution (Celery), remote method calling (Pyro4), chain-based distributed communication, and low-level networking using sockets. Together, these concepts help in understanding how modern network-based systems work.
