# addTask.py  --  Chapter 6: Distributed Python (Celery)
# Defines a Celery app and a simple task add(x, y). Celery runs tasks on separate
# WORKER processes/machines; a message broker (here RabbitMQ via amqp) passes the
# task to the worker.
# RUN:  1) start broker (RabbitMQ)   2) celery -A addTask worker --loglevel=info
#
# ----------------------- CODE (commented out) -----------------------
# from celery import Celery
# # 'addTask' = app name; broker = the message queue Celery talks to
# app = Celery('addTask', broker='amqp://guest@localhost//')
# @app.task                       # this decorator turns add() into a Celery task
# def add(x, y):
#     return x + y
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (when the worker starts it registers the task; sample worker log)
#  -------------- celery@localhost v... ready.
#  [tasks]
#    . addTask.add
# [INFO] Connected to amqp://guest@127.0.0.1:5672//
# [INFO] celery@localhost ready.
# --------------------------------------------------------------------
