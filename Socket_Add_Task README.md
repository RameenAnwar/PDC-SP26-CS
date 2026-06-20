Celery Asynchronous Task Example:
This repository contains a minimal example demonstrating how to define and execute asynchronous background tasks using Python, Celery, and a RabbitMQ message broker.

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
Note: Ensure your first script is saved exactly as `addTask.py`, as the execution script imports from it

Step 1: Start the Celery Worker
Open your terminal in the directory containing `addTask.py` and run the following command to start listening for tasks:
bash
celery -A addTask worker --loglevel=info

Step 2: Execute the Task
Open a second terminal window in the same directory and run your execution script:
bash
python run_task.py

(Assuming you saved the second snippet as `run_task.py`)

What it Does:
This codebase is split into two distinct parts:

1. The Task Definition (`addTask.py`):
* Initialization: `app = Celery('tasks', broker='pyamqp://guest@localhost//')` initializes the Celery application and connects it to the local RabbitMQ message broker using the `pyamqp` protocol.
* The Decorator: The `@app.task` decorator tells Celery that the `add(x, y)` function should be registered as a background task in the queue, rather than running as a standard synchronous function.

2. The Execution Script (`run_task.py`)
* Asynchronous Call: Calling `add.delay(5, 5)` is the standard method to push a task to the Celery queue.
* Non-Blocking Execution: The `.delay()` method sends the instruction (add 5 and 5) to the RabbitMQ broker and immediately finishes. It does not wait for the math to be calculated. The background Celery worker picks up the message from the broker and executes it independently.

Expected Output:
In your execution terminal, the script will finish almost instantly and silently.
In your Celery worker terminal, you will see logs indicating that the worker connected to the broker, received the task, and successfully executed it:
[INFO/MainProcess] Connected to pyamqp://guest:**@localhost:5672//
[INFO/MainProcess] celery@your-machine ready.
[INFO/MainProcess] Task addTask.add[<task-uuid>] received
[INFO/MainProcess] Task addTask.add[<task-uuid>] succeeded in 0.002s: 10

```
