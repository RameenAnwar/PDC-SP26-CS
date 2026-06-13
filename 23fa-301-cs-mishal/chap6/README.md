# Distributed Computing – Part 1 (Sections 1–5)

## 1. What is Distributed Computing?

**Definition:**  
A distributed system is a collection of independent computers (or processes) that work together to solve a problem. They communicate by passing messages over a network.

### Distributed vs. Parallel Computing

| Feature             | Parallel Computing                  | Distributed Computing                |
| ------------------- | ----------------------------------- | ------------------------------------ |
| Hardware            | One powerful system (shared memory) | Many separate systems                |
| Communication speed | Extremely fast (via shared memory)  | Slower (over network)                |
| Expandability       | Limited (by physical hardware)      | Almost unlimited (add more machines) |
| Example             | Multi-core CPU                      | Cluster of computers, cloud          |

---

## 2. Benefits of Distributed Computing

| Benefit           | Explanation                                                               |
| ----------------- | ------------------------------------------------------------------------- |
| Shared data       | Multiple users / applications can access the same data from anywhere.     |
| Load distribution | Work is split across many machines, so no single machine gets overloaded. |
| Concurrent usage  | Many clients can use the system at the same time without waiting.         |

**Cost (disadvantage):**  
Higher complexity – especially managing communication between parts. You must handle message delays, failures, and synchronization.

---

## 3. Types of Distributed Applications

### 🔹 Client‑Server Applications (2‑tier)

**How it works:**

- Client starts a request (e.g., asks for a web page).
- Server waits for requests and sends back a response.
- Server **cannot** start a transaction by itself – it only replies.
- Both can run on the same machine (as different processes) or on separate machines.

**Implemented using:** Network sockets (Python’s `socket` module).

**Common examples:**  
Websites, email, file transfer (FTP), chat applications.

### 🔹 Multi‑Level (Multi‑Tier) Applications

**Why?** To reduce load on the server by splitting work into layers.

**Typical 3‑Tier Model:**

| Tier | Name                            | What it does                             |
| ---- | ------------------------------- | ---------------------------------------- |
| 1    | Frontend / Presentation Tier    | User interface (web/mobile app, browser) |
| 2    | Middle Tier / Application Logic | Business rules, processing, calculations |
| 3    | Backend / Data Tier             | Database and persistent storage          |

**General software layer terms (often used):**

- **PL** = Presentation Layer
- **BLL** = Business Logic Layer
- **DAL** = Data Access Layer

**Example: An online store**

- Frontend = product pages, shopping cart
- Middle tier = payment processing, inventory check
- Backend = database of products and orders

---

## 4. Socket Programming Basics (Python)

**What is a socket?**  
A socket is an endpoint for communication between two machines (or two processes on the same machine). It’s like a telephone line.

### Important Socket Functions (Python's `socket` module)

| Function                                | Description                                                  | Used by |
| --------------------------------------- | ------------------------------------------------------------ | ------- |
| `socket.socket(family, type, protocol)` | Creates a socket. `AF_INET` = IPv4, `SOCK_STREAM` = TCP      | Both    |
| `bind(address)`                         | Associates socket with a (host, port)                        | Server  |
| `listen()`                              | Starts listening for incoming connections                    | Server  |
| `accept()`                              | Waits for a client; returns a **new socket** for that client | Server  |
| `connect(address)`                      | Connects to a server at given (host, port)                   | Client  |
| `send()` / `recv()`                     | Send or receive data                                         | Both    |
| `close()`                               | Closes the socket and ends communication                     | Both    |

**Example: IP address and port**

- `127.0.0.1` = localhost (same machine)
- `33340` = a random port assigned by the OS for the client

---

## 5. Stream Sockets (TCP) vs. Datagram Sockets (UDP)

| Feature      | TCP (Stream)                                | UDP (Datagram)                                   |
| ------------ | ------------------------------------------- | ------------------------------------------------ |
| Connection   | Connection‑oriented (3‑way handshake)       | Connectionless (no setup)                        |
| Reliability  | Reliable – packets arrive in order, no loss | Unreliable – packets may be lost or out of order |
| Speed        | Slower (due to error checking)              | Faster                                           |
| Message size | No limit (byte stream)                      | Limited (datagram size)                          |
| Use when     | File transfer, web browsing, email          | Video streaming, VoIP, DNS, gaming               |

