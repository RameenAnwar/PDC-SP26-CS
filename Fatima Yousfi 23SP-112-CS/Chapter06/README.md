# Chapter 06

This chapter contains examples from three distributed-programming areas: sockets, Celery, and Pyro4.

## Socket examples

### `socket/server.py` and `socket/client.py`

- `server.py` opens a TCP socket on port `9999`, waits for incoming connections, sends the current time, and closes the client socket.
- `client.py` connects to that server, receives the time string, and prints it.

### `socket/server2.py` and `socket/client2.py`

- `server2.py` waits on port `60000`, reads `mytext.txt`, and sends the file contents to the connected client.
- `client2.py` receives the data and stores it in `received.txt`.
- `socket/mytext.txt` is the source file used for transfer.

### `socket/addTask.py` and `socket/addTask_main.py`

- These files define and trigger a Celery task even though they are located inside the socket folder.
- They require a running message broker because `add.delay()` sends work asynchronously.

## Celery folder

### `Celery/addTask.py`

- Defines a Celery application and exposes an `add(x, y)` task.

### `Celery/addTask_main.py`

- Imports the task module and submits `add.delay(5, 5)`.
- A broker and a Celery worker are required for this example to run successfully.

## Pyro4 first example

### `Pyro4/First Example/pyro_server.py`

- Creates a simple Pyro4 server with an exposed `welcomeMessage()` method.
- Registers the object in the Pyro name server.

### `Pyro4/First Example/pyro_client.py`

- Reads a user name from input.
- Connects to `PYRONAME:server` and prints the remote welcome message.

## Pyro4 second example

### `Pyro4/Second Example/chainTopology.py`

- Defines a `Chain` object that forwards a message through a ring of Pyro servers until it returns to the starting node.

### `Pyro4/Second Example/server_chain_1.py`, `server_chain_2.py`, `server_chain_3.py`

- Each file starts one chain node and registers it in the Pyro name server.

### `Pyro4/Second Example/client_chain.py`

- Connects to node `1` and starts the chain call.

## How to run

- Socket time server: start `socket/server.py`, then run `socket/client.py`
- Socket file transfer: start `socket/server2.py`, then run `socket/client2.py`
- Celery examples: start a broker and worker first, then run the corresponding `addTask_main.py`
- Pyro4 examples: start `pyro4-ns`, run the server files, then run the client
