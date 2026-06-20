Pyro4 Client-Server RPC Example
This repository contains a minimal Python application demonstrating Remote Procedure Calls (RPC) using the `Pyro4` (Python Remote Objects) library. It showcases how a client script can seamlessly execute methods on a separate, remotely hosted server object.

Prerequisites:
To run this code, you need Python installed on your system along with the `Pyro4` library.
Install Pyro4:
bash
pip install Pyro4

How to Run:
Because this architecture relies on a central registry to locate services, you must run three separate terminal windows in a specific order.

Step 1: Start the Pyro Name Server
Open your first terminal and start the built-in Pyro Name Server. This acts as a phonebook for your remote objects.

bash
python -m Pyro4.naming
or simply run: pyro4-ns

Step 2: Start the Application Server
Open a second terminal in the directory containing your server script and run it. It will register itself with the Name Server and wait for connections.
bash
python server.py

Step 3: Run the Client
Open a third terminal and run the client script.
bash
python client.py

What it Does:
This architecture is split into two Python files:
1. The Server (server.py)
* @Pyro4.expose: This decorator explicitly marks the `welcomeMessage` method as safe to be called over the network.
* The Daemon: Pyro4.Daemon() creates a background server that listens for incoming network requests.
* The Name Server Registry: Pyro4.locateNS() finds the Name Server we started in Step 1. The daemon then registers our Python object under the simple alias `"server"` (`ns.register("server", uri)`), so clients don't need to memorize complex IP addresses or URIs.
* The Loop: daemon.requestLoop() keeps the script running infinitely, waiting for clients to connect.

The Client (`client.py`)
* User Input: It prompts the user to type their name.
* The Proxy Object: Pyro4.Proxy("PYRONAME:server") connects to the Name Server, looks up who is registered as `"server"`, and creates a local "dummy" object (the proxy) that acts exactly like the remote server object.
* Remote Execution: When the client calls `server.welcomeMessage(name)`, it feels like a normal local function call, but `Pyro4` actually sends the data across the network, executes the math/logic on the server, and brings the string result back to print it.

Example Output:
In the Server Terminal:
Ready. Object uri = PYRO:obj_4829abcd1234@localhost:51234

In the Client Terminal:

What is your name? Abdur Rafay
Hi welcome Abdur Rafay
