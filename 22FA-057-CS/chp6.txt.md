# 📂 Chapter 6: Distributed Systems & Networking in Python

This chapter covers **distributed task processing, remote method invocation, and socket programming** using Celery, Pyro4, and Python sockets.

---

## 🔹 1. Celery Task Queue (Basic Task)
📄 File: `Chapter-6/celery_add_task.py`

**Concepts Covered:**
- Celery task queue
- Distributed task execution
- Message broker (RabbitMQ)

---

## 🔹 2. Running Celery Task
📄 File: `Chapter-6/celery_run_task.py`

**Concepts Covered:**
- Async task execution
- Task delay method
- Background processing

---

## 🔹 3. Pyro4 Client
📄 File: `Chapter-6/pyro_client.py`

**Concepts Covered:**
- Remote object invocation
- Client-server communication
- Name server lookup

---

## 🔹 4. Pyro4 Server
📄 File: `Chapter-6/pyro_server.py`

**Concepts Covered:**
- Remote object exposure
- Daemon server
- Distributed services

---

## 🔹 5. Chain Topology (Pyro4)
📄 File: `Chapter-6/chain_topology.py`

**Concepts Covered:**
- Distributed chain communication
- Message forwarding
- Recursive remote calls

---

## 🔹 6. Chain Client Execution
📄 File: `Chapter-6/chain_client.py`

**Concepts Covered:**
- Triggering distributed chain
- Receiving processed results

---

## 🔹 7. Distributed Chain Servers
📄 Files:
- `Chapter-6/server1.py`
- `Chapter-6/server2.py`
- `Chapter-6/server3.py`

**Concepts Covered:**
- Multi-node communication
- Distributed topology
- Server coordination

---

## 🔹 8. Celery Task (Alternate Example)
📄 File: `Chapter-6/celery_task_alt.py`

**Concepts Covered:**
- Task reuse
- Distributed execution model

---

## 🔹 9. Celery Task Caller
📄 File: `Chapter-6/celery_caller.py`

**Concepts Covered:**
- Triggering Celery tasks
- Async execution

---

## 🔹 10. Socket Programming (Basic Client)
📄 File: `Chapter-6/socket_client_time.py`

**Concepts Covered:**
- TCP socket communication
- Client-server model
- Receiving data

---

## 🔹 11. Socket File Transfer Client
📄 File: `Chapter-6/socket_client_file.py`

**Concepts Covered:**
- File transfer over network
- Receiving binary data

---

## 🔹 12. Socket Server (Time Server)
📄 File: `Chapter-6/socket_server_time.py`

**Concepts Covered:**
- Server socket creation
- Handling multiple connections
- Sending time data

---

## 🔹 13. Socket Server (File Server)
📄 File: `Chapter-6/socket_server_file.py`

**Concepts Covered:**
- File sending server
- Data streaming
- Client handling
