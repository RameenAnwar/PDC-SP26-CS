Pyro4 Server Chain Nodes (1, 2, and 3):
These scripts represent the active server nodes required to run the Pyro4 Chain Topology example. They configure three distinct servers that link together to form a closed loop (Ring Topology).

Prerequisites:
To run this architecture, ensure you have Python and `Pyro4` installed, and that you have the `chainTopology.py` file (which contains the `Chain` class definition) saved in the same directory as these scripts.
bash
pip install Pyro4

How to Run:
Because this is a distributed system, you need to run the Name Server and each of these three server nodes in entirely separate terminal windows simultaneously.

Step 1: Start the Pyro Name Server
Open your first terminal and start the registry:
bash
python -m Pyro4.naming

Step 2: Start Server 1
Open a second terminal and run the first script (e.g., `server1.py`).
bash
python server1.py

Step 3: Start Server 2
Open a third terminal and run the second script (e.g., `server2.py`).
bash
python server2.py

Step 4: Start Server 3
Open a fourth terminal and run the third script (e.g., `server3.py`).
bash
python server3.py
Once all three servers are running, you can execute your client script in a fifth terminal to watch the message travel through the network!

What it Does:
These scripts establish the routing rules for the distributed network and expose them to the Pyro Name Server.

1. Server 1: Registers itself as `example.chainTopology.1`. It is explicitly hardcoded to forward any received messages to Server 2.
2. Server 2: Registers itself as `example.chainTopology.2`. It is explicitly hardcoded to forward any received messages to Server 3.
3. Server 3: Registers itself as `example.chainTopology.3`. It is explicitly hardcoded to forward any received messages back to Server 1, successfully closing the loop.
Each script initiates a `Pyro4.core.Daemon()`, registers its respective object with the naming service (`ns.register(...)`), and enters an infinite `daemon.requestLoop()` to patiently wait for the client or the previous server in the chain to send a message.

Expected Output:
As you start each server in their respective terminals, they will print a simple confirmation message and then hang, waiting for requests:

Terminal 2:
server_1 started

Terminal 3:
server_2 started

Terminal 4:
server_3 started
