# server.py  --  Chapter 6: Socket programming (time server)
# A TCP server that, for every client that connects, sends back the current time
# and closes that connection. Demonstrates the basic socket workflow:
# socket -> bind -> listen -> accept -> send -> close.
# RUN:  python server.py   (then run client.py in another terminal)
#
# ----------------------- CODE (commented out) -----------------------
# import socket
# import time
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
# host = socket.gethostname()
# port = 9999
# serversocket.bind((host, port))     # attach the socket to host:port
# serversocket.listen(5)              # allow up to 5 queued connections
# while True:
#     clientsocket, addr = serversocket.accept()   # wait for a client to connect
#     print("Connected with[addr],[port]%s" % str(addr))
#     currentTime = time.ctime(time.time()) + "\r\n"
#     clientsocket.send(currentTime.encode('ascii'))  # send the time
#     clientsocket.close()                             # close this client's connection
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (server terminal, when a client connects)
# Connected with[addr],[port]('127.0.0.1', 51544)
# --------------------------------------------------------------------
