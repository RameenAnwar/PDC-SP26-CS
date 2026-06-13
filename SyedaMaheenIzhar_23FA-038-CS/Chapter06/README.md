# Chapter 06: Distributed Computing using Celery, Pyro4, and Socket Programming

---

# CELERY EXAMPLES

## 1. addTask.py

### What I Learned
This file creates a Celery application and defines a distributed task named `add()`. The task is executed asynchronously using a message broker.

### How to Execute
Start RabbitMQ service first:

celery -A addTask worker --loglevel=info

### End Use
Used for background task execution and distributed processing.

### When and How to Use
Used when long-running tasks need to run separately from the main application flow.

### Summary
Basic Celery task implementation.

### Advantages
- Asynchronous execution
- Scalable system design
- Improved application performance

### Disadvantages
- Requires RabbitMQ or Redis
- Needs additional setup and configuration

---

## 2. addTask_main.py

### What I Learned
This file sends a task request to Celery workers using the delay() method.

### How to Execute
python addTask_main.py

### End Use
Used to send tasks to Celery workers for execution.

### When and How to Use
Used when background task execution is required without blocking the main program.

### Summary
Celery task producer.

### Advantages
- Simple task submission
- Non-blocking execution

### Disadvantages
- Requires active worker process

---

# PYRO4 EXAMPLES

## 3. pyro_server.py

### What I Learned
This program creates a Pyro4 server and registers a remote object with the Pyro Name Server. It exposes a method called welcomeMessage().

### How to Execute
Start Pyro Name Server:
pyro4-ns

Then run server:
python pyro_server.py

### End Use
Provides remote services using RPC.

### When and How to Use
Used when methods need to be accessed from another machine or process.

### Summary
Basic Pyro4 server implementation.

### Advantages
- Simple RPC implementation
- Object-oriented remote communication

### Disadvantages
- Requires Pyro Name Server

---

## 4. pyro_client.py

### What I Learned
This client connects to the Pyro server and calls the remote method welcomeMessage().

### How to Execute
python pyro_client.py

### End Use
Used to access remote server functionality.

### When and How to Use
Used in distributed systems requiring remote method calls.

### Summary
Basic Pyro4 client implementation.

### Advantages
- Easy remote communication
- Minimal code complexity

### Disadvantages
- Depends on server availability

---

# PYRO4 CHAIN TOPOLOGY EXAMPLE

## 5. chainTopology.py

### What I Learned
This file implements chain topology logic where each server forwards the message to the next node until completion.

### End Use
Used to demonstrate distributed message passing.

### When and How to Use
Used when requests must pass through multiple nodes.

### Summary
Chain routing logic implementation.

### Advantages
- Demonstrates distributed communication
- Shows message flow across nodes

### Disadvantages
- Failure of one node breaks the chain

---

## 6. server_chain_1.py

### What I Learned
This is the first node in the chain and forwards requests to Server 2.

### How to Execute
python server_chain_1.py

### Summary
First chain node.

---

## 7. server_chain_2.py

### What I Learned
Second node in the chain forwarding to Server 3.

### How to Execute
python server_chain_2.py

### Summary
Second chain node.

---

## 8. server_chain_3.py

### What I Learned
Final node in chain returning message to Server 1.

### How to Execute
python server_chain_3.py

### Summary
Final chain node.

---

## 9. client_chain.py

### What I Learned
Starts the chain process and receives final response.

### How to Execute
python client_chain.py

### Summary
Chain client.

---

# SOCKET PROGRAMMING EXAMPLES

## 10. server.py

### What I Learned
Sends current date and time to client.

### How to Execute
python server.py

### Summary
Time server.

---

## 11. client.py

### What I Learned
Receives system time from server.

### How to Execute
python client.py

### Summary
Time client.

---

## 12. server2.py

### What I Learned
Sends contents of mytext.txt to client.

### How to Execute
python server2.py

### Summary
File transfer server.

---

## 13. client2.py

### What I Learned
Receives file and saves as received.txt.

### How to Execute
python client2.py

### Summary
File transfer client.

---

## 14. mytext.txt
Input file used for file transfer.

---

## 15. received.txt
Output file after receiving data.
