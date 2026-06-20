# server_chain_1.py  --  Chapter 6: Pyro4 Chain server #1 (forwards to #2)
# RUN ORDER:  start the name server, then run server_chain_1.py, _2.py, _3.py.
#
# ----------------------- CODE (commented out) -----------------------
# import Pyro4
# import chainTopology
# current_server = "1"
# next_server = "2"                                   # this server forwards to server 2
# servername = "example.chainTopology." + current_server
# daemon = Pyro4.core.Daemon()
# obj = chainTopology.Chain(current_server, next_server)
# uri = daemon.register(obj)
# ns = Pyro4.locateNS()
# ns.register(servername, uri)
# print("server_%s started " % current_server)
# daemon.requestLoop()
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# server_1 started
# 1 forwarding the message to the object 2
# --------------------------------------------------------------------
