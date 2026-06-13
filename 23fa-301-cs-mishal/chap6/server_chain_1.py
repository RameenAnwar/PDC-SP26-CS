# Import the Pyro4 library for distributed object communication
import Pyro4

# Import the chainTopology module which contains the Chain class
import chainTopology

# Set the name of this chain node (first node in the chain)
current_server = "1"

# Set the name of the next node this node will forward to
next_server = "2"

# Build the full name under which this object will be registered in the Pyro4 name server
# Example: "example.chainTopology.1"
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

#ouptut
# server_1 started
# 1 forwarding the message to the object 2
# Back at 1; the chain is closed!