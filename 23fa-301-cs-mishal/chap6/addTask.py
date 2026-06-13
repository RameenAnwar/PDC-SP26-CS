# Import the Celery class from the celery module
# Celery is the main tool for creating distributed task queues
from celery import Celery

# Create a Celery application instance
# 'addTask' is the name of the module (used for task discovery)
# broker='amqp://guest@localhost//' specifies the message broker (RabbitMQ)
# amqp is the protocol, guest is the default username/password
# localhost is the broker address, // is the virtual host (default)
app = Celery('addTask', broker='amqp://guest@localhost//')

# Decorate the add function with @app.task to make it a Celery task
# This tells Celery that this function can be called asynchronously
# via .delay() or .apply_async()
@app.task
def add(x, y):
    # Task body: simply return the sum of two numbers
    # This will be executed by a Celery worker process
    return x + y