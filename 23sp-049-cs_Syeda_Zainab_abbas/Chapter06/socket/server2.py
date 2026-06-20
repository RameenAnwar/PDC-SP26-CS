# server2.py  --  Chapter 6: Socket programming (file-transfer server)
# Waits for a client, then sends the contents of mytext.txt over the socket.
# RUN:  python server2.py   (then run client2.py)
#
# ----------------------- CODE (commented out) -----------------------
# import socket
# port = 60000
# s = socket.socket()
# host = socket.gethostname()
# s.bind((host, port))
# s.listen(15)
# print('Server listening....')
# while True:
#     conn, addr = s.accept()
#     print('Got connection from', addr)
#     data = conn.recv(1024)
#     print('Server received', repr(data.decode()))
#     filename = 'mytext.txt'
#     f = open(filename, 'rb')
#     l = f.read(1024)
#     while (l):                       # keep sending until the file is fully read
#         conn.send(l)
#         print('Sent', repr(l.decode()))
#         l = f.read(1024)
#         f.close()
#         print('Donesending')
#         conn.send('->Thank you for connecting'.encode())
#         conn.close()
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# Server listening....
# Got connection from ('127.0.0.1', 52012)
# Server received 'HelloServer!'
# Sent '<contents of mytext.txt>'
# Donesending
# --------------------------------------------------------------------
