# Chapter 6 – Distributed Python

## Topic: Celery/addTask.py

### What I Learned
I learned how to create a simple Celery task. Celery is used to run tasks asynchronously using a message broker such as RabbitMQ.

### How to Execute
First, RabbitMQ must be running on the system.

Then start the Celery worker from the folder where `addTask.py` exists:

```bash
celery -A addTask worker --loglevel=info
```

After that, run the main file:

```bash
python addTask_main.py
```

### Use / Output
This program defines an `add()` task that takes two numbers and returns their sum. The task is sent to the Celery worker using `.delay()`.

Example:

```python
result = addTask.add.delay(5, 5)
```

Expected result:

```text
10
```

### When to Use
Use Celery when tasks need to run in the background or outside the main program.

### Advantages
- Runs tasks asynchronously
- Useful for background jobs
- Can distribute work across workers
- Good for long-running tasks

### Disadvantages
- Requires a message broker like RabbitMQ or Redis
- More setup is needed
- Harder to debug than normal function calls

### Summary
Celery allows Python functions to run as background tasks using workers and a message broker.

---

## Topic: Celery/addTask_main.py

### What I Learned
I learned how to call a Celery task asynchronously using the `.delay()` method.

### How to Execute
Make sure the Celery worker is already running:

```bash
celery -A addTask worker --loglevel=info
```

Then run:

```bash
python addTask_main.py
```

### Use / Output
This file imports the `addTask` module and sends the task `add(5, 5)` to the Celery worker.

Example output in worker terminal:

```text
Task addTask.add received
Task addTask.add succeeded
```

### When to Use
Use a main file like this when you want to trigger Celery tasks from another program.

### Advantages
- Keeps task definition and task execution separate
- Simple way to send work to a worker
- Makes the main program faster for background work

### Disadvantages
- Does not directly print the result
- Requires Celery worker to be active
- Requires RabbitMQ or another broker

### Summary
This file sends a Celery task to the worker. It shows how asynchronous task execution works in Celery.

---

## Topic: Pyro4/First Example/pyro_server.py

### What I Learned
I learned how to create a remote object server using Pyro4. The server exposes a method that can be called from another Python program.

### How to Execute
First, start the Pyro4 name server:

```bash
python -m Pyro4.naming
```

Then run the server:

```bash
python pyro_server.py
```

### Use / Output
The server creates a `Server` class with a `welcomeMessage()` method. This method receives a name and returns a welcome message.

Example server output:

```text
Ready. Object uri = PYRO:obj_...
```

### When to Use
Use Pyro4 when Python programs need to call objects or methods from another process or machine.

### Advantages
- Allows remote method calls
- Makes distributed object communication easier
- Useful for client-server Python applications

### Disadvantages
- Requires Pyro4 name server
- More setup than normal Python functions
- Network issues can affect communication

### Summary
This program creates a Pyro4 server and registers it with the name server so clients can call its methods remotely.

---

## Topic: Pyro4/First Example/pyro_client.py

### What I Learned
I learned how a Pyro4 client connects to a remote server object and calls a method on it.

### How to Execute
Make sure the Pyro4 name server and `pyro_server.py` are running first.

Then run:

```bash
python pyro_client.py
```

### Use / Output
The client asks the user for their name, connects to the remote server object using `PYRONAME:server`, and calls the `welcomeMessage()` method.

Example output:

```text
What is your name? Ali
Hi welcome Ali
```

### When to Use
Use a Pyro4 client when you need to access functionality from a remote Python server.

### Advantages
- Simple remote method calling
- Client can use server-side functions
- Useful for distributed systems

### Disadvantages
- Server must be running
- Name server must be running
- Network or registration errors can occur

### Summary
The Pyro4 client connects to the server and calls a remote method as if it were a local method.

---

## Topic: Pyro4/Second Example/chainTopology.py

### What I Learned
I learned how Pyro4 can be used to create a chain topology where objects pass messages to each other.

### How to Execute
This file defines the chain object, but extra setup files are usually needed to start multiple chain servers and register them with the Pyro4 name server.

Typical first step:

```bash
python -m Pyro4.naming
```

Then each chain object/server must be started and registered.

### Use / Output
Each chain object forwards a message to the next object in the chain. When the message returns to the starting object, the chain is completed.

Example output:

```text
Server1 forwarding the message to the object Server2
Server2 forwarding the message to the object Server3
Back at Server1; the chain is closed!
```

### When to Use
Use a chain topology when distributed objects need to pass messages in a fixed sequence.

### Advantages
- Demonstrates distributed object communication
- Useful for understanding network topology
- Shows how remote objects can call each other

### Disadvantages
- Requires multiple registered Pyro4 objects
- More complex setup
- If one object fails, the chain can break

### Summary
This program defines a Pyro4 chain object that forwards messages through a chain of remote objects until the message returns to the original object.

---

## Topic: socket/addTask.py

### What I Learned
I learned that Celery tasks can also be defined inside another project folder. This file creates a Celery app and defines an `add()` task.

