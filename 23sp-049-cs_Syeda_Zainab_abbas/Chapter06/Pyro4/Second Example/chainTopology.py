# chainTopology.py  --  Chapter 6: Pyro4 Chain Topology (shared object)
# Defines a Chain object. Each server holds one Chain that forwards a message to
# the NEXT server in the ring. When the message returns to where it started, the
# chain is "closed". Imported by server_chain_1/2/3.py.
#
# ----------------------- CODE (commented out) -----------------------
# import Pyro4
# @Pyro4.expose
# class Chain(object):
#     def __init__(self, name, current_server):
#         self.name = name
#         self.current_serverName = current_server   # name of the NEXT server
#         self.current_server = None
#     def process(self, message):
#         if self.current_server is None:             # lazily connect to next server
#             self.current_server = Pyro4.core.Proxy(
#                 "PYRONAME:example.chainTopology." + self.current_serverName)
#         if self.name in message:                    # message came back to us
#             print("Back at %s; the chain is closed!" % self.name)
#             return ["complete at " + self.name]
#         else:
#             print("%s forwarding the message to the object %s"
#                   % (self.name, self.current_serverName))
#             message.append(self.name)               # leave our mark, forward on
#             result = self.current_server.process(message)
#             result.insert(0, "passed on from " + self.name)
#             return result
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (no output on its own - it is used by the three chain servers below)
# --------------------------------------------------------------------
