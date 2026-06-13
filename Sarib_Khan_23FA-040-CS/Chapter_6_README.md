# Chapter 6 – Distributed Computing using Sockets, Celery, and Pyro4

In this chapter, I learned different distributed computing techniques using sockets, Celery, and Pyro4. I also learned client-server communication, remote method calling, and task distribution.

---

## Topic: Celery/addTask.py and addTask_main.py

What I Learned
I learned how Celery distributes tasks between workers asynchronously.

How to Execute
python addTask_main.py

Use / Output
Performs addition task using Celery workers.

When to Use
When background task execution is needed.

Advantages
Asynchronous execution
Useful for distributed systems

Disadvantages
Requires setup and configuration

Summary
Celery helps execute tasks in distributed environments.

---

## Topic: Pyro4/First Example/pyro_server.py and pyro_client.py

What I Learned
I learned how remote objects work using Pyro4.

How to Execute
First run:
python pyro_server.py

Then run:
python pyro_client.py

Use / Output
Client communicates with server remotely.

When to Use
When remote procedure calls are needed.

Advantages
Easy remote communication

Disadvantages
Requires network setup

Summary
Pyro4 allows remote method execution between systems.

---

## Topic: Pyro4/Second Example/chainTopology.py

What I Learned
I learned about chain topology in distributed systems.

How to Execute
Used with server files.

Use / Output
Defines communication structure between servers.

When to Use
When processes are connected in chain form.

Advantages
Organized communication

Disadvantages
Failure in one node can affect others

Summary
Chain topology connects servers sequentially.

---

## Topic: Pyro4/Second Example/server_chain_1.py, server_chain_2.py, server_chain_3.py

What I Learned
I learned how multiple servers communicate in a chain structure.

How to Execute
Run each server separately.

Use / Output
Transfers requests between servers.

When to Use
When distributed communication is required.

Advantages
Demonstrates distributed coordination

Disadvantages
Complex setup

Summary
Multiple servers can communicate in sequence.

---

## Topic: Pyro4/Second Example/client_chain.py

What I Learned
I learned how a client communicates with chained servers.

How to Execute
python client_chain.py

Use / Output
Sends requests through server chain.

When to Use
When interacting with distributed server systems.

Advantages
Shows practical distributed communication

Disadvantages
Depends on all servers running properly

Summary
Clients can interact with multiple connected servers.

---

## Topic: socket/server.py and client.py

What I Learned
I learned basic socket communication between client and server.

How to Execute
First run:
python server.py

Then run:
python client.py

Use / Output
Sends and receives messages.

When to Use
When building network communication systems.

Advantages
Direct communication
Simple networking concept

Disadvantages
Needs proper connection management

Summary
Sockets provide communication between systems.

---

## Topic: socket/server2.py and client2.py

What I Learned
I learned advanced socket communication and file transfer.

How to Execute
Run server2.py first, then client2.py.

Use / Output
Transfers data/files between systems.

When to Use
When sending files or larger data.

Advantages
Useful for network applications

Disadvantages
Can become complex

Summary
Sockets can also transfer files and large data.

---

## Topic: socket/addTask.py and addTask_main.py

What I Learned
I learned how distributed tasks can be executed using socket programming.

How to Execute
python addTask_main.py

Use / Output
Performs addition task through communication.

When to Use
When distributed task execution is needed.

Advantages
Simple distributed example

Disadvantages
Limited scalability

Summary
Sockets can distribute tasks between systems.

---

## Final Understanding

In this chapter, I learned distributed computing concepts using sockets, Celery, and Pyro4. I understood client-server communication, remote method execution, task distribution, and distributed system topologies.