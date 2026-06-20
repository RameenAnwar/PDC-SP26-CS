Celery Simple Add Task Example:
This repository contains a minimal "Hello World" style example demonstrating how to define and execute asynchronous background tasks using Python, Celery, and a RabbitMQ message broker.

Prerequisites:
To run this code, you need Python installed along with the Celery package. You also need a RabbitMQ server running locally to act as the message broker.

1. Install Python Dependencies:

bash
pip install celery

2. Install and Start RabbitMQ:
* Linux (Ubuntu/Debian): `sudo apt-get install rabbitmq-server` and `sudo systemctl start rabbitmq-server`
* Windows: Download the installer from the official RabbitMQ website.

How to Run:
Because this is a distributed task queue, you need to run the worker process and the execution script in two separate terminal windows.
Step 1: Start the Celery Worker
Open your terminal in the directory containing `addTask.py` and run the following command to start listening for tasks:
bash
celery -A addTask worker --loglevel=info

Step 2: Execute the Task:
Open a second terminal window in the same directory and run your execution script:
bash
python run_task.py
(Assuming you saved the second snippet as `run_task.py`)

What it Does:
This example is split into two distinct parts: defining the task and calling the task.

1. The Task Definition (`addTask.py`)
* Initialization: app = Celery('addTask', broker='amqp://guest@localhost//') initializes the Celery application and connects it to the local RabbitMQ message broker using the default guest credentials.
* The Decorator: The @app.task decorator tells Celery that the `add(x, y)` function is a background task that should be registered into the task queue rather than executed normally.

2. The Execution Script
* Asynchronous Call: Calling `addTask.add.delay(5, 5)` is the standard way to send a task to the queue in Celery.
* Non-Blocking: The `.delay()` method pushes the instruction (add 5 and 5) to the RabbitMQ broker and immediately returns execution back to your script without waiting for the math to actually finish. The Celery worker picks up the message from the broker and computes the result in the background.

Expected Output:
In your execution terminal, the script will finish almost instantly and silently since you are assigning the result to a variable but not printing it.
In your Celery worker terminal, you will see logs indicating that the task was received and successfully executed:

[INFO/MainProcess] Task addTask.add[<task-uuid>] received
[INFO/MainProcess] Task addTask.add[<task-uuid>] succeeded in 0.001s: 10
