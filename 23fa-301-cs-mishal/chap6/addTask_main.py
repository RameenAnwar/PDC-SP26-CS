# Import the addTask module which contains the Celery app and task definition
import addTask

# This block runs when the script is executed directly
if __name__ == '__main__':
    # Call the 'add' task asynchronously using .delay()
    # .delay() sends the task to the Celery worker (RabbitMQ broker)
    # The arguments 5 and 5 are passed to the add() function
    result = addTask.add.delay(5, 5)
    
    # 'result' is an AsyncResult object that can be used to check status,
    # get the result later, or wait for completion.