# Celery Task Creation

# Description
This code demonstrates how to create a simple Celery task that performs addition asynchronously.

## What This Code Does
- Creates a Celery application  
- Connects to RabbitMQ using a broker URL  
- Defines a task named `add()`  
- Accepts two numbers as input  
- Returns the sum of the numbers  

## Execution Flow
1. Import `Celery`  
2. Create Celery application instance  
3. Connect to RabbitMQ broker  
4. Define task using `@app.task` decorator  
5. Task waits for execution requests  
6. Worker executes task when called  

## How to Execute
1. Install Celery:
   ```bash
   pip install celery
   ```

2. Install and start RabbitMQ

3. Start Celery worker:
   ```bash
   celery -A addTask worker --loglevel=info
   ```

4. Run task from another Python file:
   ```python
   import addTask
   result = addTask.add.delay(5, 5)
   ```

## End Use
Used for:
- Background processing  
- Distributed task execution  
- Asynchronous operations  

## When to Use
Use when:
- Tasks take time to execute  
- Background processing is needed  
- Workload should be distributed  

Avoid when:
- Immediate results are required  
- Simple synchronous execution is enough  

## How to Use
1. Create Celery app  
2. Configure broker connection  
3. Define task with `@app.task`  
4. Start worker process  
5. Call task using `.delay()` or `.apply_async()`  

## Advantages
- Asynchronous task execution  
- Scalable architecture  
- Supports distributed workers  

## Disadvantages
- Requires RabbitMQ or Redis  
- Additional setup and configuration  
- More complex than normal functions  

## One-Line Summary
This code creates a Celery task that adds two numbers and can be executed asynchronously by a worker.


# Celery Task Execution

## Description
This code demonstrates how to execute a Celery task asynchronously using `.delay()`.

## What This Code Does
- Imports a Celery task from `addTask.py`  
- Calls the task asynchronously using `delay()`  
- Passes two numbers as arguments (`5` and `5`)  
- Returns a task result object immediately without waiting for execution  

## Execution Flow
1. Import `addTask` module  
2. Call `add.delay(5, 5)`  
3. Celery sends task to the message broker  
4. Worker receives and executes task  
5. Result is stored in the backend  
6. Main program continues without waiting  

## How to Execute
1. Start Redis/RabbitMQ broker  
2. Start Celery worker:
   ```bash
   celery -A addTask worker --loglevel=info
   ```
3. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Background task processing  
- Distributed task execution  
- Asynchronous workloads  

## When to Use
Use when:
- Tasks take a long time to complete  
- Work should run in the background  
- Distributed processing is needed  

Avoid when:
- Immediate results are required  
- Tasks are very small and simple  

## How to Use
1. Define a Celery task  
2. Start a message broker  
3. Start Celery worker  
4. Call task using `.delay()`  
5. Retrieve result if needed  

## Advantages
- Asynchronous execution  
- Scalable and distributed  
- Improves application responsiveness  

## Disadvantages
- Requires broker setup  
- More complex architecture  
- Additional system resources needed  

## One-Line Summary
This program sends a Celery task to execute asynchronously in the background.

