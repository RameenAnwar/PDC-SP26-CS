# Parallel and Distributed Computing 
These notes cover how modern computer systems improve speed, efficiency, scalability, and performance by using multiple tasks, processors, threads, or machines together.

## Table of Contents

1. [Introduction](#1-introduction)
2. [What is Computing?](#2-what-is-computing)
3. [Parallel and Distributed Computing Together](#3-parallel-and-distributed-computing-together)
4. [Serial vs Parallel Computing](#4-serial-vs-parallel-computing)
5. [Fetch, Decode, Execute Cycle](#5-fetch-decode-execute-cycle)
6. [Parallelism in Fetch, Decode, Execute](#6-parallelism-in-fetch-decode-execute)
7. [Why We Need Parallel and Distributed Computing](#7-why-we-need-parallel-and-distributed-computing)
8. [Where It Is Used](#8-where-it-is-used)
9. [Multithreading vs Multiprocessing](#9-multithreading-vs-multiprocessing)
10. [Process vs Thread](#10-process-vs-thread)
11. [Types of Parallel Computing Systems](#11-types-of-parallel-computing-systems)
12. [Advantages of Parallel Computing](#12-advantages-of-parallel-computing)
13. [Distributed vs Parallel Computing](#13-distributed-vs-parallel-computing)
14. [Scale Up vs Scale Out](#14-scale-up-vs-scale-out)
15. [High Throughput vs High Performance Computing](#15-high-throughput-vs-high-performance-computing)
16. [MPI Library in Python](#16-mpi-library-in-python)
17. [Amdahl's Law](#17-amdahls-law)
18. [Gustafson's Law](#18-gustafsons-law)
19. [Flynn's Classification](#19-flynns-classification)
20. [Parallel Algorithm Key Concepts](#20-parallel-algorithm-key-concepts)
21. [Memory Organization](#21-memory-organization)
22. [Shared Memory Models](#22-shared-memory-models)
23. [Conclusion](#23-conclusion)

---

## 1. Introduction

In the early days, computers did one thing at a time. You gave them a task, they finished it, and only then moved to the next one. That worked fine for small problems — but today's world is very different.

Now we expect computers to:

- Handle huge amounts of data instantly
- Respond without delay
- Support millions of users at the same time
- Run many apps together
- Solve complex scientific problems

One processor working alone simply cannot keep up anymore. That is why we have **Parallel Computing** and **Distributed Computing** — two fields that teach us how to divide work, share the load, and get things done faster and more efficiently.

---

## 2. What is Computing?

**In simple words:** Computing means using a computer to do something useful — anything from adding two numbers to running a massive AI model.

### What falls under computing:

- Taking input from a user
- Storing and retrieving data
- Doing math and logic
- Running software and controlling devices
- Solving business or science problems
- Networking and communication
- Graphics, gaming, and artificial intelligence

### A simple example

When you open a calculator app and type `25 + 17`, that is computing. When you search something on Google, thousands of computing operations happen behind the scenes.

### Why computing matters

Without computing there would be no smartphones, no cloud storage, no online banking, no AI tools, no video games. It is the foundation of everything digital.

---

## 3. Parallel and Distributed Computing Together

This is a really important idea to understand clearly.

| Term | What it means |
|------|--------------|
| **Parallel Computing** | Take a big problem, cut it into smaller pieces, and work on all pieces **at the exact same time** using multiple processors or cores |
| **Distributed Computing** | Use **multiple separate computers** connected through a network to solve a problem together — each computer handles its own part |

### The big question they both answer

> *"How can we use many computing resources — whether inside one machine or across many machines — to get work done faster and handle bigger problems?"*

### Real-life analogy

Imagine you have 1 million exam papers to check:

- **Serial way** → One teacher checks all papers one by one
- **Parallel way** → Four teachers in the same room each check 250,000 papers at the same time
- **Distributed way** → Four teachers in four different cities each check 250,000 papers and coordinate with each other

---

## 4. Serial vs Parallel Computing

### What is serial computing?

Solving a problem step by step, one instruction at a time. Only one processor works and nothing overlaps.

### What is parallel computing?

Running different parts of the same program at the same time. This works when the work can be split into independent chunks.

### A concrete example

You want to add up 1000 numbers:

- **Serial way** → One processor adds all 1000 numbers one by one
- **Parallel way** → Processor 1 adds 1–250, Processor 2 adds 251–500, Processor 3 adds 501–750, Processor 4 adds 751–1000, then combine results

### Comparison

| Feature | Serial | Parallel |
|---------|--------|----------|
| Execution | One after another | All at once |
| Speed for big tasks | Slow | Fast |
| Processors used | Usually one | Multiple |
| Complexity | Simple | More complex |

### When to use which

- Use **serial** when the problem is small or tasks depend heavily on each other
- Use **parallel** when the task is large, speed matters, and data can be split

---

## 5. Fetch, Decode, Execute Cycle

Every CPU works on a simple repeating cycle:

| Step | What happens |
|------|-------------|
| **Fetch** | The CPU grabs the next instruction from memory |
| **Decode** | The CPU figures out what that instruction means |
| **Execute** | The CPU actually does the work |

Every single program you run is just millions of these cycles happening over and over again.

---

## 6. Parallelism in Fetch, Decode, Execute

Modern hardware applies parallelism at a very low level:

### 1. Pipelining (the assembly line)

While instruction 1 is being **executed**, instruction 2 is being **decoded**, and instruction 3 is being **fetched** — all at the same time.

### 2. Multiple cores

Modern CPUs have multiple cores. Each core has its own fetch-decode-execute unit running independently.

### 3. Superscalar execution

Some CPUs can execute multiple instructions in the same clock cycle if those instructions do not depend on each other.

### 4. SIMD (Single Instruction, Multiple Data)

One instruction works on many pieces of data at the same time.

> **Key takeaway:** Parallelism is not just about running multiple programs — it is built into the hardware at a very deep level.

---

## 7. Why We Need Parallel and Distributed Computing

The main reason is simple: modern problems have grown too big and too slow for one processor working alone.

| Reason | Explanation |
|--------|-------------|
| **Speed** | Self-driving cars, live video, online transactions all need instant results |
| **Huge data** | Machine learning datasets, social media traffic, big databases cannot fit in one machine |
| **Hardware waste** | Your phone and laptop already have multiple cores — use them |
| **Scalability** | As more users arrive, the system should handle them without slowing down |
| **Reliability** | If one machine fails in a distributed system, others keep working |
| **Cost efficiency** | Many regular computers are often cheaper than one super-powerful machine |

> **Bottom line:** Without parallel and distributed computing, modern technology would be painfully slow, incredibly expensive, or simply impossible.

---

## 8. Where It Is Used

| Field | How it is used |
|-------|---------------|
| **AI and Machine Learning** | Training ChatGPT and neural networks uses GPUs and distributed systems |
| **Scientific simulations** | Weather forecasting, climate models, drug discovery |
| **Big Data** | Hadoop and Spark process terabytes of data across clusters |
| **Cloud Computing** | AWS, Google Cloud, Azure are all built on distributed systems |
| **Search Engines** | Google processes billions of searches using distributed computing |
| **Banking and Finance** | Fraud detection, transaction processing, risk analysis |
| **Gaming and Graphics** | Your GPU has thousands of cores working in parallel |
| **Web and Social Media** | Millions using YouTube, Instagram, or Twitter at the same time |

---

## 9. Multithreading vs Multiprocessing

### What is multithreading?

One program (one process) has multiple **threads** inside it that can run at the same time. Threads are lightweight and share memory with each other.

### What is multiprocessing?

Running multiple **independent processes**. Each process has its own separate memory space.

### Comparison

| Aspect | Multithreading | Multiprocessing |
|--------|---------------|-----------------|
| What is it? | Multiple threads in one process | Multiple independent processes |
| Memory | Shared | Separate |
| Communication | Easy | Harder |
| Crash impact | One thread can crash the whole process | One crash does not affect others |
| Overhead | Low | High |

### Which one to use?

- Use **multithreading** for I/O-bound tasks (waiting for files or network)
- Use **multiprocessing** for CPU-heavy tasks (heavy calculations)

> **Special note for Python:** Due to the GIL (Global Interpreter Lock), multiprocessing is usually better for CPU-heavy work in Python.

---

## 10. Process vs Thread

### What is a process?

A program that is currently running. It has its own memory, resources, and address space.
- Examples: Chrome browser, calculator app

### What is a thread?

The smallest unit of execution inside a process. One process can have many threads that share memory.
- Example: In a music app, one thread plays audio while another updates the UI

### The house analogy

- A **process** is a house — its own address, its own rooms, its own stuff
- A **thread** is a person living in that house — they share things easily, but one person's fire burns the whole house

### Comparison

| Feature | Process | Thread |
|---------|---------|--------|
| Memory | Separate | Shared |
| Creation cost | Expensive | Cheap |
| Communication | Hard | Easy |
| Isolation | Strong | Weak |

---

## 11. Types of Parallel Computing Systems

| Type | Focus | Example |
|------|-------|---------|
| **Bit-level parallelism** | How many bits the processor handles at once | 64-bit CPU handles 64 bits per operation |
| **Instruction-level (ILP)** | CPU runs multiple instructions at once within a single core | Pipelining |
| **Task-level (TLP)** | Different threads or processes run different tasks at the same time | Browser with many open tabs |

---

## 12. Advantages of Parallel Computing

1. **Faster execution** — A task that takes a year can become a one-day task
2. **Better CPU utilization** — Keep all cores busy instead of wasting hardware
3. **Solve bigger problems** — Weather simulations, genome assembly, large AI models
4. **Real-time responsiveness** — Self-driving cars need instant decisions
5. **Scalability** — Systems can grow to handle more work as needed

> **A word of caution:** Parallel computing is not automatically better. It can introduce synchronization bugs, race conditions, and harder debugging. Use it only when the benefits outweigh the costs.

---

## 13. Distributed vs Parallel Computing

| Feature | Parallel Computing | Distributed Computing |
|---------|-------------------|----------------------|
| Hardware | One machine or tightly coupled systems | Multiple separate computers |
| Memory | Often shared | Each machine has its own memory |
| Communication speed | Very fast | Slower due to network latency |
| Fault tolerance | Lower | Higher |
| Scalability | Good | Almost unlimited |

### The analogy

- **Parallel** = many workers in one room
- **Distributed** = many workers in different buildings connected by phone

---

## 14. Scale Up vs Scale Out

| Term | Meaning |
|------|---------|
| **Scale Up (Vertical Scaling)** | Make your existing machine more powerful — add more RAM, faster CPU, bigger SSD |
| **Scale Out (Horizontal Scaling)** | Add more machines to your system — more servers, more computers |

### Comparison

| Feature | Scale Up | Scale Out |
|---------|----------|-----------|
| Simplicity | Simpler | More complex |
| Scalability | Limited | Almost unlimited |
| Fault tolerance | Lower | Higher |
| Cost | Expensive at large scale | Cheaper per unit |

### When to choose which

- **Scale up** when your system is small and simplicity matters
- **Scale out** when you expect growth or need fault tolerance

---

## 15. High Throughput vs High Performance Computing

| Aspect | High Throughput Computing (HTC) | High Performance Computing (HPC) |
|--------|--------------------------------|----------------------------------|
| Goal | Complete a large number of tasks over time | Solve one very large problem as fast as possible |
| Metric | Jobs per day | FLOPS, speed |
| Example | Rendering 10,000 animation frames | Weather forecasting simulation |
| Analogy | A bus — not the fastest, but moves many people | A Formula 1 car — incredibly fast, but for one specific thing |

---

## 16. MPI Library in Python

### What is MPI?

**MPI (Message Passing Interface)** is a standard that lets programs running on different computers communicate with each other.

### Why do we need it?

When processes run on different machines, they do not share memory. MPI gives them a way to send and receive data.

### Key concepts

| Concept | What it means |
|---------|--------------|
| **Rank** | Each process gets a unique ID number |
| **Size** | Total number of processes running |
| **Send / Receive** | Explicit message passing between processes |

### Simple example

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    comm.send("Hello", dest=1)
else:
    msg = comm.recv(source=0)
    print(msg)
```

### When to use MPI

Use MPI when your problem is too big for one computer and you need multiple machines working together — especially for distributed-memory systems, clusters, and scientific computing.

---

## 17. Amdahl's Law

### What it says

No matter how many processors you add, the **sequential (non-parallelizable) part** of your program limits your total speedup.

### The formula

```
Speedup = 1 / ((1 - P) + (P / N))
```

Where:
- `P` = fraction of the program that can be parallelized
- `N` = number of processors

### Example

If 80% of your code can be parallelized and 20% must run sequentially, with 4 processors:

```
Speedup = 1 / (0.2 + 0.8/4)
        = 1 / (0.2 + 0.2)
        = 1 / 0.4
        = 2.5x   (not 4x as you might expect)
```

### Why this matters

Optimize the sequential parts of your code first. No amount of parallel power can fix a slow sequential bottleneck.

---

## 18. Gustafson's Law

### What it says

When we increase the number of processors, we usually increase the problem size too. If we do that, we can achieve almost linear speedup.

### The formula

```
Speedup = N - α(N - 1)
```

Where:
- `N` = number of processors
- `α` = sequential fraction of the program

### Amdahl vs Gustafson

| Aspect | Amdahl's Law | Gustafson's Law |
|--------|-------------|-----------------|
| Assumption | Fixed problem size | Problem size grows with processors |
| View | Pessimistic | Optimistic |
| Use case | When the problem is fixed | When you scale the problem too |

> Both laws are correct — they just describe different scenarios. Use Amdahl when the problem is fixed. Use Gustafson when you are scaling both the hardware and the problem.

---

## 19. Flynn's Classification

Flynn's Classification organizes computer architectures based on how they handle **instructions** and **data**.

| Type | Full name | How it works | Example |
|------|-----------|--------------|---------|
| **SISD** | Single Instruction, Single Data | One instruction, one piece of data | Basic calculator, traditional serial computer |
| **SIMD** | Single Instruction, Multiple Data | One instruction works on many data items at once | GPU, array processing |
| **MISD** | Multiple Instruction, Single Data | Many instructions work on the same data | Fault-tolerant systems (rare) |
| **MIMD** | Multiple Instruction, Multiple Data | Many instructions work on many data items | Modern multi-core CPUs running multiple apps |

> **Most modern computers are MIMD.** GPUs use SIMD heavily for graphics and AI.

---

## 20. Parallel Algorithm Key Concepts

### Task decomposition

Breaking a big problem into smaller pieces that can run at the same time (concurrently).

### Synchronization

Coordinating tasks that share data. Common tools include:
- **Locks** — only one thread accesses shared data at a time
- **Semaphores** — controls access to a limited resource
- **Barriers** — all threads must reach this point before any can continue

### Communication

How processors exchange data:
- In **shared memory** → through variables
- In **distributed memory** → through messages

### Load balancing

Distributing work fairly across all processors. No processor should be overloaded while another sits idle — that wastes resources and slows everything down.

### Granularity

How big or small your parallel tasks are:

| Type | Description | Trade-off |
|------|-------------|-----------|
| **Fine-grained** | Many small tasks | Better balance, but more overhead |
| **Coarse-grained** | Fewer large tasks | Less overhead, but potentially worse balance |

---

## 21. Memory Organization

### Shared Memory

All processors access the same memory space.

- **Good:** Easy to program, fast communication
- **Bad:** Synchronization needed, does not scale well
- **Example:** Threads inside a single process

### Distributed Memory

Each processor has its own private memory.

- **Good:** Scales very well, no memory contention
- **Bad:** Harder to program, communication adds overhead
- **Example:** A cluster of computers

### Comparison

| Feature | Shared Memory | Distributed Memory |
|---------|--------------|-------------------|
| Communication | Direct through variables | Message passing |
| Programming | Easier | Harder |
| Scalability | Limited | Almost unlimited |
| Contention | Can be a problem | Not an issue |

---

## 22. Shared Memory Models

| Model | What it means | Key property |
|-------|--------------|--------------|
| **UMA** (Uniform Memory Access) | Every processor takes the same time to access any memory | Simple but does not scale well |
| **NUMA** (Non-Uniform Memory Access) | Processors access local memory faster than remote memory | Scales better, but performance depends on data placement |
| **NORMA** (No Remote Memory Access) | No shared memory at all — each processor has private memory, communication only through messages | Used in clusters |
| **COMA** (Cache Only Memory Architecture) | Memory behaves like a big cache — data moves to where it is used | Used in advanced high-performance systems |

---

## 23. Conclusion

Parallel and Distributed Computing is not just an academic topic. It is the reason modern technology works the way it does.

### Why we need these techniques

- Problems have grown too large for a single processor
- Performance demands are higher than ever before
- One machine alone simply cannot keep up

### What studying this teaches us

- How to use multiple cores and processors effectively
- How to design systems that scale to millions of users
- How to write code that runs faster by doing many things at once
- How to build reliable systems that keep working even when parts fail

### Where these concepts are essential

- Artificial Intelligence and Machine Learning
- Cloud Computing and Web Services
- Scientific Simulations
- Big Data Processing
- Graphics and Gaming

---

