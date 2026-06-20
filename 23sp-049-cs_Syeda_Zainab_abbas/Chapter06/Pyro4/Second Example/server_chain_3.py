# server_chain_3.py  --  Chapter 6: Pyro4 Chain server #3 (forwards back to #1)
# Server 3 forwards to server 1, closing the ring 1 -> 2 -> 3 -> 1.
#
# ----------------------- CODE (commented out) -----------------------
# from __future__ import print_function
# import Pyro4
# import chainTopology
# current_server = "3"
# next_server = "1"                                   # ring closes back to server 1
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
# server_3 started
# 3 forwarding the message to the object 1
# 1 ... Back at 1; the chain is closed!
# --------------------------------------------------------------------
