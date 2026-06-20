# addTask_main.py  --  Chapter 6: Celery client (socket-folder variant)
# Submits add(5, 5) to the worker via .delay().
# RUN:  python addTask_main.py   (worker must be running)
#
# ----------------------- CODE (commented out) -----------------------
# from addTask import add
# if __name__ == '__main__':
#     add.delay(5, 5)        # send the task to a Celery worker (result would be 10)
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (worker log)
# [INFO] Received task: tasks.add[<task-id>]
# [INFO] Task tasks.add[<task-id>] succeeded in 0.0006s: 10
# --------------------------------------------------------------------
