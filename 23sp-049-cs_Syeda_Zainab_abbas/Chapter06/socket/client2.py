# client2.py  --  Chapter 6: Socket programming (file-transfer client)
# Connects, says hello, then receives the file data and saves it to received.txt.
# RUN:  python client2.py   (server2.py must be running first)
#
# ----------------------- CODE (commented out) -----------------------
# import socket
# s = socket.socket()
# host = socket.gethostname()
# port = 60000
# s.connect((host, port))
# s.send('HelloServer!'.encode())
# with open('received.txt', 'wb') as f:     # save incoming data to this file
#     print('file opened')
#     while True:
#         print('receiving data...')
#         data = s.recv(1024)
#         if not data:                       # empty = transfer finished
#             break
#         print('Data=>', data.decode())
#         f.write(data)
# f.close()
# print('Successfully get the file')
# s.close()
# print('connection closed')
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# file opened
# receiving data...
# Data=> <contents of mytext.txt>
# receiving data...
# Successfully get the file
# connection closed
# --------------------------------------------------------------------
