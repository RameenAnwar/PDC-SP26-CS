Python Distributed Computing — Chapter 6
This repository covers distributed computing in Python using three different technologies — Sockets for low-level network communication, Pyro4 for remote object communication, and Celery for distributed task queuing. The programs are organized into three subfolders, each demonstrating a different approach to building networked and distributed applications.

Program Descriptions

Socket Programs

1. socket/server.py + socket/client.py — Time Server
Description:
This is a basic client-server program using Python sockets. The server listens for connections and sends the current time to any client that connects. The client connects, receives the time, and prints it.
How it works:
server.py creates a TCP socket, binds it to port 9999, and waits in a loop for incoming connections. When a client connects, it sends the current time as a string. client.py connects to the same host and port, receives the time string, and prints it.
Result:
# Server side
Connected with [addr],[port] ('192.168.x.x', 12345)

# Client side
Time connection server: Thu Jun 05 12:00:00 2026
Advantages:

Very simple introduction to socket programming.
Shows the complete request-response cycle between a client and server.

Disadvantages:

Server handles only one client at a time — not suitable for multiple simultaneous connections.
No error handling if the connection fails.

Where it can be used:

Time synchronization services, simple monitoring tools, or any application that needs basic client-server communication.


2. socket/server2.py + socket/client2.py — File Transfer over Socket
Description:
This program transfers a file (mytext.txt) from the server to the client over a socket connection. The client saves the received data into received.txt.
How it works:
server2.py listens on port 60000. When a client connects, it reads mytext.txt in chunks of 1024 bytes and sends them one by one. client2.py connects, receives the chunks, and writes them into received.txt until the transfer is complete.
Result:
# Server side
Server listening....
Got connection from ('192.168.x.x', 54321)
Server received 'HelloServer!'
Sent 'file content here...'

# Client side
file opened
receiving data...
Data=> file content here...
Successfully get the file
connection closed
Advantages:

Demonstrates real-world file transfer using raw sockets.
Shows how to send and receive binary data in chunks.

Disadvantages:

No encryption — data is sent in plain text.
Only transfers one file to one client at a time.

Where it can be used:

Simple file sharing systems, local network file transfer tools, or understanding how FTP-like protocols work at a low level.


3. socket/addTask.py + socket/addTask_main.py — Celery Task via Socket Folder
Description:
These two files define a simple Celery task inside the socket folder. addTask.py defines an add function as a Celery task. addTask_main.py calls it asynchronously using .delay().
How it works:
addTask.py creates a Celery app connected to a RabbitMQ broker and defines an add task. addTask_main.py imports it and calls add.delay(5, 5) which sends the task to the broker queue to be executed by a worker.
Advantages:

Shows how to define and call a Celery task.

Disadvantages:

Requires RabbitMQ to be running as a message broker — will not work without it.

Where it can be used:

Background job processing, sending emails, running scheduled tasks asynchronously.


Pyro4 Programs

4. Pyro4/First Example/pyro_server.py + pyro_client.py — Remote Object Communication
Description:
This example shows the simplest use of Pyro4 — a client calling a method on an object that lives on a remote server, as if it were a local object.
How it works:
pyro_server.py defines a Server class with a welcomeMessage method. It registers the object with Pyro4's name server under the name "server" and starts listening for remote calls. pyro_client.py connects to the name server, looks up "server", and calls welcomeMessage(name) as if it were a local method call.
Result:
# Server side
Ready. Object uri = PYRO:obj_...@localhost:...

# Client side
What is your name? Komal
Hi welcome Komal
Advantages:

Extremely clean — the client calls a remote method exactly like a local one.
Pyro4 handles all the network communication behind the scenes.

Disadvantages:

Requires Pyro4's name server (python -m Pyro4.naming) to be running before the server or client starts.
Not suitable for cross-internet communication without additional configuration.

Where it can be used:

Distributed applications where different components run on different machines, remote procedure calls, microservice-style architectures on a local network.


5. Pyro4/Second Example/ — Chain Topology (3-Server Ring)
Description:
This example demonstrates a chain (ring) topology using Pyro4. Three servers are connected in a ring — server 1 → server 2 → server 3 → server 1. A message is passed around the ring and each server forwards it to the next until it returns to the starting server.
Files:

chainTopology.py — defines the Chain class used by all three servers
server_chain_1.py — server 1, forwards to server 2
server_chain_2.py — server 2, forwards to server 3
server_chain_3.py — server 3, forwards back to server 1
client_chain.py — starts the chain by sending a message to server 1

How it works:
Each server registers itself with Pyro4's name server. When client_chain.py sends a message to server 1, it appends its name and forwards it to server 2. Server 2 does the same and forwards to server 3. Server 3 forwards back to server 1. When server 1 sees its own name in the message, it knows the chain is complete and stops.
Result:
1 forwarding the message to the object 2
2 forwarding the message to the object 3
3 forwarding the message to the object 1
Back at 1; the chain is closed!
Result=['complete at 1', 'passed on from 3', 'passed on from 2', 'passed on from 1']
Advantages:

Demonstrates distributed object communication in a ring pattern.
Each server is independent and communicates only with its neighbor.

Disadvantages:

Requires all three servers and the Pyro4 name server to be running simultaneously.
Complex setup for a small demonstration.

Where it can be used:

Token ring networks, distributed workflow pipelines, or any system where tasks are passed along a chain of processing nodes.


Celery Programs

6. Celery/addTask.py + Celery/addTask_main.py — Distributed Task with Celery
Description:
This is a simple Celery example where an addition task is defined and sent to a message broker (RabbitMQ) to be executed by a background worker process.
How it works:
addTask.py creates a Celery application connected to a RabbitMQ broker and defines an add task that returns the sum of two numbers. addTask_main.py calls addTask.add.delay(5, 5) which sends the task to the broker queue. A Celery worker running separately picks it up and executes it.
Result:
# Worker terminal
[Task] addTask.add[...] succeeded in 0.001s: 10
Advantages:

Tasks run in the background without blocking the main program.
Workers can run on different machines — true distributed execution.
Celery handles retries, scheduling, and monitoring automatically.

Disadvantages:

Requires RabbitMQ to be installed and running as the message broker.
Requires a separate Celery worker process to be started before tasks can execute.

Where it can be used:

Sending emails in the background, processing uploaded files, running scheduled jobs, handling high-volume task queues in web applications.


Applications
TechnologyReal-World UseSocket (basic)Time servers, monitoring tools, chat appsSocket (file transfer)Local file sharing, FTP-like toolsPyro4 (simple)Remote procedure calls, distributed componentsPyro4 (chain)Pipeline processing, token ring systemsCeleryBackground jobs, email queues, task scheduling

About
Each program in this repository demonstrates a different layer of distributed computing in Python — from raw socket communication at the network level, to remote object proxying with Pyro4, to fully distributed task queuing with Celery. Together they cover the main patterns used to build networked and distributed Python applications.