# Process-Based Parallelism – Complete Study Notes

These notes explain **process-based parallelism in Python** in a clear and practical way. The focus is on understanding concepts deeply with **real-world examples, comparisons, and clean explanations**.

---

# Table of Contents

1. What is Process-Based Parallelism
2. Spawning a Process
3. Naming a Process
4. Background Processing (Daemon vs Non-Daemon)
5. Process Termination and Control
6. Subclassing a Process
7. Inter-Process Communication
   - Queue
   - Pipes
8. Process Synchronization
9. Process Pool
10. Process Pool Methods (Comparison)

---

# 1. What is Process-Based Parallelism?

Process-based parallelism is a way of running **multiple independent programs (processes) at the same time** so that a task finishes faster.

Unlike threads, each process has its **own memory space**, which means processes do not interfere with each other. This makes them more stable and safer, especially when handling heavy computations.

The main idea is simple: instead of doing one big task step-by-step, you **divide it into smaller parts** and run each part in a separate process. Since modern computers have multiple CPU cores, these processes can truly run in parallel.

### Real-world example

Think of editing a video:

- One process handles color correction
- Another handles audio
- Another renders frames

All of them run at the same time → faster output.

---

# 2. Spawning a Process

Spawning means **creating a new process (child)** from an existing process (parent).

In Python, this is done using the `multiprocessing.Process` class.

The parent process decides:

- Should it **continue working immediately** (asynchronous)?
- Or should it **wait for the child to finish** using `join()`?

### Key idea

- `start()` → begins execution
- `join()` → makes parent wait

If you don’t use `join()`, your program keeps moving without waiting.

### Real-world example

A manager assigns a task:

- If the manager keeps working → asynchronous
- If the manager waits for the result → join()

---

# 3. Naming a Process

When you have multiple processes running, things can get confusing very quickly. This is where naming becomes important.

Instead of default names like _Process-1_, _Process-2_, you can give meaningful names like:

- DataLoader
- ImageProcessor
- ResultSaver

This makes debugging and tracking much easier.

### Why it matters

- Helps identify which process caused an error
- Makes logs readable
- Improves overall code clarity

---

# 4. Background Processing (Daemon vs Non-Daemon)

Background processing means running tasks **without user interaction**, while the main program continues doing something else.

In Python, processes can be either **daemon** or **non-daemon**.

---

## Daemon vs Non-Daemon (Comparison)

| Feature               | Daemon Process | Non-Daemon Process |
| --------------------- | -------------- | ------------------ |
| Runs in background    | Yes            | Usually foreground |
| Ends when parent ends | Yes            | No                 |
| Independent           | No             | Yes                |
| Used for              | Support tasks  | Critical tasks     |

---

### Daemon Process

A daemon process runs silently in the background and automatically stops when the parent process exits.

**Example:** logging, monitoring, background cleanup

---

### Non-Daemon Process

A non-daemon process runs independently and must complete its work even if the parent stops.

**Example:** saving files, database updates

---

### Important note

Daemon processes **cannot create child processes**, because they are meant to be lightweight helpers.

---

# 5. Process Termination and Control

Sometimes processes don’t behave properly — they may hang, crash, or consume too many resources. That’s why we need ways to control and terminate them.

### Important methods

- `terminate()` → forcefully stop a process
- `is_alive()` → check if still running
- `join()` → wait until process fully ends

---

## Exit Code Meaning

| Exit Code | Meaning                 |
| --------- | ----------------------- |
| 0         | Success                 |
| > 0       | Error occurred          |
| < 0       | Killed by system signal |

---

### Real-world example

When an app freezes and you close it using Task Manager — that’s like calling `terminate()`.

---

# 6. Subclassing a Process

Instead of writing everything in one function, you can create your own **custom process class** by inheriting from `Process`.

The main logic is written inside the `run()` method.

When you start the process, Python automatically calls this `run()` method.

### Why use this?

- Cleaner structure
- Better organization
- Easy to reuse code

---

### Real-world example

In a company:

- All employees follow the same rules (parent class)
- Each has different roles (child classes)

---

# 7. Inter-Process Communication (IPC)

Since processes don’t share memory, they need special ways to communicate. This is called **IPC (Inter-Process Communication)**.

---

## 7.1 Queue

A Queue follows **FIFO (First-In, First-Out)** order.

### How it works

- Producer → adds data
- Queue → holds data
- Consumer → removes data

This solves the **producer-consumer problem** safely.

---

### Image Explanation (Queue)

The diagram shows:

- Items being continuously added by producer
- Stored in queue
- Removed by consumer one-by-one

This ensures no data is lost and order is maintained.

---

### Real-world example

A ticket line:

- First person in → first person served

---

## Queue vs Pipe

| Feature       | Queue              | Pipe               |
| ------------- | ------------------ | ------------------ |
| Communication | Multiple processes | Only two processes |
| Structure     | FIFO               | Direct connection  |
| Flexibility   | High               | Low                |
| Speed         | Slightly slower    | Faster             |

---

## 7.2 Pipes

A Pipe is a direct communication channel between two processes.

It returns two endpoints:

- One for sending
- One for receiving

---

### Types

- Unidirectional → one-way
- Bidirectional → two-way

---

### Real-world example

A phone call between two people.

---

# 8. Process Synchronization

When multiple processes try to access shared resources, problems can occur (like incorrect data). Synchronization prevents this.

---

## Synchronization Tools

| Tool      | Purpose                    |
| --------- | -------------------------- |
| Lock      | Only one process at a time |
| Event     | Signal between processes   |
| Condition | Wait for a condition       |
| Semaphore | Limit number of processes  |
| RLock     | Reusable lock              |
| Barrier   | Wait for all processes     |

---

### Real-world examples

- Lock → only one person uses ATM
- Semaphore → limited parking slots
- Barrier → team waits for everyone before starting

---

# 9. Process Pool

Creating processes again and again is expensive. A **process pool** solves this problem.

A pool creates a fixed number of worker processes and reuses them.

---

### How it works

1. Pool is created
2. Tasks are divided
3. Workers execute tasks
4. Results are collected

---

### Key idea

Same function runs on different data → **data parallelism**

---

### Real-world example

Factory workers:

- Tasks are distributed among workers
- Work happens faster

---

# 10. Process Pool Methods (Comparison)

---

## apply vs apply_async vs map vs map_async

| Method      | Blocking | Parallel | Best Use              |
| ----------- | -------- | -------- | --------------------- |
| apply       | Yes      | No       | Single task           |
| apply_async | No       | No       | Background execution  |
| map         | Yes      | Yes      | Multiple inputs       |
| map_async   | No       | Yes      | Parallel + background |

---

### Simple understanding

- `apply()` → do one job, wait
- `apply_async()` → do one job, don’t wait
- `map()` → many jobs, wait
- `map_async()` → many jobs, don’t wait

---

### Real-world analogy

- apply → one worker
- map → many workers
- async → work continues without waiting

---

# Final Summary

Process-based parallelism allows programs to run **multiple tasks at the same time using separate processes**. It improves performance, ensures stability, and is ideal for heavy computations.

To use it effectively, you must understand:

- how to create processes
- how they communicate (Queue, Pipe)
- how to control them (terminate, join)
- and how to scale using process pools

When used correctly, it helps build **fast, efficient, and scalable systems**.
