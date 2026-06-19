import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Hi welcome " + str(name))

def startServer():
    server = Server()

    # Create a Pyro4 daemon to dispatch incoming calls
    daemon = Pyro4.Daemon()

    # Locate the Pyro4 nameserver
    ns = Pyro4.locateNS()

    # Register the server object with the daemon
    uri = daemon.register(server)

    # Register the object under the name "server" in the nameserver
    ns.register("server", uri)

    print("Ready. Object uri =", uri)

    # Start the event loop, waiting for client calls
    daemon.requestLoop()

if __name__ == "__main__":
    startServer()