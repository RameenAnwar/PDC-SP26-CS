# Import the Pyro4 library to facilitate Remote Procedure Calls (RPC) on the server side
import Pyro4

# Define a standard Python class that contains the logic/methods we want to expose remotely
class Server(object):
    # This decorator explicitly exposes this specific method to remote clients
    # Without @Pyro4.expose, the client cannot call this function remotely due to security restrictions
    @Pyro4.expose
    def welcomeMessage(self, name):
        # Concatenate the greeting with the string representation of the received name and return it
        return ("Hi welcome " + str(name))

# Define a function to initialize, configure, and start the remote server application
def startServer():
    # Instantiate an object of our custom Server class
    server = Server()
    
    # Initialize a Pyro daemon, which acts as the background listener managing incoming network connections
    daemon = Pyro4.Daemon()             
    
    # Locate the active Pyro Name Server running on the network (acts like a phonebook for remote objects)
    ns = Pyro4.locateNS()
    
    # Register our server instance with the daemon, which generates a unique Uniform Resource Identifier (URI)
    uri = daemon.register(server)  
    
    # Register that generated URI inside the Name Server book under the simple logical lookup name "server"
    ns.register("server", uri)   
    
    # Print the full, complex URI string to the console for monitoring and verification purposes
    print("Ready. Object uri =", uri)
    
    # Start the daemon's infinite event loop, keeping the server alive and waiting for incoming client requests
    daemon.requestLoop()                  

# Standard execution guard to ensure the server only starts if this specific script is run directly
if __name__ == "__main__":
    startServer()