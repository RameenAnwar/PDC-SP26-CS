###
# addTask.py : RUN the AddTask example with Celery
###

# Import our previous 'addTask' module/file to access the Celery app instance and registered tasks
import addTask

# Standard execution guard ensuring this block only runs when this script is executed directly
if __name__ == '__main__':
    # Trigger the 'add' function asynchronously using the '.delay()' method
    # Instead of executing locally, this packages the arguments (5, 5) into a message and sends it to the message broker (RabbitMQ)
    # A background Celery worker process will pick up this message from the queue and perform the actual math
    result = addTask.add.delay(5, 5)