# server_chain_2.py  --  Chapter 6: Pyro4 Chain server #2 (forwards to #3)
#
# ----------------------- CODE (commented out) -----------------------
# from __future__ import print_function
# import Pyro4
# import chainTopology
# current_server = "2"
# next_server = "3"
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
# server_2 started
# 2 forwarding the message to the object 3
# --------------------------------------------------------------------
