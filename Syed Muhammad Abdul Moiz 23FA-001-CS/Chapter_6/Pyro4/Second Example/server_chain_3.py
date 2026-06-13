# Import print_function from future module to ensure compatibility across different Python versions
from __future__ import print_function
# Import the Pyro4 library to set up the remote object server network
import Pyro4
# Import our custom 'chainTopology' module which contains the definition of the Chain class
import chainTopology

# Define the logical identifier/name of this specific current server node (Node 3)
current_server = "3"
# Define the identifier of the next server node, pointing back to "1" to close the distributed loop/ring
next_server = "1"

# Dynamically construct the full unique name for this server node to register inside the Name Server book
servername = "example.chainTopology." + current_server

# Initialize a Pyro core Daemon object to handle incoming TCP/IP socket connections for this node
daemon = Pyro4.core.Daemon()

# Create an instance of our Chain class, passing this server's identity ("3") and its target next server ("1")
obj = chainTopology.Chain(current_server, next_server)

# Register our created Chain object instance with the local daemon to generate its unique network URI
uri = daemon.register(obj)

# Locate the active running Pyro Name Server on the local network (the central phonebook directory)
ns = Pyro4.locateNS()

# Map the readable 'servername' string to the generated technical 'uri' in the Name Server's records
ns.register(servername, uri)

# Enter the service loop.
# Print a confirmation message to the terminal showing that Server 3 has been successfully initialized and started
print("server_%s started " % current_server)

# Start the daemon's main server execution loop, keeping it active and listening endlessly for remote calls
daemon.requestLoop()