### How to Execute
First, make sure RabbitMQ is running.

Start the Celery worker:

```bash
celery -A addTask worker --loglevel=info
```

Then run:

```bash
python addTask_main.py
```

### Use / Output
The `add()` task receives two numbers and returns their sum.

Example:

```python
add.delay(5, 5)
```

Expected result:

```text
10
```

### When to Use
Use this when background task execution is needed in a socket or distributed programming project.

### Advantages
- Allows background task processing
- Separates task execution from the main program
- Can scale with multiple workers

### Disadvantages
- Requires RabbitMQ
- Requires Celery worker
- No result is printed unless result handling is added

### Summary
This file defines a Celery task that can be executed asynchronously by a Celery worker.

---

## Topic: socket/addTask_main.py

### What I Learned
I learned how to import a Celery task directly and run it asynchronously using `.delay()`.

### How to Execute
Start Celery worker first:

```bash
celery -A addTask worker --loglevel=info
```

Then run:

```bash
python addTask_main.py
```

### Use / Output
This program sends the task `add(5, 5)` to the Celery worker.

Example output in worker terminal:

```text
Task addTask.add received
Task addTask.add succeeded
```

### When to Use
Use this file when you want to trigger a Celery task from a separate Python script.

### Advantages
- Simple task triggering
- Keeps main file small
- Useful for testing Celery tasks

### Disadvantages
- Does not display the returned result
- Worker must already be running
- Broker connection is required

### Summary
This script triggers the Celery `add()` task asynchronously.

---

## Topic: socket/client.py

### What I Learned
I learned how to create a basic socket client that connects to a server and receives data.

### How to Execute
First, run the socket server.

Then run:

```bash
python client.py
```

### Use / Output
The client creates a TCP socket, connects to a host and port, receives data from the server, closes the connection, and prints the received message.

Example output:

```text
Time connection server: Sat Jun 06 10:30:00 2026
```

### When to Use
Use a socket client when a program needs to connect to a server and receive data over a network.

### Advantages
- Basic network communication
- Useful for client-server applications
- Works over TCP/IP

### Disadvantages
- Server must be running before client
- Port number must match the server
- Low-level socket programming can be error-prone

### Summary
This file creates a TCP client that connects to a server, receives data, and prints it.

---

## Topic: socket/server2.py

### What I Learned
I learned how to create a socket server that listens for client connections and sends file data to the client.

### How to Execute
First, make sure a file named `mytext.txt` exists in the same folder.

Then run:

```bash
python server2.py
```

After that, run the client in another terminal.

### Use / Output
The server listens for incoming connections. When a client connects, it receives data from the client, reads `mytext.txt`, and sends the file content to the client.

Example output:

```text
Server listening....
Got connection from ('127.0.0.1', 50000)
Server received 'Hello'
Sent 'file content'
Done sending
```

### When to Use
Use a socket server when you want to send data or files from one machine/program to another over a network.

### Advantages
- Allows network communication
- Can send files to clients
- Useful for understanding TCP servers

### Disadvantages
- Client and server ports must match
- Current code has indentation issues
- File closing happens inside the loop
- No error handling is added

### Summary
This file creates a simple TCP server that accepts client connections and sends file data.

---

# Chapter 6 Summary

In this chapter, I learned about distributed Python programming using Celery, Pyro4, and sockets. These tools allow Python programs to communicate across processes, machines, or background workers.

Celery is used for asynchronous task queues. Pyro4 is used for remote object communication. Sockets are used for low-level network communication between clients and servers.

## Main Concepts Covered

- Celery task creation
- Celery workers
- Message brokers
- Asynchronous task execution
- Pyro4 remote objects
- Pyro4 name server
- Remote method calls
- Chain topology
- Socket client
- Socket server
- TCP communication
- File transfer through sockets

## Overall Advantages

- Enables distributed programming
- Supports background task execution
- Allows communication between different programs
- Useful for client-server systems
- Can improve scalability

## Overall Disadvantages

- Requires extra setup
- Celery needs a broker such as RabbitMQ or Redis
- Pyro4 needs a name server
- Socket programming needs careful port and connection handling
- Debugging distributed systems is harder

## Final Summary

Chapter 6 explains how Python can be used for distributed programming. Celery helps run background tasks, Pyro4 allows remote method calls, and sockets provide direct network communication. These tools are powerful, but they require proper setup and careful handling of servers, clients, workers, ports, and connections.

---

# Important Code Notes

## Celery Note
Celery examples will not work unless RabbitMQ or another broker is running.

## Pyro4 Note
Pyro4 examples require the Pyro4 name server to run first:

```bash
python -m Pyro4.naming
```

## Socket Note
The provided `client.py` connects to port `9999`, but `server2.py` listens on port `60000`. Both files must use the same port to communicate.

Correct either the client:

```python
port = 60000
```

or the server:

```python
port = 9999
```

## server2.py Note
In `server2.py`, the `f.close()`, thank-you message, and `conn.close()` lines should be outside the file-reading loop. Otherwise, the server may close the file and connection too early.
