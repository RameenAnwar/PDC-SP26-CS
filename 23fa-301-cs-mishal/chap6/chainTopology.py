# Import the Pyro4 library for distributed object communication (RPC)
import Pyro4

# Decorate the Chain class with @Pyro4.expose to make its methods
# remotely callable by other Pyro4 clients/servers
@Pyro4.expose
class Chain(object):
    # Constructor: initializes a chain node with a name and the next server's name
    def __init__(self, name, current_server):
        self.name = name                      # This node's own name (e.g., "A")
        self.current_serverName = current_server  # Name of the next node in the chain
        self.current_server = None            # Will hold the proxy to the next node (lazy init)

    # The main method that processes messages along the chain
    def process(self, message):
        # Lazy initialization: if the proxy to the next server doesn't exist yet,
        # create it by looking up the Pyro4 name server
        if self.current_server is None:
            # Construct the full name registered in Pyro4 name server
            # Example: "example.chainTopology.B"
            proxy_name = "PYRONAME:example.chainTopology." + self.current_serverName
            self.current_server = Pyro4.core.Proxy(proxy_name)

        # Check if this node's name already appears in the message list
        # If yes, the message has come full circle → chain is closed
        if self.name in message:
            print("Back at %s; the chain is closed!" % self.name)
            # Return a single-element list indicating completion
            return ["complete at " + self.name]
        else:
            # This node hasn't seen the message yet, so forward it
            print("%s forwarding the message to the object %s" % (self.name, self.current_serverName))
            # Append this node's name to the message list (to track the path)
            message.append(self.name)
            # Call the process() method of the next node in the chain
            result = self.current_server.process(message)
            # Insert a string at the beginning of the result (reverse path trace)
            result.insert(0, "passed on from " + self.name)
            return result