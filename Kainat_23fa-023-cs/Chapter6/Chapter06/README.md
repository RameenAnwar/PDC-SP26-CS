## CELERY

This chapter demonstrates task execution using Celery, a distributed task queue system in Python.

The system is divided into two connected files:

1. addTask.py (Task Definition)
2. addTask_main.py (Task Execution / Client)

###  addTask.py 

This file defines a Celery application and creates a simple task called add().

A Celery instance is created using a message broker (RabbitMQ via AMQP).

The add() function is registered as a Celery task using the @app.task decorator.

This function takes two numbers and returns their sum.

###  addTask_main.py

This file imports the task module and sends a task request.

The add.delay(5,5) method sends the task to the Celery worker asynchronously.

Instead of executing immediately, the task is placed in the message queue and handled by a worker process.

Important concepts in this program:
- Distributed task queue (Celery)
- Asynchronous task execution
- Message broker (RabbitMQ / AMQP)
- Producer-consumer model
- Worker-based processing

Celery allows tasks to run asynchronously in the background using workers. The main program does not wait for execution; instead, it sends tasks to a queue, making it useful for scalable and distributed systems.


## Pyro4

### First Example

This chapter demonstrates Remote Method Invocation (RMI) using Pyro4 in Python.

The system is divided into two connected files:

1. pyro_server.py (Server)
2. pyro_client.py (Client)

### pyro_server.py

This file creates a remote server object using Pyro4.

A class named Server is defined with a method welcomeMessage(), which returns a greeting message.

The server is exposed using @Pyro4.expose so it can be accessed remotely.

A Pyro daemon is created to handle incoming remote requests.

The server object is registered with the Pyro Name Server using the name "server".

The daemon then starts an event loop to continuously listen for client requests.

###  pyro_client.py 

This file acts as a client that connects to the remote server.

The user enters their name as input.

The client creates a proxy object using Pyro4.Proxy("PYRONAME:server"), which connects to the server registered in the Name Server.

The client calls the remote method welcomeMessage(name), which executes on the server and returns a response.

Important concepts in this program:
- Remote Method Invocation (RMI)
- Client-server architecture
- Pyro4 distributed computing
- Name server registration
- Proxy-based remote communication

Pyro4 allows a program running on one machine to call methods on another machine as if they were local. This enables distributed computing by separating client and server logic over a network.

