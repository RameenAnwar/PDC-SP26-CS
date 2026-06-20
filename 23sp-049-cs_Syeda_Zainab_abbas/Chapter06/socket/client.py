# client.py  --  Chapter 6: Socket programming (time client)
# Connects to the time server, receives the time string, and prints it.
# RUN:  python client.py   (server.py must be running first)
#
# ----------------------- CODE (commented out) -----------------------
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 9999
# s.connect((host, port))             # connect to the server
# tm = s.recv(1024)                   # receive up to 1024 bytes
# s.close()
# print("Time connection server:%s" % tm.decode('ascii'))
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# Time connection server:Sat Jun 20 14:05:31 2026
# --------------------------------------------------------------------
