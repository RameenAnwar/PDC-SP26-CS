# addTask_main.py  --  Chapter 6: Distributed Python (Celery client)
# Calls the add task ASYNCHRONOUSLY with .delay(5, 5). The work is sent to the
# Celery worker through the broker; the result is fetched from the result backend.
# RUN:  python addTask_main.py   (worker must already be running)
#
# ----------------------- CODE (commented out) -----------------------
# import addTask
# if __name__ == '__main__':
#     result = addTask.add.delay(5, 5)   # .delay() = run the task on a worker, non-blocking
#     # print(result.get())              # .get() would wait for and return 10
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (on the WORKER side, the task is received and executed)
# [INFO] Received task: addTask.add[<task-id>]
# [INFO] Task addTask.add[<task-id>] succeeded in 0.0007s: 10
# (result.get() on the client side would return:  10)
# --------------------------------------------------------------------
