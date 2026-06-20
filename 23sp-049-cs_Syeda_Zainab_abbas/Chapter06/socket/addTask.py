# addTask.py  --  Chapter 6: Celery task (socket-folder variant)
# Same idea as the Celery example: define an app + an add task, but using the
# pyamqp broker URL.
# RUN:  celery -A addTask worker --loglevel=info
#
# ----------------------- CODE (commented out) -----------------------
# from celery import Celery
# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# @app.task
# def add(x, y):
#     return x + y
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# [tasks]
#   . tasks.add
# [INFO] celery@localhost ready.
# --------------------------------------------------------------------
