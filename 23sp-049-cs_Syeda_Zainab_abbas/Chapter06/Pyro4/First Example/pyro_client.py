# pyro_client.py  --  Chapter 6: Remote Method Invocation with Pyro4 (Client)
# Looks up the remote "server" object by name and calls welcomeMessage() on it
# AS IF it were local. The call actually runs on the server process.
# RUN:  python pyro_client.py   (name server + pyro_server.py must be running)
#
# ----------------------- CODE (commented out) -----------------------
# import Pyro4
# name = input("What is your name? ").strip()
# server = Pyro4.Proxy("PYRONAME:server")    # proxy to the remote object
# print(server.welcomeMessage(name))         # remote method call
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# What is your name? Zainab
# Hi welcome Zainab
# --------------------------------------------------------------------
