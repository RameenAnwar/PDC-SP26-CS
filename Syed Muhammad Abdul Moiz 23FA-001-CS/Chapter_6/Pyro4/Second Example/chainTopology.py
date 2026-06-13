# Import the Pyro4 library to handle Remote Procedure Calls (RPC) across the distributed servers
import Pyro4

# This decorator exposes the entire Chain class so its methods can be called remotely by other nodes
@Pyro4.expose
class Chain(object):
    # The constructor initializes each server node with its own name and the name of the next server in the chain
    def __init__(self, name, current_server):
        self.name = name                      # Store the name of the current server node (e.g., "Node A")
        self.current_serverName = current_server  # Store the name of the next target server in the sequence (e.g., "Node B")
        self.current_server = None            # Initialize the proxy reference to the next server as None (lazy loading)
    
    # The main processing method that handles passing messages along the chain topology
    def process(self, message):
        # If the proxy connection to the next server hasn't been established yet, create it now
        if self.current_server is None:
            # Look up the next server's location from the Name Server using its dynamically concatenated name
            self.current_server = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.current_serverName)
        
        # Base Case: Check if this node's name is already in the message list (meaning the message has traveled full circle)
        if self.name in message:
            # Print a message on the console stating that the loop has completed and the chain is securely closed
            print("Back at %s; the chain is closed!" % self.name)
            # Return a list indicating where the chain execution successfully ended
            return ["complete at " + self.name]
        
        # Recursive Case: If the message hasn't visited this node yet, forward it to the next server
        else:
            # Print a tracking log showing which node is currently forwarding the message to whom
            print("%s forwarding the message to the object %s" % (self.name, self.current_serverName))
            # Append the current node's name to the message list to mark it as visited
            message.append(self.name)
            
            # Remotely call the 'process' method on the next server in the chain and wait for its downstream result
            result = self.current_server.process(message)
            
            # As the execution comes back up the call stack, insert a tracking string at the beginning of the result list
            result.insert(0, "passed on from " + self.name)
            # Return the updated tracking list back to the previous caller
            return result