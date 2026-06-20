# client_chain.py  --  Chapter 6: Pyro4 Chain client
# Sends ["hello"] into server 1. The message travels 1 -> 2 -> 3 -> 1 and comes
# back with each server's note attached, proving the distributed ring works.
# RUN:  python client_chain.py   (name server + all 3 chain servers must be running)
#
# ----------------------- CODE (commented out) -----------------------
# from __future__ import print_function
# import Pyro4
# obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")
# print("Result=%s" % obj.process(["hello"]))
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# Result=['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']
# --------------------------------------------------------------------
