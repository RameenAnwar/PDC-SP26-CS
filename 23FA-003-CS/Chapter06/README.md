# Chapter 6: Task Queues with Celery

---

# 1.Celery

## 1. addTask.py

### What I learned:

I learned how to initialize a Celery application instance and define a basic asynchronous task. This script establishes a connection to a message broker (RabbitMQ via the amqp protocol) and wraps a standard Python addition function using the @app.task decorator to make it executable by background workers.

### How to execute:

Start the Celery worker from your terminal using: celery -A addTask worker --loglevel=info (ensuring your RabbitMQ broker service is running on localhost first).

### Use cases:

Offloading simple, non-blocking computations, sending automated operational emails, or queuing background database updates away from the main application thread.

### Requirements for execution:

The celery library installed along with an active, running RabbitMQ message broker instance accessible at amqp://guest@localhost//.

### Advantages:

Decouples task definition from task execution entirely, allowing workers to scale independently based on the system's workload.

### Disadvantages:

Requires a running external message broker infrastructure to function, adding architectural complexity for incredibly basic operations.

---

## 2. addTask_main.py

### What I learned:

I learned how to trigger a Celery task asynchronously from a client script using the .delay() method. Instead of executing the function locally and blocking the script, .delay() hands off the function arguments to the configured message broker so an available Celery worker can pick up and process the job in the background.

### How to execute:

Run in cmd: python addTask_main.py (while your Celery worker from addTask.py is actively running in another terminal).

### Use cases:

An entry-point application script, web route handler, or API endpoint that fires off heavy tasks to a background queue without making the end-user wait for the execution to finish.

### Requirements for execution:

Importing the task module (addTask) and invoking the task explicitly with the .delay() wrapper.

### Advantages:

Provides an instantaneous, non-blocking handoff that immediately returns an AsyncResult object, ensuring the main application remains highly responsive.

### Disadvantages:

Does not capture or print the return value of the task locally within this script, as configured, because a result backend (like Redis or an RPC database) is not specified to track the output.

# 2. Pyro4

---

## Folder 1: 1st example

### 1. pyro_server.py

#### What I learned:

I learned how to build and launch a Remote Method Invocation (RMI) server. This script establishes a Pyro daemon to listen for incoming network connections, queries the local network to find the central Pyro Name Server, and exposes a clean Python class interface (Server) using the @Pyro4.expose decorator so its methods can be requested remotely.

#### How to execute:

1. First, start the Pyro Name Server in its own window: python -m Pyro4.naming
2. Then, run the server script: python pyro_server.py

#### Use cases:

Creating isolated microservices, sharing computational resources across machines, or creating centralized database handler servers.

#### Requirements for execution:

The Pyro4 package installed and an active, running Pyro Name Server registry available on the network.

#### Advantages:

Completely abstracts low-level socket creation, serialization, and connection protocols, making remote services behave like local dependencies.

#### Disadvantages:

Introduces an absolute dependency on a distinct, single Name Server component; if the Name Server drops offline, clients cannot locate the registered objects.

---

### 2. pyro_client.py

#### What I learned:

I learned how client scripts establish logical bridges to remote processes. By initializing a Pyro4.Proxy wrapper pointing to the logical network name PYRONAME:server, the client delegates the lookup mechanics to the Name Server, fetches the actual URI, and cleanly triggers the distant welcomeMessage method.

#### How to execute:

Run in cmd: python pyro_client.py (making sure both the central Name Server and pyro_server.py are running).

#### Use cases:

Building client apps or lightweight frontends that offload their operational workloads to more powerful remote network clusters.

#### Requirements for execution:

An interactive console for user text inputs and a valid configuration matching the server's registered target name.

#### Advantages:

Decouples client scripts from rigid network configurations; the client never needs hardcoded IP addresses or ports to find the resource.

#### Disadvantages:

The execution pattern is strictly synchronous, causing the client script to pause and hang if network congestion delays the response.

---

## Folder 2: 2nd example

### 1. chainTopology.py

#### What I learned:

I learned how to construct a cyclic pipeline architecture using an object-oriented tracking class (Chain). It maps out message routes by configuring an immediate downstream neighbor, validating that incoming messages haven't caused an infinite cycle, logging its identity, and passing payloads along dynamically via remote proxies.

#### How to execute:

This module contains the shared logic definitions and is not executed directly; it is imported as a dependency into the active node scripts.

#### Use cases:

