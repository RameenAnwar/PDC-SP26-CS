# Import the main Celery class from the celery library to create our distributed task application
from celery import Celery

# Initialize the Celery application object named 'tasks'
# The 'broker' parameter sets up the message queue using the 'pyamqp' protocol (Python AMQP client)
# It tells Celery to connect to a server running locally ('localhost') using default 'guest' credentials
app = Celery('tasks', broker='pyamqp://guest@localhost//')

# This decorator transforms a normal Python function into a Celery distributed task
# It registers the function with the Celery app so it can be queued and executed by background worker processes
@app.task
def add(x, y):
    # Simply add the two numbers together and return the mathematical sum
    return x + y