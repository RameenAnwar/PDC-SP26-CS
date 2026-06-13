# Chapter 06 – Distributed Systems and Network Communication

## Overview

This chapter explores distributed computing and network communication using three different technologies:

* **Celery** – Distributed Task Queues
* **Pyro4** – Remote Method Invocation (RMI)
* **Sockets** – Low-Level TCP/IP Networking

The implementations use **Greatest Common Divisor (GCD)** and **Least Common Multiple (LCM)** computations to demonstrate remote execution, task distribution, client-server communication, and distributed system architectures.

The objective is to understand how applications communicate across processes, machines, and networks while maintaining efficiency and scalability.

---

## Concepts Implemented

### 1. Celery – Distributed Task Queue

Celery is used to distribute computational tasks across background worker processes.

#### Features

* Asynchronous task execution
* Background processing
* Message broker integration
* Distributed workload management

#### Workflow

```text
Client
   ↓
Message Broker (RabbitMQ / Redis)
   ↓
Celery Worker
   ↓
GCD / LCM Computation
   ↓
Result Returned
```

#### Mathematical Tasks

* GCD Calculation
* LCM Calculation

#### Benefits

* Non-blocking execution
* Horizontal scaling through multiple workers
* Fault-tolerant task processing

---

### 2. Pyro4 – Remote Method Invocation (RMI)

Pyro4 enables Python objects located on remote machines to be accessed as if they were local objects.

#### Features

* Remote object communication
* Transparent method invocation
* Name Server support
* Distributed object architecture

#### Name Server

Acts as a directory service for locating remote objects.

```text
Client
   ↓
Pyro Name Server
   ↓
Remote Object
```

#### Daisy Chain Topology

This implementation demonstrates a chain-based communication model:

```text
Server 1 → Server 2 → Server 3 → Server 1
```

A message and mathematical parameters are passed through multiple servers before returning to the origin.

#### Benefits

* Simplified distributed programming
* Object-oriented communication
* Easy remote procedure execution

---

### 3. Sockets – TCP/IP Communication

Sockets provide the foundation for network programming and low-level communication.

#### Features

* Client-Server architecture
* TCP/IP communication
* Data streaming
* File transfer support

---

### Math Server

A TCP server receives numerical values and computes mathematical results.

#### Example Request

```text
48,18
```

#### Example Response

```text
GCD = 6
LCM = 144
```

---

### File Transfer

Demonstrates transmission of binary and text files over a network connection.

Example:

```text
mytext.txt
```

The file is read by the sender and transferred through a TCP socket to the receiving system.

---

## Technology Comparison

| Technology | Level      | Primary Use Case                 | Scaling Method            |
| ---------- | ---------- | -------------------------------- | ------------------------- |
| Celery     | High-Level | Background Task Processing       | Horizontal Worker Scaling |
| Pyro4      | High-Level | Distributed Object Systems       | Remote Object Proxy       |
| Sockets    | Low-Level  | Custom Protocols & File Transfer | Byte Stream Communication |

---

## Project Structure

| Component             | Description               |
| --------------------- | ------------------------- |
| celery_tasks.py       | Celery Task Definitions   |
| celery_worker.py      | Celery Worker Process     |
| celery_client.py      | Celery Task Submission    |
| pyro_server.py        | Pyro Remote Object Server |
| pyro_client.py        | Pyro Client Application   |
| pyro_chain.py         | Daisy Chain Communication |
| socket_math_server.py | TCP Math Server           |
| socket_math_client.py | TCP Math Client           |
| socket_file_server.py | File Transfer Server      |
| socket_file_client.py | File Transfer Client      |

---

## Requirements

### Python Version

* Python 3.10+
* Tested on Python 3.14

---

## Installation

### Celery

Install Celery:

```bash
pip install celery
```

Install and configure one of the following brokers:

#### Redis

```bash
redis-server
```

#### RabbitMQ

```bash
rabbitmq-server
```

---

### Pyro4

Install Pyro4:

```bash
pip install Pyro4
```

Start the Name Server:

```bash
python -m Pyro4.naming
```

---

### Sockets

No external installation required.

Uses Python's built-in:

```python
import socket
```

---

## Running the Programs

### Celery

Start Worker:

```bash
celery -A celery_tasks worker --loglevel=info
```

Run Client:

```bash
python celery_client.py
```

---

### Pyro4

Start Name Server:

```bash
python -m Pyro4.naming
```

Start Server:

```bash
python pyro_server.py
```

Run Client:

```bash
python pyro_client.py
```

---

### Socket Communication

Start Server:

```bash
python socket_math_server.py
```

Run Client:

```bash
python socket_math_client.py
```

---

## Example Output

### Celery

```text
Task Submitted...
Worker Processing...

GCD = 6
LCM = 144

Task Completed Successfully
```

### Pyro4

```text
Connected to Remote Object

Remote GCD = 6
Remote LCM = 144
```

### Socket Server

```text
Client Connected

Received: 48,18

GCD = 6
LCM = 144
```

---

## Learning Objectives

After completing this chapter, you will be able to:

* Understand distributed system fundamentals.
* Implement asynchronous task queues using Celery.
* Configure message brokers such as Redis and RabbitMQ.
* Create remote objects using Pyro4.
* Use Name Servers for service discovery.
* Develop TCP/IP client-server applications.
* Implement file transfer using sockets.
* Compare high-level and low-level communication technologies.
* Design scalable distributed computing solutions.

---

## Performance Analysis

This chapter enables comparison between:

* Local vs Remote Execution
* Synchronous vs Asynchronous Processing
* Celery vs Pyro4 Communication Models
* High-Level Frameworks vs Low-Level Networking
* Distributed Tasks vs Direct Socket Communication

These comparisons provide insights into selecting the appropriate technology for real-world distributed applications.

---

## Future Enhancements

* Multi-Node Distributed GCD/LCM Processing
* Celery Task Monitoring Dashboard
* Secure Socket Communication (SSL/TLS)
* Load Balancing Across Multiple Servers
* Distributed File Synchronization
* Cloud-Based Worker Deployment
* Hybrid Celery + Pyro4 Architectures
* Fault-Tolerant Distributed Systems

---

## Author

Huzaifa Alim

Computer Science Student
Usman Institute of Technology (UIT)