Simulating ring consensus protocols, managing multi-tier approval token processes, or tracking distributed log pipelines.

#### Requirements for execution:

The module must be saved in the identical directory context alongside the active server scripts to ensure smooth imports.

#### Advantages:

Encapsulates routing rules away from server lifecycles, enabling modular modifications to data handling logic without changing deployment code.

#### Disadvantages:

Lacks built-in error handling for intermediate nodes; a breakdown at any step along the path terminates the entire pipeline immediately.

---

### 2. server_chain_1.py, server_chain_2.py, & server_chain_3.py

#### What I learned:

I learned how to initialize a multi-node, cyclic ring topology across separate process boundaries. Each individual script launches its own independent daemon workspace, instantiates a unique Chain instance tracking a sequential neighbor, and binds its location inside the Name Server under a specific step reference (Node 1 calls 2, Node 2 calls 3, and Node 3 loops back to 1).

#### How to execute:

1. Start the Name Server: python -m Pyro4.naming
2. Open three separate terminal windows and run each script:
.) python server_chain_1.py
.) python server_chain_2.py
.) python server_chain_3.py



#### Use cases:

Setting up distributed sandbox environments to safely evaluate load balancing protocols, routing performance, or ring network topologies.

#### Requirements for execution:

The chainTopology.py class script must exist in the folder path to support node instantiation across all three servers.

#### Advantages:

Achieves robust application isolation; each processing stage operates inside an autonomous environment with dedicated system memory.

#### Disadvantages:

Spawning and coordinating multiple independent scripts manually becomes complex and scales poorly without container orchestration tools like Docker.

---

### 3. client_chain.py

#### What I learned:

I learned how to initiate and capture workflows routed through a complex distributed ring. By targeting the primary entryway node (example.chainTopology.1), the client passes an initial payload list and receives a full execution trace showing every server that processed the data.

#### How to execute:

Run in cmd: python client_chain.py (ensure that the Name Server and all three server_chain_.) nodes are fully active).

#### Use cases:

Triggering decentralized batch processing runs, confirming system topology health, or inspecting processing states across pipeline segments.

#### Requirements for execution:

Requires the entryway target node to be registered and discoverable within the connected Pyro registry network.

#### Advantages:

Maximizes client simplicity; the calling script remains completely unaware of the internal pipeline layout and only interacts with the front node.

#### Disadvantages:

Increases debugging difficulty; errors or unexpected modifications happening deep inside the server chain require inspecting logs scattered across multiple separate terminals.

---

# 3. Sockets

---

## 1. server.py

### What I learned:

I learned how to set up a fundamental TCP stream socket server using IPv4 (`socket.AF_INET`) and the connection-oriented TCP protocol (`socket.SOCK_STREAM`). This script demonstrates how to bind a socket to a local port, listen for incoming connections with a backlog queue, and enter an infinite operational loop to accept client requests, generate a timestamp using `time.ctime()`, and dispatch it back across the network connection.

### How to execute:

Run in cmd: `python server.py` to start the socket listener on your local machine.

### Use cases:

Building basic network listeners, localized background daemons, or dedicated single-purpose network utility servers (like standard NTP or heartbeat monitors).

### Requirements for execution:

The standard `socket` and `time` libraries pre-packaged with Python.

### Advantages:

Extremely lightweight and operates natively with minimal overhead without needing external dependencies or web framework containers.

### Disadvantages:

The loop is strictly blocking; the server handles exactly one client connection at a time, making it highly inefficient for scaling to multiple concurrent connections.

---

## 2. client.py

### What I learned:

I learned how a client script requests a network bridge to a remote socket address. This program handles resolving a local hostname, connecting via a designated port assignment, allocating a 1024-byte input buffer to catch incoming data payloads, and cleanly closing the interface once the data transaction completes.

### How to execute:

Run in cmd: `python client.py` (ensuring that `server.py` is actively running in another command terminal).

### Use cases:

Testing network socket visibility, querying simple remote daemons, or downloading single-line operational flags from a control unit.

### Requirements for execution:

Matching host configurations and network port bindings corresponding directly to the target server's environment.

### Advantages:

Fires up instantly, extracts the data stream payload, and cleanly terminates local system socket links immediately to prevent port resource leakage.

### Disadvantages:

Lacks any fallback architecture or error-handling blocks; if the server drops offline or is unreachable, the client process crashes abruptly.

---

## 3. server2.py

### What I learned:

