# Chapter 06: Parallel and Distributed Programming Examples

This folder contains example code for Chapter 6 of the Python Parallel Programming Cookbook. The examples are grouped into three categories:

- `Celery/` — a simple Celery task producer example.
- `Pyro4/` — two remote object examples using Pyro4.
- `socket/` — basic socket server/client examples.

---

## Celery

### Files
- `Celery/addTask.py`
- `Celery/addTask_main.py`

### What is happening
- `addTask.py` creates a Celery application named `addTask` and configures it to use an AMQP broker at `amqp://guest@localhost//`.
- It defines a single Celery task `add(x, y)` that returns `x + y`.
- `addTask_main.py` imports the Celery task module and calls `addTask.add.delay(5, 5)` to enqueue an asynchronous task.

### Expected behavior
- When run alone, `addTask_main.py` enqueues the task and creates an `AsyncResult` internally, but it does not print the result.
- If you run a Celery worker in the `Celery` folder with a command like:
  - `celery -A addTask worker --loglevel=info`
- Then run `python addTask_main.py`, the worker will execute the task and compute `10`.
- The worker log will show the task execution and a successful result of `10`.

### Notes
- This example requires a running RabbitMQ broker or compatible AMQP server on `localhost` with guest credentials.

---

## Pyro4

### First Example

Files:
- `Pyro4/First Example/pyro_server.py`
- `Pyro4/First Example/pyro_client.py`

What is happening:
- `pyro_server.py` defines a `Server` object with a remote method `welcomeMessage(name)`.
- It starts a Pyro daemon, locates the Pyro name server, registers the server object, and publishes it under the name `server`.
- `pyro_client.py` prompts the user for a name, obtains a proxy to `PYRONAME:server`, and calls `welcomeMessage(name)` remotely.

Expected runtime output:
- Server console: prints something like
  - `Ready. Object uri = PYRO:...`
- Client console: after typing a name like `Alice`, prints
  - `Hi welcome Alice`

How to run:
1. Start the Pyro name server separately (usually `pyro4-ns`).
2. Run `python pyro_server.py`.
3. Run `python pyro_client.py` and enter a name.

---

### Second Example

Files:
- `Pyro4/Second Example/chainTopology.py`
- `Pyro4/Second Example/server_chain_1.py`
- `Pyro4/Second Example/server_chain_2.py`
- `Pyro4/Second Example/server_chain_3.py`
- `Pyro4/Second Example/client_chain.py`

What is happening:
- `chainTopology.py` defines a remote `Chain` object that forwards a message to the next server.
- Each `Chain` object stores its own `name` and the next server name.
- When `process(message)` is called:
  - if its own name is already in the `message` list, it declares the chain closed and returns `['complete at ' + self.name]`.
  - otherwise it appends its name to the message, forwards the message to the next remote server, and then prepends a status string on return.

- `server_chain_1.py`, `server_chain_2.py`, and `server_chain_3.py` each start one Pyro server instance:
  - server 1 forwards to server 2
  - server 2 forwards to server 3
  - server 3 forwards back to server 1
- Each server is registered under a Pyro name:
  - `example.chainTopology.1`
  - `example.chainTopology.2`
  - `example.chainTopology.3`

- `client_chain.py` creates a proxy for `example.chainTopology.1` and calls `process(["hello"])`.

Expected runtime output:
- Server consoles show forwarding and the closure of the chain, for example:
  - `server_1 started`
  - `server_2 started`
  - `server_3 started`
  - `1 forwarding the message to the object 2`
  - `2 forwarding the message to the object 3`
  - `3 forwarding the message to the object 1`
  - `Back at 1; the chain is closed!`
- Client console prints a result list:
  - `Result=['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']`

How to run:
1. Start the Pyro name server (`pyro4-ns`).
2. Start each chain server in separate terminals:
   - `python server_chain_1.py`
   - `python server_chain_2.py`
   - `python server_chain_3.py`
3. Run `python client_chain.py`.

Notes:
- The chain is intentionally circular, so the message travels through 1 -> 2 -> 3 -> 1 before completing.

---

## socket

### Files
- `socket/server.py`
- `socket/client.py`
- `socket/server2.py`
- `socket/client2.py`
- `socket/mytext.txt`
- `socket/received.txt`

### Simple time server

What is happening:
- `server.py` starts a TCP server on port `9999` bound to the local host name.
- It accepts incoming connections, obtains the current time, sends it to the client, and closes the client socket.
- `client.py` connects to `localhost:9999`, receives up to 1024 bytes, decodes the response, and prints it.

Expected output:
- Server console: prints a connection message like
  - `Connected with[addr],[port]('HOSTNAME', 12345)`
- Client console: prints something like
  - `Time connection server:Thu Jun 05 14:23:12 2026`

How to run:
1. Run `python server.py`.
2. In another terminal, run `python client.py`.

### File-transfer server

What is happening:
- `server2.py` listens on port `60000` bound to the local host name.
- When a client connects, it receives a greeting from the client.
- It opens `mytext.txt` in binary mode, reads up to 1024 bytes, sends that chunk to the client, prints the bytes sent, then sends a final text message `->Thank you for connecting` and closes the connection.
- `client2.py` connects to `localhost:60000`, sends `HelloServer!`, then receives data in a loop and writes every chunk into `received.txt`.
- It prints `file opened`, `receiving data...`, and the decoded chunk contents while receiving.
- At the end it prints `Successfully get the file` and `connection closed`.

Expected output:
- Server console example:
  - `Server listening....`
  - `Got connection from ('HOSTNAME', 54321)`
  - `Server received 'HelloServer!'`
  - `Sent '...file contents...'`
  - `Donesending`
- Client console example:
  - `file opened`
  - `receiving data...`
  - `Data=> ...` (decoded chunk text)
  - `Successfully get the file`
  - `connection closed`
- The file `received.txt` will contain the bytes received from `mytext.txt` plus the text `->Thank you for connecting` if it is received before the socket closes.

Notes:
- `client2.py` and `server2.py` both use the local host name as the server address.
- `server2.py` closes the file inside the send loop, which is not ideal. For a small file, the transfer still works once.

---

## Summary

This workspace contains examples for:

- asynchronous task execution using Celery,
- remote object invocation with Pyro4,
- simple TCP socket communication,
- chained remote calls across multiple servers.

Each example is self-contained and demonstrates a different style of distributed or parallel programming in Python.
