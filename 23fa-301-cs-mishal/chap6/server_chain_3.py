# Import the print_function from __future__ to enable Python 3 style print()
# (Ensures print() works consistently across Python versions)
from __future__ import print_function

# Import the Pyro4 library for distributed object communication
import Pyro4

# Import the chainTopology module which contains the Chain class
import chainTopology

# Set the name of this chain node (third node in the chain)
current_server = "3"

# Set the name of the next node this node will forward to
# Here it points back to node "1", completing the circular chain
next_server = "1"

# Build the full name under which this object will be registered in the Pyro4 name server
# Example: "example.chainTopology.3"
servername = "example.chainTopology." + current_server

# Create a Pyro4 daemon (handles network connections for this server)
daemon = Pyro4.core.Daemon()

# Create an instance of the Chain class, passing its own name and the next server's name
obj = chainTopology.Chain(current_server, next_server)

# Register the object with the daemon, obtaining a unique URI
uri = daemon.register(obj)

# Locate the Pyro4 name server (must be running already)
ns = Pyro4.locateNS()

# Register this object's URI with the name server under the constructed servername
ns.register(servername, uri)

# Print a message indicating this server has started
print("server_%s started" % current_server)

# Start the daemon's event loop – this blocks forever and handles incoming requests
daemon.requestLoop()

#output
# server_3 started
# 3 forwarding the message to the object 1
