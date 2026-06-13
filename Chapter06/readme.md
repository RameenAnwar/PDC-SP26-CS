# Chapter 06 — Distributed Services (sockets, Celery, Pyro4)

This chapter contains small examples showing TCP sockets, a Celery task, and two Pyro4 example sets (a simple RPC and a chain topology).

Socket examples (folder `socket`):

- `server.py` and `client.py`:
  - Basic TCP server (`server.py`) that listens for connections, sends the current time and closes the connection.
  - `client.py` connects to the server, receives up to 1024 bytes and prints the server time.

- `server2.py` and `client2.py`:
  - `server2.py` accepts a client request and sends the contents of `mytext.txt` to the client in 1024-byte chunks and a final message.
  - `client2.py` connects, sends a greeting, receives the file into `received.txt`, and writes chunks until the socket closes.

- `addTask.py` and `addTask_main.py` (in `socket` folder):
  - These are Celery examples (oddly placed under `socket`); `addTask.py` defines a Celery `add` task and `addTask_main.py` calls `add.delay(5,5)`.
  - Running them requires a Celery broker (the example uses RabbitMQ via `pyamqp://guest@localhost//`).

Pyro4 examples:

- `First Example` (folder):
  - `pyro_server.py` defines a `Server` class exposing `welcomeMessage` via Pyro4, registers it with the Pyro name server and starts the daemon.
  - `pyro_client.py` looks up the server via `PYRONAME:server` and invokes `welcomeMessage(name)` interactively.

- `Second Example` (chain topology folder):
  - Contains `chainTopology.py`, three `server_chain_X.py` scripts and `client_chain.py`.
  - `chainTopology.Chain` is a Pyro-exposed object that forwards a message along a chain of Pyro servers until it returns to the origin, demonstrating remote method calls and forwarding.
  - Each `server_chain_*.py` registers one chain node in the Pyro name server; `client_chain.py` invokes the chain starting at node 1.

Celery (folder `Celery`):

- `addTask.py` and `addTask_main.py` mirror the small Celery task shown above (task creation and a delayed invocation). Requires Celery and a message broker to run.

How to run

- Socket examples: run `server.py` then `client.py` from the same host to see time exchange. For file transfer use `server2.py` and `client2.py`.
- Pyro4 examples: ensure a Pyro4 Name Server is running (`pyro4-ns`), start each server process, then run the client.
- Celery examples: start a broker (RabbitMQ), then run a Celery worker and execute `addTask_main.py`.

Notes

- Many examples assume local services (name server, RabbitMQ) are available and configured; they will error if the service is not running.
- Socket examples are minimal and lack production hardening (timeouts, chunking edge cases, error handling).
