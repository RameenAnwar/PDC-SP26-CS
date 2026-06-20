Python TCP Time Server:
A simple Python script demonstrating how to create a basic TCP server using the built-in socket library. This server listens for incoming client connections, sends back the current system time, and then smoothly disconnects.

⚙️ Prerequisites:
Python version: 3.x
No external libraries are required as socket and time are part of the Python Standard Library.

🚀 How to Run:
Because this is a server script, it needs to be running in the background before any clients attempt to connect to it.

Step 1: Start the server:
Open your terminal and run the script:
Bash
python server.py
The server will start silently and wait for connections.

Step 2: Connect a client:
Use a companion Python client script or a tool like telnet or netcat targeting port 9999 to connect to the server and receive the time.

Step 3: Stopping the server:
Because the server runs in an infinite loop (while True:), it will not stop on its own. To shut it down, click into your server terminal and press Ctrl + C.

🧠 What it Does:
This script represents the foundational steps of hosting a network service:
Socket Creation: socket.socket() initializes a new socket using IPv4 (AF_INET) and TCP (SOCK_STREAM).

Binding: serversocket.bind((host, port)) assigns the socket to the local machine's hostname and explicitly reserves port 9999 for this service.

Listening: serversocket.listen(5) tells the OS to start listening for incoming connections, allowing a queue of up to 5 pending client requests at a time.

Accepting Connections: The script enters an infinite while True: loop. serversocket.accept() blocks and waits until a client attempts to connect. Once connected, it returns a new socket dedicated to that specific client, along with the client's IP address.

Sending Data: It calculates the current time, formats it as a string, encodes it into raw ASCII bytes, and sends it directly to the client.

Teardown: It immediately closes the client socket to free up resources, then loops back around to wait for the next person to connect.

📊 Expected Output:
When the server is running and a client successfully connects, your server terminal will log the connection details:
Connected with[addr],[port]('192.168.1.10', 54321)
Meanwhile, the connected client will receive a payload containing the timestamp:
Mon Jun  8 04:28:12 2026
