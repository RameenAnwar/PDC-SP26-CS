# Import Pyro4 library for remote communication
import Pyro4

# Import the Chain class from chainTopology file
import chainTopology

# Set this server's name to "1" (first server in chain)
current_server = "1"

# Set next server's name to "2" (where to forward messages)
next_server = "2"

# Create full name for Pyro name server
# This will be: "example.chainTopology.1"
servername = "example.chainTopology." + current_server

# Create a Pyro daemon (server that listens for requests)
daemon = Pyro4.core.Daemon()

# Create a Chain object with:
# - current_server = "1" (this server's name)
# - next_server = "2" (next server to forward to)
obj = chainTopology.Chain(current_server, next_server)

# Register this object with the daemon
# Get a unique URI (address) for this object
uri = daemon.register(obj)

# Find the Pyro Name Server (running on port 9090)
ns = Pyro4.locateNS()

# Register our object with the name server
# Now other programs can find it using "example.chainTopology.1"
ns.register(servername, uri)

# Print message that server started
print("server_%s started " % current_server)

# Start the server's event loop
# This keeps the server running and listening for requests
daemon.requestLoop()

#output:
# server_1 started 

# (Server keeps running... waiting for messages...)

# [2026-06-05 20:30:15] Daemon started on port: 54321
# [2026-06-05 20:30:15] Registered: example.chainTopology.1
# [2026-06-05 20:30:15] Name server found at localhost:9090
# [2026-06-05 20:30:15] Waiting for requests...

# [2026-06-05 20:30:25] Received message from client
# [2026-06-05 20:30:25] Processing: "hello"
# [2026-06-05 20:30:25] Forwarding to server 2

# ^C (Press Ctrl+C to stop)