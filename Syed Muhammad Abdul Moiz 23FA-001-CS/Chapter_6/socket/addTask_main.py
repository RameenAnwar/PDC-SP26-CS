# Import the 'add' task function directly from our previous 'addTask' module
from addTask import add

# Standard execution guard ensuring this block only runs when this script is executed directly
if __name__ == '__main__':
    # Trigger the 'add' task asynchronously using the '.delay()' method
    # Instead of calculating 5 + 5 locally, it packages the arguments (5, 5) into a message 
    # and pushes it to the message broker (RabbitMQ/AMQP) for a background Celery worker to handle
    add.delay(5, 5)