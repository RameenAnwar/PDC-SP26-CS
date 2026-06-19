# Chapter 3 – Process-Based Parallelism in Python

## Student Information

**Name:** Uzair
**Roll Number:** 23FA-034-CS

---

## Overview

This chapter focuses on Python multiprocessing and demonstrates how processes can be created, managed, synchronized, and used for parallel execution. It also covers process communication techniques and process pools.

---

## Naming Processes (naming_processes.py)

### Learning Outcome

Learned how to assign and identify process names.

### Execution

```bash
python naming_processes.py
```

### Use Case

Useful for debugging and monitoring processes.

### Summary

Demonstrates process naming functionality.

### Pros

* Easy process identification

### Cons

* No direct performance gain

---

## Spawning Processes (spawning_processes.py)

### Learning Outcome

Learned how to create and launch multiple processes.

### Execution

```bash
python spawning_processes.py
```

### Use Case

Useful for running independent tasks simultaneously.

### Summary

Shows process creation and execution.

### Pros

* True parallel execution

### Cons

* Higher resource usage

---

## Spawning Processes with Namespace (spawning_processes_namespace.py)

### Learning Outcome

Learned how processes can share custom namespace objects.

### Execution

```bash
python spawning_processes_namespace.py
```

### Use Case

Useful when sharing structured information among processes.

### Summary

Demonstrates namespace-based data sharing.

---

## Process Communication using Pipe (communicating_with_pipe.py)

### Learning Outcome

Learned inter-process communication using pipes.

### Execution

```bash
python communicating_with_pipe.py
```

### Use Case

Used when two processes need to exchange data.

### Summary

Demonstrates communication through pipes.

### Pros

* Fast communication

### Cons

* Limited scalability

---

## Process Communication using Queue (communicating_with_queue.py)

### Learning Outcome

Learned process communication using queues.

### Execution

```bash
python communicating_with_queue.py
```

### Use Case

Useful for producer-consumer systems.

### Summary

Shows queue-based communication.

### Pros

* Safe and scalable

### Cons

* Slight overhead

---

## Process Pool (process_pool.py)

### Learning Outcome

Learned efficient task execution using worker pools.

### Execution

```bash
python process_pool.py
```

### Use Case

Used for repetitive parallel tasks.

### Summary

Demonstrates worker process pools.

### Pros

* Better CPU utilization

### Cons

* Reduced process-level control

---

## Barrier Synchronization (processes_barrier.py)

### Learning Outcome

Learned process synchronization using barriers.

### Execution

```bash
python processes_barrier.py
```

### Use Case

Useful when processes must wait for each other.

### Summary

Demonstrates barrier synchronization.

---

## Running Background Processes (run_background_processes.py)

### Learning Outcome

Learned daemon process behavior.

### Execution

```bash
python run_background_processes.py
```

### Use Case

Background monitoring services.

### Summary

Shows daemon processes.

---

## Running Non-Daemon Processes (run_background_processes_no_daemons.py)

### Learning Outcome

Learned differences between daemon and non-daemon processes.

### Execution

```bash
python run_background_processes_no_daemons.py
```

### Summary

Shows persistent background processes.

---

## Killing Processes (killing_processes.py)

### Learning Outcome

Learned how to terminate running processes.

### Execution

```bash
python killing_processes.py
```

### Summary

Demonstrates process termination.

---

## Process in Subclass (process_in_subclass.py)

### Learning Outcome

Learned object-oriented multiprocessing.

### Execution

```bash
python process_in_subclass.py
```

### Summary

Extends the Process class through inheritance.

---

## Final Summary

This chapter introduced multiprocessing concepts including process creation, communication, synchronization, pools, and background execution.

---

## Conclusion

Through this chapter, I learned how Python multiprocessing enables true parallelism and improves performance for CPU-intensive tasks.
