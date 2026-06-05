
# This file SENDS tasks to the Celery worker

from addTask import add

# Not when another file imports it
if __name__ == '__main__':
    

    # .delay() puts task in broker queue
    # Worker will do: add(5, 5) = 10
    # This line returns immediately with a task ID
    result = add.delay(5, 5)
    
    # Each task gets a special ID like "abc-123-def"
    print(f"Task ID: {result.id}")
    
    # .get() WAITS for worker to finish
    # timeout=10 means wait max 10 seconds
    # Then prints: 5 + 5 = 10
    print(f"5 + 5 = {result.get(timeout=10)}")
    
#output:
# Celery app created successfully!
# 8