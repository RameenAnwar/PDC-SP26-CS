# Chapter 6 – Distributed Python
## Overview
This chapter introduces distributed computing in Python — a paradigm where applications and components reside on different nodes connected over a network. It covers the theoretical foundations of client-server architecture, practical socket programming, distributed task management, and remote method invocation using Pyro4.

---

## Topics Covered

### 1. Introducing Distributed Computing
**Concept:** Parallel vs. Distributed Processing

**Explanation:**
Explains the key differences between parallel and distributed computing. Parallel systems concentrate all processors in one machine (low latency, high speed), while distributed systems spread processing across many networked computers (more scalable, but higher communication overhead).

**Local vs. Distributed Architectures:**
- **Local:** All components reside on the same machine.
- **Distributed:** Components run on different nodes connected via a network.

**Pros:**
- Concurrent use of programs
- Centralized data management
- Distribution of processing load
- Near-infinite scalability

**Cons:**
- Greater complexity in design
- Communication overhead between components

---

### 2. Types of Distributed Applications
**Concept:** Client-Server & Multi-Level Architectures

**Explanation:**
Distributed applications are classified by their degree of distribution:

- **Client-Server Applications:** Two-level architecture where all processing is done on the server. The client initiates transactions; the server responds. Common examples include static and dynamic websites.

- **Multi-Level Applications:** Three or more tiers that separate concerns:
  - **Presentation Layer (PL):** User interface and data visualization.
  - **Business Logic Layer (BLL):** Core application rules and entity relationships.
  - **Data Access Layer (DAL):** Persistent data management (databases).

**Client-Server Communications:**
- Communication can occur over local networks, geographic networks, or OS-level services.
- Based on **TCP/IP**: point-to-point connections identified by IP address and port number.
- Standard protocols (HTTP, FTP, SMTP) are used by well-known applications; custom protocols can be defined for proprietary systems.

---

### 3. server.py & client.py
**Concept:** Using the Python `socket` Module

**Explanation:**
Demonstrates how to build a basic TCP/IP client-server application using Python's `socket` module. The server listens on a port and sends the current timestamp to any connecting client.

**Key Socket Methods:**
| Method | Description |
|--------|-------------|
| `socket()` | Creates a new socket (family, type, protocol) |
| `bind(address)` | Associates the socket with a host and port |
| `listen(n)` | Starts listening for up to `n` queued connections |
| `accept()` | Accepts an incoming connection, returns `(conn, address)` |
| `connect(address)` | Connects the client socket to a server |
| `send(data)` | Sends data through the socket |
| `close()` | Closes the socket connection |

**Use:**
Building low-level network applications, inter-process communication, and custom protocol implementations.

**Pros:**
- Full control over network communication
- Low-level and lightweight

**Cons:**
- Verbose and requires manual connection management
- No built-in abstractions for complex distributed patterns

**Types of Sockets:**
- **Stream Sockets:** Connection-oriented, based on TCP/SCTP — reliable and ordered.
- **Datagram Sockets:** Connectionless, based on UDP — fast but unreliable.
- **Raw Sockets:** Bypass the transport layer; headers are accessible at the application level.

---

### 4. addTask.py & addTask_main.py
**Concept:** Distributed Task Management with Celery

**Explanation:**
Demonstrates how to use **Celery**, a Python framework for distributed task queuing. Tasks are defined with the `@app.task` decorator and dispatched to worker nodes via a **message broker** (RabbitMQ or Redis). The example implements a distributed addition task.

**Setup:**
```bash
pip install celery
# Install RabbitMQ from http://www.rabbitmq.com/download.html
celery --version
```

**Key Methods:**
- `delay(*args, **kwargs)` — Shortcut to send a task message asynchronously.
- `apply_async(args, kwargs)` — Full-featured task dispatch with execution options.

**Architecture:**
Uses the **publish/subscribe paradigm** via a message broker:
- Producer publishes a task message to the broker.
- The broker distributes the task to available workers.
- Workers execute the task and return results.

**Use:**
Background job processing, asynchronous workflows, distributed computation across many nodes.

**Pros:**
- Scalable and fault-tolerant
- Supports multiple brokers (RabbitMQ, Redis, MongoDB, Amazon SQS, etc.)
- Simple task definition with decorators

**Cons:**
- Requires a separate message broker process
- Additional Windows setup needed (`FORKED_BY_MULTIPROCESSING` environment variable)

---

### 5. pyro_server.py & pyro_client.py
**Concept:** Remote Method Invocation (RMI) with Pyro4

**Explanation:**
Shows how to use **Pyro4** (Python Remote Objects) to call methods on remote objects as if they were local — analogous to Java RMI. The server exposes a `welcomeMessage()` method using the `@Pyro4.expose` decorator, and the client invokes it through a `Pyro4.Proxy` object.

**Setup:**
```bash
pip install Pyro4
python -m Pyro4.naming   # Start the Pyro4 nameserver
```

**Key Components:**
- `Pyro4.Daemon` — Dispatches incoming client calls to registered objects.
- `Pyro4.locateNS()` — Locates the running nameserver.
- `daemon.register(obj)` — Registers a server object with the daemon.
- `ns.register(name, uri)` — Registers the object under a name in the nameserver.
- `Pyro4.Proxy(name)` — Client-side proxy that forwards calls to the remote object.

**Use:**
Distributed object-oriented systems where remote services need to be invoked transparently.

**Pros:**
- Transparent remote method calls
- Supports complex object topologies (e.g., chain, broadcast)
- Easy to integrate with existing Python code

**Cons:**
- Requires a running Pyro4 nameserver
- Adds network latency compared to local calls

---

### 6. chainTopology.py, server_chain_1/2/3.py & client_chain.py
**Concept:** Chain Topology with Pyro4

**Explanation:**
Demonstrates a **chain topology** pattern where a client calls Server 1, which forwards the request to Server 2, then to Server 3, and the chain closes when Server 3 calls back to Server 1. Each server uses the `Chain` class to process and forward messages.

**Execution Order:**
```bash
python -m Pyro4.naming         # Start nameserver
python server_chain_1.py       # Terminal 1
python server_chain_2.py       # Terminal 2
python server_chain_3.py       # Terminal 3
python client_chain.py         # Terminal 4
```

**Expected Output:**
```
Result=['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']
```

**Use:**
Modeling pipeline workflows, distributed event chains, or any architecture where requests must pass through a fixed sequence of services.

---

## Summary
This chapter builds practical skills in distributed Python programming — from low-level TCP socket communication to high-level abstractions with Celery and Pyro4. It covers the fundamental theory of distributed architectures, hands-on client-server implementations, and advanced patterns like chain topology, providing a solid foundation for building real-world distributed systems.