### TCP Communication Phases (simple)

1. **Socket creation** – Server creates a listening socket.
2. **Connection request** – Client requests connection; server accepts and creates a dedicated data socket for that client.
3. **Communication** – Data flows between client socket and server's data socket.
4. **Connection close** – Client closes; server deallocates the data socket.

### Example Application: File Transfer

- Client connects and sends a request (e.g., "send me mytext.txt").
- Server reads the file and sends it in **chunks** (e.g., 1024 bytes at a time).
- Client receives chunks and writes them to a new file (e.g., `received.txt`).

---

## 6. Distributed Task Management with Celery

**Definition:**  
Celery is a Python framework for running **tasks asynchronously** and distributing them across multiple **workers** (separate processes or machines).

**Typical uses:**

- Sending thousands of emails in the background
- Processing uploaded images (resizing, filtering)
- Running parallel computations (e.g., data analysis)
- Task queues in web applications

### How Celery Works (simple)

- Producer sends a task (e.g., "resize this image").
- Broker stores the task and gives it to an available worker.
- Worker executes the task.
- Result backend stores the result so you can check it later.

### Basic Celery Code Example

````python
# tasks.py
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')

@app.task
def add(x, y):
    return x + y

# Call asynchronously from another script
result = add.delay(4, 6)
print(result.get(timeout=10))   # 10


### 7. RMI (Remote Method Invocation) with Pyro4

**Definition:**
Pyro4 (Python Remote Objects) allows you to call **methods on remote objects** as if they were local – similar to Java RMI or .NET Remoting.

### Components

| Component | Role |
|-----------|------|
| Server | Hosts the object and its methods. |
| Client | Calls server methods remotely using a **Proxy** object. |
| Name Server | Keeps track of all Pyro objects – maps logical names (e.g., "server") to network URIs. |

### Simple Pyro4 Example

**Server side**

