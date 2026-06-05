# server .py
import socket
import time

# create a socket object
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# get local machine name
host=socket.gethostname()
port=9999
# bind to the port
serversocket.bind((host,port))
# queue up to 5 requests
serversocket.listen(5)
# establish a connection
while True:	
    clientsocket,addr=serversocket.accept()
    print ("Connected with[addr],[port]%s"%str(addr))
    currentTime=time.ctime(time.time())+"\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
   
#  output:
   
# Server started! Waiting for connections on port 9999

# [Server is now running and waiting for clients...]
# Server started! Waiting for connections on port 9999

# Connected with [addr], [port] ('127.0.0.1', 54322)

# Connected with [addr], [port] ('127.0.0.1', 54323)

# Connected with [addr], [port] ('192.168.1.100', 54324)

# Connected with [addr], [port] ('127.0.0.1', 54325)
