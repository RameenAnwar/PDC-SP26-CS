Pyro4 Chain Topology Example:
This repository demonstrates a network chain (or ring) topology using Remote Procedure Calls (RPC) via the `Pyro4` library. In this architecture, a client sends a message to the first server node, which then passes it to the second, and so on, until the message loops back to the start.

Prerequisites:
To run this architecture, you need Python installed on your system along with the `Pyro4` library.
bash
pip install Pyro4

What it Does:
This codebase is split into two main logical components:

1. The Server Node (`Chain` class):
This class acts as a single link in the chain.
* Initialization: It is created with its own `name` and the name of the `current_server` (which is technically the next server it should forward data to).
* Connection on Demand: Inside the `process` method, it dynamically connects to the next server using `Pyro4.core.Proxy(...)` only when a message is received.
* Loop Detection: It checks if its own `name` is already inside the `message` list. If it is, that means the message has traveled through the whole chain and returned to the start. It closes the chain and returns a `complete` status.
* Forwarding: If it hasn't seen the message before, it appends its name to the list and calls the `process` method on the next server.
2. The Client Script:
The client initializes the entire chain reaction. It connects to the very first node in the Name Server registry (`PYRONAME:example.chainTopology.1`) and calls the `.process(["hello"])` method, passing in the initial payload.

How to Run (Architecture Setup):
Because this represents a distributed topology, running it requires a Pyro Name Server and multiple active server nodes.
Note: The provided code defines the `Chain` class but does not include the script to start the servers. To actually run this, you would need a setup script that registers multiple instances of the `Chain` class with the Name Server.

Step 1: Start the Name Server:
Open a terminal and start the Pyro phonebook:
bash
python -m Pyro4.naming

Step 2: Start the Nodes (Requires additional setup script):
You would need to write and run a script that creates your nodes, links them together, and starts the daemon. For example:

* Node 1 (named `"1"`) forwards to `"2"`
* Node 2 (named `"2"`) forwards to `"3"`
* Node 3 (named `"3"`) forwards back to `"1"` (closing the ring)

Step 3: Run the Client
Once your nodes are running and waiting for requests, open a new terminal and run your client script:
bash
python client.py

Expected Output:
If you set up a 3-node chain as described above, running the client script will result in the servers passing the message around until Node 1 recognizes it has already signed the message.
The client terminal will output the unwound stack trace of the journey:
Result=['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']