```python
import Pyro4

@Pyro4.expose
class Greeting:
    def welcome(self, name):
        return f"Hello {name}"

daemon = Pyro4.Daemon()                 # listens for requests
ns = Pyro4.locateNS()                   # find name server
uri = daemon.register(Greeting)         # register object
ns.register("server", uri)              # give it a logical name
print("Server ready.")
daemon.requestLoop()                    # wait for calls


# Section 8: Advantages of Distributed Computing

## Benefits at a Glance

Distributed computing offers several key advantages over traditional single‑machine systems. The table below summarizes the main benefits:

| Advantage | Explanation |
|-----------|-------------|
| **Scalability** | Add more machines easily (horizontal scaling). Increasing the number of computers in the system allows it to handle larger workloads without replacing existing hardware. |
| **Fault tolerance** | If one machine fails, others can take over (with proper design). Replication and redundancy mean that the system as a whole continues to operate even if individual components crash. |
| **Resource sharing** | Data, storage, and computing power can be shared across all machines in the network. This avoids isolated resources and improves overall utilization. |
| **Cost effectiveness** | Use many cheap, commodity machines instead of one expensive supercomputer. Distributed systems can achieve high performance at a fraction of the cost of a specialized parallel machine. |
| **Geographic distribution** | Place servers close to users around the world (low latency). By locating resources near where they are needed, response times are reduced and user experience improves. |

## Why These Advantages Matter

- **Scalability** means your system can grow with your business – from a few users to millions.
- **Fault tolerance** ensures high availability; a crashed server doesn't bring down the entire service.
- **Resource sharing** avoids waste – idle memory or CPU on one machine can be used by another.
- **Cost effectiveness** makes distributed computing accessible to startups and research groups with limited budgets.
- **Geographic distribution** is essential for global applications like streaming services, social media, and online gaming.

> **Note:** These benefits come with trade‑offs, including increased complexity, communication overhead, and security challenges


# Section 9: Challenges / Disadvantages of Distributed Computing

While distributed computing offers many benefits (Section 8), it also introduces significant challenges. Below are the main disadvantages you must handle when designing or using a distributed system.

| Challenge | Explanation |
|-----------|-------------|
| **Communication overhead** | Sending messages over a network is much slower than accessing shared memory. Every exchange of data between machines involves network latency, serialization, and protocol processing. This overhead can dominate execution time, especially for fine‑grained tasks. |
| **Deadlocks** | Two or more processes may wait forever for each other to release resources or send messages. Deadlocks are harder to detect and resolve in distributed systems because there is no global clock or shared memory to track dependencies easily. |
| **Partial failures** | One machine crashing should not break the whole system – but handling this gracefully is very hard. Unlike a single computer that either works or fails completely, a distributed system can be in a partially working state (some nodes down, others alive). Detecting failures and recovering without losing data requires complex protocols (e.g., timeouts, consensus algorithms). |
| **Security** | Data travels over networks that can be intercepted, modified, or spoofed. You must encrypt communication, authenticate nodes, and protect against denial‑of‑service attacks. Security is harder to enforce when control is spread across many machines, possibly in different administrative domains. |
| **Complexity** | More moving parts = harder to develop, debug, and maintain. You need to handle message ordering, duplication, loss, and clock synchronization. Tools, logging, and monitoring are more involved than for a single‑machine program. |

## Practical Implications

- **Communication overhead** → Keep messages large and infrequent; co‑locate related tasks.
- **Deadlocks** → Use timeouts, message ordering protocols, or deadlock‑free designs (e.g., request all resources at once).
- **Partial failures** → Design idempotent operations and use replication with consensus (e.g., Paxos, Raft).
- **Security** → Use TLS/SSL for transport, authentication tokens, and rate limiting.
- **Complexity** → Leverage established frameworks (e.g., Celery, Pyro4, Kafka) rather than building from scratch.

> **Remember:** The same feature that gives distributed systems scalability and fault tolerance (multiple independent nodes) is also the source of these challenges. There is no free lunch.


# Section 10: Comparison: Distributed vs. Parallel Computing

This section highlights the key differences between **parallel computing** (shared memory, single system) and **distributed computing** (multiple independent systems communicating over a network).

| Aspect | Parallel Computing | Distributed Computing |
|--------|--------------------|------------------------|
| **Memory** | Shared – all processors see the same memory address space. | Private – each machine has its own local memory. |
| **Communication** | Through shared variables (extremely fast, via bus or interconnect). | Through message passing (slower, depends on network latency). |
| **Scalability** | Limited by the physical bus, interconnect, or memory coherence protocol. | Almost unlimited – just add more machines. |
| **Typical hardware** | Single multi‑core computer, GPU, or shared‑memory multiprocessor. | Network of computers (clusters, cloud, or geographically distributed nodes). |
| **Programming model** | Threads, OpenMP, CUDA, OpenCL, parallel loops. | MPI, Sockets, Celery, Pyro4, REST APIs, message queues. |
| **Fault tolerance** | Generally low – if one processor fails, the whole program usually crashes. | Can be high – remaining nodes can continue if a node fails (requires replication and failover logic). |
| **Ease of programming** | Easier for regular, data‑parallel problems (e.g., matrix multiplication). | Harder – need to handle partial failures, network delays, and lack of global clock. |
| **Cost per performance** | High for large scale – expensive specialized hardware. | Low – commodity hardware can be used. |
| **Example systems** | Multi‑core CPU (Intel/AMD), NVIDIA GPU, Cray supercomputer. | Web servers, Hadoop/Spark cluster, cloud computing (AWS, Azure). |

## When to Use Each Model

- **Use parallel computing** when:
  - You have a single, powerful machine with many cores.
  - Your problem fits in shared memory (data is not too large).
  - Communication is frequent and fine‑grained.
  - You need the highest possible speed for a fixed hardware budget.

- **Use distributed computing** when:
  - Your data or computation is too large for one machine.
  - You want fault tolerance and high availability.
  - You expect to scale out over time (add more nodes).
  - Your application is naturally separated into independent services (microservices).
  - You are building a web service, cloud application, or large‑scale data processing pipeline.

## Complementary Relationship

Parallel and distributed computing are **not mutually exclusive**. Many modern systems use both:
- A distributed system of nodes, where each node itself is a parallel machine (multi‑core with shared memory).
- Example: A Hadoop cluster – each node runs tasks in parallel using multiple cores, and nodes communicate via network.

> **Takeaway:** Parallel computing gives you raw speed within one box; distributed computing gives you scale and resilience across many boxes. Choose based on your problem size, budget, and reliability needs.
````
