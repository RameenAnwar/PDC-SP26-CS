# Bring Celery library into our code
from celery import Celery

# Make a Celery app
# 'addTask' = name of our app
# broker='memory://' = place where tasks wait 
# backend='rpc://' = place where answers are kept
app = Celery('addTask', 
             broker='memory://',
             backend='rpc://')

# This turns a normal function into a Celery task
@app.task
def add(x, y):
    # Simple addition - add two numbers
    return x + y

# Show message that app is ready
print("Celery app created successfully!")

# output:
# :\Users\LAPTOP LAB\...\Celery>python -m celery -A addTask worker --loglevel=info --pool=solo

# Celery app created successfully!

#  -------------- celery@DESKTOP-7OAL6MQ v5.6.3 (recovery)
# --- ***** ----- 
# -- ******* ---- Windows-11-10.0.22631-SP0 2026-06-05 19:54:02
# - *** --- * --- 
# - ** ---------- [config]
# - ** ---------- .> app:         addTask:0x2608e103230
# - ** ---------- .> transport:   memory://localhost//
# - ** ---------- .> results:     rpc://
# - *** --- * --- .> concurrency: 12 (solo)
# -- ******* ---- .> task events: OFF
# --- ***** ----- 
#  -------------- [queues]
#                 .> celery           exchange=celery(direct) key=celery

# [tasks]
#   . addTask.add

# [2026-06-05 19:54:02,492: INFO/MainProcess] Connected to memory://localhost//
# [2026-06-05 19:54:02,495: INFO/MainProcess] celery@DESKTOP-7OAL6MQ ready.

# [2026-06-05 19:55:10,123: INFO/MainProcess] Task addTask.add[abc-123-def-456] received
# [2026-06-05 19:55:10,125: INFO/ForkPoolWorker-8] Task addTask.add[abc-123-def-456] succeeded in 0.000456s: 8
