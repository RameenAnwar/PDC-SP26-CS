**************************************************************************************************
**Chapter: 06       Name: Javaria Owais        Roll Number: 23FA-017-CS**
**************************************************************************************************

## Celery 
This example demonstrates the basic usage of **Celery**, a distributed task queue used to execute tasks asynchronously. The program defines a simple addition task and submits it to a Celery worker for execution.

### Main Concept
- Celery allows tasks to run asynchronously
- Tasks are placed in a message queue
- Workers retrieve and execute tasks
- Results can be collected later

### Code Interpretation
**File 1: addTask.py**
This file creates the Celery application and defines a task.

*Importing Modules*
from celery import Celery
- Imports the Celery framework.

*Creating Celery Application*
app = Celery('addTask', broker='amqp://guest@localhost//')
- Creates a Celery application named `addTask`.
- Uses RabbitMQ as the message broker.
- The broker is responsible for storing and forwarding tasks.

*Defining a Task*
@app.task
def add(x, y):
    return x + y
- `@app.task` converts the function into a Celery task.
- Accepts two numbers.
- Returns their sum.
- Example:
    add(5,5) = 10

**File 2: addTask_main.py**
This file submits the task for execution.

*Importing Task Module*
import addTask
- Imports the Celery application and task.

*Sending Task to Queue*
result = addTask.add.delay(5,5)
- `delay()` sends the task asynchronously.
- The task is placed in the message queue.
- A worker process executes it later.
- Equivalent to add(5,5) but executed asynchronously through Celery.

### Program Execution
> RabbitMQ must be running before executing the program.

*Start Celery Worker*
celery -A addTask worker --loglevel=info

*Run Client Program*
python runTask.py

### Output Behavior
Worker Output:
Task addTask.add received
Task addTask.add succeeded

Task Result:
10

### Advantages
- Executes tasks asynchronously
- Improves application responsiveness
- Supports distributed computing
- Scales across multiple workers

### Limitations
- Requires a message broker
- Additional setup and configuration
- More complex than normal function calls

**************************************************************************************************

## Pyro4 Client-Server 
This example demonstrates distributed computing using **Pyro4 (Python Remote Objects)**.
Pyro4 allows a client program to call methods on a remote object as if it were a local Python object.
- A server exposes methods for remote access
- A client connects to the server
- The client invokes methods remotely
- Communication occurs through Pyro4

### Key Concepts
**Pyro4**
A distributed computing framework that enables remote method invocation in Python.

**Proxy**
A local object representing a remote object.

**Name Server**
A directory service used to locate remote objects by name.

**Daemon**
A server process that listens for incoming remote requests.

**Remote Method Invocation (RMI)**
Calling a method on an object located on another machine or process.

### Server Program (pyro_server.py)
The server creates a remote object and waits for client requests.

*Importing Module*
import Pyro4
- Imports the Pyro4 framework.

*Creating the Server Class*
class Server(object):
- Defines a class whose methods can be accessed remotely.

@Pyro4.expose
def welcomeMessage(self, name):
- Makes the method available to remote clients.

return ("Hi welcome " + str(name))
- Returns a greeting message.
- Example:
    Hi welcome Javaria

*Creating a Pyro Daemon*
daemon = Pyro4.Daemon()
- Creates a Pyro server daemon.
- Responsible for receiving remote requests.

*Locating Name Server*
ns = Pyro4.locateNS()
- Connects to the Pyro Name Server.
- Used for service discovery.

*Registering the Object*
uri = daemon.register(server)
- Registers the server object.
- Generates a unique URI.

*Registering a Name*
ns.register("server", uri)
- Associates the name `"server"` with the object's URI.

*Starting Request Loop*
daemon.requestLoop()
- Keeps the server running.
- Waits for incoming client requests.

### Client Program (pyro_client.py)
The client connects to the remote server and invokes a method.

*Getting User Input*
name = input("What is your name? ")
- Takes user's name as input.

*Connecting to Server*
server = Pyro4.Proxy("PYRONAME:server")
- Creates a proxy object.
- Connects to the remote server using the registered name.

*Calling Remote Method*
print(server.welcomeMessage(name))
- Executes a method on the remote server.
- Receives and prints the returned result.

### Program Flow
- Client
- Name Server Lookup
- Locate Server URI
- Connect to Server
- Call welcomeMessage()
- Server Executes Method
- Result Returned to Client

