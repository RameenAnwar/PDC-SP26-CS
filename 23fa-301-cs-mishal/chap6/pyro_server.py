# Import the Pyro4 library for distributed object communication (RPC)
import Pyro4

# Define a class that will be exposed to remote clients
class Server(object):
    
    # Decorate the method with @Pyro4.expose to make it remotely callable
    @Pyro4.expose
    def welcomeMessage(self, name):
        # Return a welcome string using the provided name
        return ("Hi welcome " + str(name))

# Function to start the Pyro4 server
def startServer():
    # Create an instance of the Server class
    server = Server()
    
    # Create a Pyro4 daemon (handles network connections and dispatching)
    daemon = Pyro4.Daemon()
    
    # Locate the Pyro4 name server (must be running separately)
    ns = Pyro4.locateNS()
    
    # Register the server object with the daemon, obtaining a unique URI
    uri = daemon.register(server)
    
    # Register the object in the name server under the name "server"
    # This allows clients to look it up by name instead of using the raw URI
    ns.register("server", uri)
    
    # Print the URI to the console for debugging/information
    print("Ready. Object uri =", uri)
    
    # Start the event loop, waiting for incoming client requests
    # This method blocks until the daemon is shut down
    daemon.requestLoop()

# Standard Python idiom: run startServer() only when this script is executed directly
if __name__ == "__main__":
    startServer()