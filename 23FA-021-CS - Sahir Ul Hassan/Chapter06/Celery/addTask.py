###
## addTask.py :Executing a simple task
###

from celery import Celery

app = Celery('addTask',broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