### Program Execution
*Start Pyro Name Server*
pyro4-ns

*Start Server*
python server.py

*Step 3: Start Client*
python client.py

### Example Output
Client Input:
What is your name?
Javaria

Output:
Hi welcome Javaria

### Advantages
- Simple remote communication
- Object-oriented approach
- Easy service discovery using Name Server
- Supports distributed applications

### Limitations
- Requires Pyro Name Server
- Additional network overhead
- Less suitable for very large-scale distributed systems

**************************************************************************************************

## Socket Client-Server 
This example demonstrates socket programming in Python using the TCP protocol.

### Important Concepts
**Socket**
An endpoint used for communication between two devices.

**TCP (Transmission Control Protocol)**
A reliable communication protocol that guarantees data delivery.

**Server**
A program that provides services to clients.

**Client**
A program that requests services from a server.

**Port**
A logical communication endpoint used by network applications.

> Two separate client-server applications are implemented:
    1. Time Server and Time Client
    2. File Transfer Server and File Transfer Client

### Part 1: Time Server and Client (client.py, server.py)
This application allows a client to connect to a server and receive the current system time.

**Server**
*Creating Socket*
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
- `AF_INET` > IPv4 addressing
- `SOCK_STREAM` > TCP protocol

*Binding Server*
serversocket.bind((host, port))
- Associates the server with a specific host and port.
- Port used: 9999

*Listening for Connections*
serversocket.listen(5)
- Server waits for incoming client requests.
- Queue size is 5.

*Accepting Client Connection*
clientsocket, addr = serversocket.accept()
- Establishes connection with a client.
- Returns client socket and address.

*Sending Current Time*
currentTime = time.ctime(time.time())
clientsocket.send(currentTime.encode('ascii'))
- Retrieves current system time.
- Sends it to the client.

**Client**
*Creating Socket*
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
- Creates a TCP client socket.

*Connecting to Server*
s.connect((host, port))
- Connects to the Time Server on port 9999.

*Receiving Data*
tm = s.recv(1024)
- Receives time sent by server.

#### Output Example
Connected with ('127.0.0.1', 54000)

Time connection server:
Mon Jun 23 10:15:40 2025

### Part 2: File Transfer Server and Client (client2.py, server2.py)
This application transfers a file from server to client.

**Server**
*Creating Socket*
s = socket.socket()
- Creates TCP server socket.

*Binding Port*
s.bind((host, 60000))
- Server listens on port 60000.

*Waiting for Client*
s.listen(15)
- Waits for incoming connections.

*Accepting Connection*
conn, addr = s.accept()
- Establishes connection with client.

*Receiving Request*
data = conn.recv(1024)
- Receives message from client.

#*Opening File*
f = open('mytext.txt', 'rb')
- Opens file in binary mode.

*Sending File Data*
conn.send(l)
- Sends file contents in chunks.

*Closing Connection*
conn.close()
- Terminates connection after transfer.

**Client**
*Connecting to Server*
s.connect((host, port))
- Connects to File Server on port 60000.

*Sending Request*
s.send('HelloServer!'.encode())
- Sends request message to server.

*Creating Output File*
with open('received.txt', 'wb') as f:
- Creates destination file.

*Receiving Data*
data = s.recv(1024)
- Receives file contents from server.

*Saving File*
f.write(data)
- Writes received data into `received.txt`.

#### Output Example
Server:
Server listening...
Got connection from ('127.0.0.1', 54001)
Server received HelloServer!
Sent data
Done sending

Client:
file opened
receiving data...
Successfully get the file
connection closed

### Difference Between the Two Applications

#### Time Server Example
- Sends current system time
- Small text message transfer
- Demonstrates basic socket communication

#### File Transfer Example
- Transfers an entire file
- Uses repeated send/receive operations
- Demonstrates practical data transmission

### Program Flow
#### Time Service
- Client
- Connect to Server
- Request Time
- Server Sends Time
- Client Displays Time

#### File Transfer Service
- Client
- Connect to Server
- Send Request
- Server Opens File
- Server Sends File Data
- Client Saves File

### Advantages
- Simple network communication
- Reliable data transfer using TCP
- Supports file sharing and messaging
- Foundation of distributed systems

### Limitations
- Requires active network connection
- Manual connection management
- Server must remain running to serve clients

**************************************************************************************************