I learned how to manage streaming transactions like file chunk parsing over a raw network connection. This server binds onto a distinct port (`60000`), listens for an incoming connection, reads an initial confirmation string from the client, opens a local asset file (`mytext.txt`) in binary read mode (`rb`), and streams its contents over the network in 1024-byte block increments before appending a sign-off string.

### How to execute:

Run in cmd: `python server2.py` (ensure an asset named `mytext.txt` is present in the execution folder).

### Use cases:

Building localized file distribution engines, system backup synchronization nodes, or microservice asset delivery channels.

### Requirements for execution:

An active companion text file or data file (`mytext.txt`) to feed the binary read streaming loop.

### Advantages:

Efficient buffer allocation ensures that massive target files can be parsed and dispatched without flooding or overloading the server's RAM footprint.

### Disadvantages:

Improperly closes the active file handle inside the loop block after the first segment read, which can cause resource tracking bugs or script crashes depending on file size.

---

## 4. client2.py

### What I learned:

I learned how to stream incoming data blocks directly into local storage files. The client initiates a greeting message to flag the server, initializes a fresh destination file (`received.txt`) using binary write authorization (`wb`), and maintains an active retrieval loop to catch data increments until the transmission stream terminates.

### How to execute:

Run in cmd: `python client2.py` (while `server2.py` is actively listening on port 60000).

### Use cases:

Automated remote log collectors, client asset patch download agents, or content replication scripts.

### Requirements for execution:

Sufficient local system disk access permissions to generate and append data to files in the current workspace folder.

### Advantages:

Maintains an active tracking structure that logs network activity down to the console during active streaming, simplifying connectivity troubleshooting.

### Disadvantages:

Relies entirely on an open-ended loop (`while True`) that assumes a clean server disconnect (`if not data`); network interruptions can potentially lock the script in an infinite waiting loop.

---

## 5. mytext.txt & received.txt (Data Assets)

### What they are for:

These text files serve as the actual storage layer payload for the file transfer mechanism running in `server2.py` and `client2.py`.

* **`mytext.txt`**: This is the source file situated on the server-side. It holds the baseline text payload ("hello!!!") designed to be opened, read block-by-block, and transferred.
* **`received.txt`**: This is the dynamically generated destination file on the client-side. It captures the incoming raw byte stream and saves the accumulated message along with the connection confirmation appended by the server ("hello!!!->Thankyouforconnecting").

### Use cases:

Simulating real-world network data persistence, validating that file streaming logic doesn't introduce data corruption across the network, and checking byte translation integrity.

---

## 6. addTask.py

### What I learned:

I learned how to initialize a Celery application instance and define an asynchronous background task. This script establishes a connection to an external message broker (RabbitMQ via the `pyamqp` protocol) and registers a simple arithmetic addition function using the `@app.task` decorator so that execution can be handed off away from the local application thread.

### How to execute:

Start the Celery worker process from your console terminal: `celery -A addTask worker --loglevel=info` (ensure your RabbitMQ broker service is up and running first).

### Use cases:

Offloading computationally heavy math functions, processing asynchronous data transactions, or decoupling user-facing code from heavy background workflows.

### Requirements for execution:

The `celery` module installed along with an active, running RabbitMQ message broker instance accessible at `localhost`.

### Advantages:

Provides total isolation of computing tasks, allowing you to easily scale up the number of background worker nodes when task volume increases.

### Disadvantages:

Introduces infrastructural overhead since it depends completely on an external message broker to receive and track queued tasks.

---

## 7. addTask_main.py

### What I learned:

I learned how to trigger a registered Celery task asynchronously using the `.delay()` wrapper technique. Instead of executing the addition function locally and causing the script to block, `.delay(5, 5)` serializes the function arguments, sends them as a message into the broker queue, and allows the script to continue without waiting for the calculation to finish.

### How to execute:

Run in cmd: `python addTask_main.py` (while your background Celery worker from `addTask.py` is actively listening in another terminal session).

### Use cases:

Firing off non-blocking tasks from web server request routes, API gateways, or scheduling loops where user-response latency must be kept low.

### Requirements for execution:

Importing the specific task instance explicitly from the worker-configured module (`addTask`).

### Advantages:

Offers a complete non-blocking interface execution pattern that immediately transfers the task responsibility to the background infrastructure.

### Disadvantages:

Because it triggers the task in a fire-and-forget style without a result backend configured, the client script cannot natively capture, block, or display the function's calculated return value locally.