# Chapter 06 - Celery, Pyro4, and Socket Communication

## What I learned overall

- Distributed and networked programs need a different mindset than local threading or multiprocessing because communication happens across boundaries.
- Task queues, remote objects, and sockets all solve the same broad problem in different ways: getting work or data from one place to another.
- Reliable communication depends on clear message flow, explicit endpoints, and careful shutdown behavior.
- These examples showed me how Python can support both high-level distributed systems and low-level network programming.

## Concepts from each folder/example

### `Celery/addTask.py` and `Celery/addTask_main.py`
These files show a simple task queue example:

- `addTask.py` creates a `Celery` app with a RabbitMQ broker.
- `addTask.add()` is registered as a task with `@app.task`.
- `addTask_main.py` submits the task asynchronously with `.delay(5, 5)`.

My takeaway: Celery is useful when work should run outside the main process and be handled by a worker system.

### `Pyro4/First Example/pyro_server.py` and `pyro_client.py`
This pair demonstrates remote method invocation:

- The server defines a `welcomeMessage()` method and exposes it with `@Pyro4.expose`.
- A Pyro daemon registers the object with the name server.
- The client connects through `PYRONAME:server` and calls the method remotely.

My conclusion: Pyro4 makes remote object calls feel similar to local method calls, which simplifies distributed application design.

### `Pyro4/Second Example/chainTopology.py`, `server_chain_*.py`, and `client_chain.py`
This example builds a chain of remote objects:

- `Chain.process()` forwards a message to the next server in the chain.
- Each server registers itself with the Pyro name server.
- The client starts the process by contacting the first server in the chain.

My takeaway: this is a good example of distributed coordination, where each node contributes to a larger workflow.

### `socket/server.py` and `socket/client.py`
This is the basic socket time-service example:

- The server creates a TCP socket, binds to a host and port, and listens for connections.
- Each client connection receives the current time.
- The client connects, receives the response, and prints it.

My observation: this example is a simple introduction to client-server networking with raw sockets.

### `socket/server2.py` and `client2.py`
This example shows file transfer over sockets:

- The server accepts a connection, reads a request, and sends the contents of `mytext.txt`.
- The client sends a greeting and writes the received bytes into `received.txt`.
- The loop continues until the server finishes sending data.

My takeaway: sockets can move arbitrary data, but the protocol needs to define when transmission starts and ends.

### `socket/addTask.py` and `socket/addTask_main.py`
This is another Celery-style task example included in the socket folder:

- Defines the same simple `add(x, y)` task pattern.
- Dispatches the task with `.delay(5, 5)`.

My conclusion: even small task-queue examples reinforce the idea of decoupling task submission from task execution.

## Personal chapter conclusions

- Remote communication is all about contracts: what is sent, where it goes, and when the exchange is complete.
- Higher-level tools like Celery and Pyro4 hide a lot of networking complexity, while sockets expose the mechanics directly.
- The examples helped me understand the spectrum from convenient abstractions to low-level control.
- Distributed systems need careful design just like threaded programs, but the failure modes now include network and service availability too.

