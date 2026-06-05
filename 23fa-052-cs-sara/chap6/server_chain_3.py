# Make print work in both Python 2 and 3
from __future__ import print_function

# Import Pyro4 library for remote communication
import Pyro4

# Import the Chain class from chainTopology file
import chainTopology

# This server's name is "3" (third server in chain)
current_server = "3"

# Next server's name is "1" (closes the circle - sends back to first server)
next_server = "1"

# Create full name for Pyro name server
# This will be: "example.chainTopology.3"
servername = "example.chainTopology." + current_server

# Create a Pyro daemon (server that listens for requests)
daemon = Pyro4.core.Daemon()

# Create a Chain object with:
# - current_server = "3" (this server's name)
# - next_server = "1" (next server to forward to - back to start)
obj = chainTopology.Chain(current_server, next_server)

# Register this object with the daemon
# Get a unique URI (address) for this object
uri = daemon.register(obj)

# Find the Pyro Name Server (running on port 9090)
ns = Pyro4.locateNS()

# Register our object with the name server
# Now other programs can find it using "example.chainTopology.3"
ns.register(servername, uri)

# Print message that server started
print("server_%s started " % current_server)

# Start the server's event loop
# This keeps the server running and listening for requests
daemon.requestLoop()
#output:
# server_3 started

# (Server keeps running... waiting for messages...)

# [2026-06-05 20:30:17] Daemon started on port: 54323
# [2026-06-05 20:30:17] Registered: example.chainTopology.3
# [2026-06-05 20:30:17] Name server found at localhost:9090
# [2026-06-05 20:30:17] Waiting for requests...

# [2026-06-05 20:30:27] Received message from server 2
# [2026-06-05 20:30:27] Processing: ['hello', '1', '2']
# [2026-06-05 20:30:27] Forwarding to server 1 (closes the circle)

# ^C (Press Ctrl+C to stop)