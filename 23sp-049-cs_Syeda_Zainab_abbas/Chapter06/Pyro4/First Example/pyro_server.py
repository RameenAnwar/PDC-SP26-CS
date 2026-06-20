# pyro_server.py  --  Chapter 6: Remote Method Invocation with Pyro4 (Server)
# Pyro4 lets you call methods on objects living in another process/machine.
# This server exposes welcomeMessage(name) and registers it with the Pyro name server.
# RUN:  1) python -m Pyro4.naming      (start the name server)
#       2) python pyro_server.py
#
# ----------------------- CODE (commented out) -----------------------
# import Pyro4
# class Server(object):
#     @Pyro4.expose                       # makes this method callable remotely
#     def welcomeMessage(self, name):
#         return ("Hi welcome " + str(name))
# def startServer():
#     server = Server()
#     daemon = Pyro4.Daemon()             # the Pyro server engine
#     ns = Pyro4.locateNS()               # find the running name server
#     uri = daemon.register(server)       # register our object -> get its URI
#     ns.register("server", uri)          # give it the friendly name "server"
#     print("Ready. Object uri =", uri)
#     daemon.requestLoop()                # wait for and handle remote calls
# if __name__ == "__main__":
#     startServer()
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# Ready. Object uri = PYRO:obj_<random-id>@localhost:<port>
# (server now waits in its request loop for client calls)
# --------------------------------------------------------------------
