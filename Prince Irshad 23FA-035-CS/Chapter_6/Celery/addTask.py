###
## addTask.py : Executing a simple task
###

# Import the main Celery class from the celery library to create our distributed task application
from celery import Celery

# Initialize the Celery application object named 'addTask'
# The 'broker' parameter sets up the message queue using the AMQP protocol (typically RabbitMQ)
# It tells Celery to connect to a server running locally ('localhost') using default 'guest' credentials
app = Celery('addTask', broker='amqps://tjkebacu:QhmVC8TAInbzptBddkqktLZBOOCQG8qj@fuji.lmq.cloudamqp.com/tjkebacu')

# This decorator transforms a normal Python function into a Celery distributed task
# It registers the function with the Celery app so it can be pushed into a queue and executed by worker processes
@app.task
def add(x, y):
    # Simply add the two numbers together and return the mathematical sum
    return x + y