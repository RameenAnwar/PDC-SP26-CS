# Chapter 06

## 1. Celery – Asynchronous Task Queue System

### Purpose
Celery is used to execute tasks in the background without blocking the main program. It is mainly used for handling heavy or time-consuming operations efficiently.

### How to Use
- Define a Celery app with a message broker (RabbitMQ/Redis)
- Create tasks using `@app.task`
- Run worker process separately
- Call tasks using `.delay()` or `.apply_async()`

### Concepts Covered
- Asynchronous programming
- Producer–consumer model
- Message broker system
- Task queue architecture
- Distributed worker system

### Advantages
- Improves application performance
- Non-blocking execution
- Scalable architecture
- Efficient task distribution

### Disadvantages
- Requires external broker setup
- Complex configuration
- Debugging is difficult
- Overhead for small applications

---

## 2. Pyro4 – Remote Method Invocation (RMI)

### Purpose
Pyro4 allows remote objects to be accessed and used over a network as if they are local objects.

### How to Use
- Create a server object and expose methods
- Register object with Pyro daemon
- Use Name Server for object lookup
- Access remote methods using `Pyro4.Proxy()`

### Concepts Covered
- Remote Procedure Call (RPC)
- Distributed object communication
- Client-server architecture
- Name server registry system
- Network-based method invocation

### Advantages
- Easy remote communication
- Object-oriented approach
- Reduces network complexity
- Transparent remote calling

### Disadvantages
- Network dependency
- Security vulnerabilities if not secured
- Requires Name Server setup
- Slower than local execution

---

## 3. Pyro4 Chain Topology (Distributed Ring System)

### Purpose
To demonstrate message passing between multiple distributed nodes in a circular (ring) structure.

### How to Use
- Create multiple Pyro servers (nodes)
- Each node connects to the next node
- Send a message from first node
- Message circulates until it returns to origin

### Concepts Covered
- Distributed system topology
- Message passing mechanism
- Ring/chain architecture
- Workflow pipeline system
- Node-to-node communication

### Advantages
- Useful for workflow modeling
- Demonstrates distributed coordination
- Good for sequential processing systems

### Disadvantages
- Failure of one node affects system
- Difficult to debug loops
- Not efficient for large networks
- Latency increases with nodes

---

## 4. Socket Programming – Client Server Model

### Purpose
Socket programming is used for low-level network communication between client and server using TCP/IP protocol.

### How to Use
- Create socket object
- Bind server to IP and port
- Listen and accept connections
- Use send/receive methods for communication

### Concepts Covered
- TCP/IP communication
- Client-server architecture
- Socket-based networking
- Stream-based data transfer
- File and time sharing systems

### Advantages
- Full control over communication
- Lightweight and fast
- Suitable for real-time systems
- Flexible implementation

### Disadvantages
- Low-level complexity
- Manual error handling required
- Not scalable for large systems
- Security must be handled manually

---
## Final Conclusion
This chapter covers the fundamentals of distributed systems in Python, including task distribution (Celery), remote method invocation (Pyro4), distributed topology (chain system), and low-level networking (socket programming). These concepts together form the foundation of modern network-based and distributed applications.