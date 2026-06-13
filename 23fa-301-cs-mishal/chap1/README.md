# Parallel and Distributed Computing – Detailed Study Notes

This file contains my detailed study notes on **Parallel and Distributed Computing**.  
The purpose of these notes is to understand **how modern computer systems improve speed, efficiency, scalability, and performance** by using multiple tasks, processors, threads, or machines together.

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [What is Computing?](#2-what-is-computing)
3. [What is Parallel and Distributed Computing Together?](#3-what-is-parallel-and-distributed-computing-together)
4. [Serial Computing vs Parallel Computing](#4-serial-computing-vs-parallel-computing)
5. [Fetch, Decode, Execute Cycle](#5-fetch-decode-execute-cycle)
6. [How Fetch, Decode, Execute Can Be Done in Parallel](#6-how-fetch-decode-execute-can-be-done-in-parallel)
7. [Why Parallel and Distributed Computing is Needed](#7-why-parallel-and-distributed-computing-is-needed)
8. [Where Parallel and Distributed Computing is Used](#8-where-parallel-and-distributed-computing-is-used)
9. [Multithreading vs Multiprocessing](#9-multithreading-vs-multiprocessing)
10. [Process vs Thread](#10-process-vs-thread)
11. [Parallel Computing System Types](#11-parallel-computing-system-types)
12. [Advantages of Parallel Computing](#12-advantages-of-parallel-computing)
13. [Distributed Computing vs Parallel Computing](#13-distributed-computing-vs-parallel-computing)
14. [Scale Up vs Scale Out](#14-scale-up-vs-scale-out)
15. [High Throughput Computing vs High Performance Computing](#15-high-throughput-computing-vs-high-performance-computing)
16. [MPI Library in Python](#16-mpi-library-in-python)
17. [Amdahl’s Law](#17-amdahls-law)
18. [Gustafson’s Law](#18-gustafsons-law)
19. [Flynn’s Classification](#19-flynns-classification)
20. [Parallel Algorithm Key Concepts](#20-parallel-algorithm-key-concepts)
21. [Memory Organization](#21-memory-organization)
22. [Shared Memory Models](#22-shared-memory-models)
23. [Conclusion](#23-conclusion)

---

# 1. Introduction

In the early days of computing, most programs were executed **one instruction at a time** and **one task at a time**.  
This worked well for small problems, but as technology grew, the size and complexity of tasks also increased.

Today, computers are expected to:

- process huge amounts of data,
- respond quickly,
- support many users at once,
- run multiple applications simultaneously,
- and solve very large scientific or industrial problems.

Because of this, **single-processor serial execution is often not enough**.

To overcome this limitation, computer scientists use:

- **Parallel Computing**
- **Distributed Computing**

These fields help systems **divide work**, **share load**, and **finish tasks faster and more efficiently**.

---

# 2. What is Computing?

## Definition

**Computing** is the process of using a computer system to **perform operations on data**, **solve problems**, and **execute instructions**.

In simple words:

> Computing means using hardware and software to process information and do useful work.

---

## What Computing May Include

Computing is a broad term and may include many activities, such as:

- receiving input from the user,
- storing and retrieving data,
- performing arithmetic and logical operations,
- running software applications,
- controlling devices,
- solving scientific and business problems,
- networking and communication,
- automation,
- graphics and multimedia processing,
- artificial intelligence and machine learning.

---

## Example of Computing

When you open a calculator app and perform `25 + 17`, the system is doing computing.

When you search something on the internet, thousands of computing operations happen in the background:

- searching databases,
- ranking results,
- loading web pages,
- and displaying content.

So computing can be **small and simple** or **large and highly complex**.

---

## Importance of Computing

Computing is important because it is the **foundation of all digital systems**.

Without computing, we would not have:

- smartphones,
- cloud services,
- online banking,
- AI tools,
- simulations,
- social media,
- or automation systems.

---

# 3. What is Parallel and Distributed Computing Together?

This is one of the most important concepts in the subject.

---

## Parallel Computing

**Parallel Computing** means:

> Breaking a problem into smaller parts and executing those parts **at the same time** using multiple processing units.

These processing units may be:

- multiple CPU cores,
- multiple processors,
- GPUs,
- or specialized hardware.

---

## Distributed Computing

**Distributed Computing** means:

> Solving a problem by using **multiple separate computers** connected through a network.

Each computer handles a part of the work and may communicate with others.

---

## What They Mean Together

When we say **Parallel and Distributed Computing together**, we mean:

> Using multiple computational resources, whether inside one machine or across many machines, to perform work more efficiently.

This usually involves:

- dividing tasks,
- running many operations simultaneously,
- sharing workload,
- improving speed,
- improving scalability,
- and handling large systems.

---

## Main Shared Goal

Both fields try to answer one question:

> “How can we make computing faster, larger, and more efficient than a single sequential processor?”

That is why they are often studied together.

---

## Easy Example

Suppose you need to process **1 million student records**.

### Serial way:

One processor handles all records one by one.

### Parallel way:

4 processors each handle 250,000 records at the same time.

### Distributed way:

4 different computers each handle 250,000 records over a network.

So both approaches reduce total work time, but they do it in slightly different ways.

---

# 4. Serial Computing vs Parallel Computing

Understanding this comparison is extremely important because **parallel computing exists mainly to improve upon serial computing**.

---

## What is Serial Computing?

**Serial Computing** means:

> A problem is solved step by step, one instruction or one task at a time.

Only one processor or one execution path is used.

---

## How Serial Computing Works

Suppose a program has 4 tasks:

1. Read file
2. Process data
3. Calculate result
4. Save output

In serial computing:

- Task 1 finishes first,
- then Task 2 starts,
- then Task 3,
- then Task 4.

Nothing overlaps.

---

## Characteristics of Serial Computing

- Simple to design
- Easy to understand
- Easy to debug
- But slower for large problems

---

## What is Parallel Computing?

**Parallel Computing** means:

> Different parts of the same program or workload are executed simultaneously.

This is possible when the work can be divided into independent or semi-independent parts.

---

## Example of Parallel Computing

Suppose you want to sum an array of 1000 numbers.

### Serial:

One processor adds all 1000 numbers one by one.

### Parallel:

- Processor 1 sums 1–250
- Processor 2 sums 251–500
- Processor 3 sums 501–750
- Processor 4 sums 751–1000

Then the partial sums are combined.

This saves time.

---

## Detailed Comparison

| Feature         | Serial Computing       | Parallel Computing        |
| --------------- | ---------------------- | ------------------------- |
| Execution Style | One after another      | At the same time          |
| Speed           | Slower for large tasks | Faster for large tasks    |
| Processors Used | Usually one            | Multiple                  |
| Complexity      | Simpler                | More complex              |
| Efficiency      | Lower for heavy tasks  | Higher for suitable tasks |
| Scalability     | Limited                | Better                    |

---

## When Serial Computing is Preferred

Serial computing is still useful when:

- the problem is small,
- the program must follow a strict sequence,
- tasks depend heavily on each other,
- parallel overhead is not worth it.

### Example:

A simple calculator program may not need parallel execution.

---

## When Parallel Computing is Preferred

Parallel computing is preferred when:

- the task is large,
- time matters,
- data can be divided,
- performance is important.

### Example:

Image rendering, simulations, AI model training.

---

## Importance of This Difference

This comparison matters because **not every problem should automatically be parallelized**.

Sometimes parallelism gives huge benefits, and sometimes it adds unnecessary complexity.

So the main question is not:

> “Can we parallelize it?”

But rather:

> “Is parallelization useful and efficient for this problem?”

---

# 5. Fetch, Decode, Execute Cycle

Every CPU works using a very basic instruction cycle called the:

> **Fetch – Decode – Execute Cycle**

This is the fundamental process through which instructions are processed.

---

## Step 1: Fetch

The CPU **fetches** the next instruction from memory.

This means it reads the instruction that needs to be executed.

### Example:

Instruction in memory:

```text
ADD A, B
```

The CPU first fetches this instruction.

---

## Step 2: Decode

The CPU then **decodes** the instruction.

This means it interprets:

- what operation is required,
- what data is needed,
- where the result should go.

### Example:

`ADD A, B` means:

- add value of A and B

---

## Step 3: Execute

Now the CPU performs the actual action.

### Example:

If:

```text
A = 5
B = 3
```

Then:

```text
A + B = 8
```

This is the execute stage.

---

## Why This Cycle is Important

Every program you run is made up of instructions.

So whether it is:

- a game,
- a browser,
- a calculator,
- or an AI program,

the CPU is repeatedly doing:

1. Fetch
2. Decode
3. Execute

again and again.

---

# 6. How Fetch, Decode, Execute Can Be Done in Parallel

This is an important question because many students think:

> “If instructions are fetched, decoded, and executed in order, then how can parallelism happen?”

The answer is: **parallelism can happen at different levels**.

---

## 1. Pipelining

One of the simplest forms of instruction parallelism is **pipelining**.

Instead of waiting for one instruction to fully finish before starting the next, the CPU overlaps stages.

### Example:

| Time | Instruction 1 | Instruction 2 | Instruction 3 |
| ---- | ------------- | ------------- | ------------- |
| T1   | Fetch         |               |               |
| T2   | Decode        | Fetch         |               |
| T3   | Execute       | Decode        | Fetch         |
| T4   |               | Execute       | Decode        |
| T5   |               |               | Execute       |

This means multiple instructions are active at the same time.

---

## 2. Multiple Cores

Modern CPUs have multiple cores.

Each core can fetch, decode, and execute its own instructions independently.

### Example:

- Core 1 runs one thread
- Core 2 runs another
- Core 3 runs another

So many instruction streams can happen together.

---

## 3. Superscalar Execution

Some CPUs can execute **multiple instructions in the same clock cycle** if they are independent.

This improves performance.

---

## 4. SIMD Execution

The same instruction can be applied to multiple data values at once.

### Example:

If we want to add two arrays:

```text
A = [1,2,3,4]
B = [5,6,7,8]
```

Instead of doing:

- 1+5
- 2+6
- 3+7
- 4+8

one by one, SIMD may process multiple additions together.

---

## Importance

This is important because **parallel computing is not only about running many programs**.

It also happens **inside the CPU architecture itself**.

That means parallelism exists at both:

- hardware level
- software level

---

# 7. Why Parallel and Distributed Computing is Needed

This is one of the most practical questions in the course.

---

## Main Reason

The biggest reason is:

> Modern problems are too large and too slow for pure serial execution.

---

## Detailed Reasons

## 1. Need for Speed

Many applications require very fast results.

### Example:

- online transactions,
- live video processing,
- scientific simulation,
- gaming,
- AI inference.

If we wait for one processor to do everything alone, it may take too long.

---

## 2. Large Amount of Data

Today’s systems work with:

- big databases,
- cloud storage,
- machine learning datasets,
- social media traffic,
- sensor data,
- financial transactions.

This data volume is too large for simple single-thread execution.

---

## 3. Better Resource Utilization

Modern hardware already has:

- multiple cores,
- multiple processors,
- GPUs,
- networked servers.

If we only use one core at a time, we waste available resources.

Parallel and distributed computing help us **fully utilize hardware**.

---

## 4. Scalability

As workload increases, systems should be able to handle more users and more tasks.

This is difficult in serial systems.

Parallel and distributed systems support growth much better.

---

## 5. Reliability and Availability

Distributed systems can continue working even if one machine fails.

This is useful in real-world systems where downtime is costly.

---

## 6. Cost Efficiency

Instead of buying one extremely powerful machine, organizations often use:

- multiple affordable servers,
- clusters,
- cloud instances.

This can be more practical and scalable.

---

## Final Importance

Without parallel and distributed computing, many modern technologies would become:

- too slow,
- too expensive,
- too limited,
- or impossible to run efficiently.

---

# 8. Where Parallel and Distributed Computing is Used

These concepts are not just theory.  
They are used in many real-world applications.

---

## 1. Artificial Intelligence and Machine Learning

Training AI models requires huge computation.

Parallelism is used for:

- matrix operations,
- neural network training,
- GPU acceleration.

Distributed computing is used when training is too large for one machine.

---

## 2. Scientific Simulations

Used in:

- weather forecasting,
- climate modeling,
- physics simulations,
- molecular biology,
- space research.

These calculations are massive and often require supercomputers.

---

## 3. Big Data Systems

Frameworks like Hadoop and Spark use distributed computing to process huge datasets.

Used in:

- analytics,
- recommendation systems,
- business intelligence.

---

## 4. Cloud Computing

Cloud platforms use distributed systems to provide:

- storage,
- virtual machines,
- web hosting,
- scalable services.

---

## 5. Search Engines

Search engines process billions of pages and queries.

This is only possible using distributed computing.

---

## 6. Banking and Finance

Used in:

- fraud detection,
- transaction processing,
- market analysis,
- risk calculation.

---

## 7. Gaming and Graphics

Graphics rendering often uses parallel hardware like GPUs.

Used in:

- 3D rendering,
- real-time gaming,
- visual effects.

---

## 8. Video and Image Processing

Parallelism is useful for:

- video encoding,
- filtering,
- compression,
- object detection.

---

## 9. Web Servers and Social Platforms

Large websites need to handle many users at once.

Distributed systems help balance traffic and improve uptime.

---

# 9. Multithreading vs Multiprocessing

This is one of the most asked and most confusing topics, so it must be understood clearly.

---

## What is Multithreading?

**Multithreading** means:

> A single process contains multiple threads that can run concurrently.

Threads are lightweight execution units inside a process.

---

## Key Idea

All threads inside the same process share:

- code,
- data,
- memory,
- resources.

This makes communication easier and faster.

---

## Example of Multithreading

A web browser may use threads for:

- loading a webpage,
- playing audio,
- rendering images,
- handling user clicks.

These can happen at the same time.

---

## What is Multiprocessing?

**Multiprocessing** means:

> Using multiple independent processes, often to perform work in parallel.

Each process has its own memory space.

---

## Example of Multiprocessing

Suppose a Python program starts 4 separate processes to calculate 4 parts of a dataset.

Each process works independently.

---

## Detailed Comparison

| Feature       | Multithreading                | Multiprocessing                           |
| ------------- | ----------------------------- | ----------------------------------------- |
| Unit          | Thread                        | Process                                   |
| Memory        | Shared                        | Separate                                  |
| Communication | Easier                        | More difficult                            |
| Isolation     | Weak                          | Strong                                    |
| Overhead      | Low                           | High                                      |
| Crash Impact  | One thread can affect process | One process usually does not crash others |

---

## Which One is Better?

There is no single “always best” answer.

It depends on the problem.

---

## When Multithreading is Preferred

Use multithreading when:

- tasks share data often,
- you want lightweight concurrency,
- the tasks are related,
- you need fast communication.

### Example:

GUI apps, web clients, file downloading.

---

## When Multiprocessing is Preferred

Use multiprocessing when:

- tasks are CPU-heavy,
- tasks need isolation,
- true parallel execution is needed,
- crashes must be separated.

### Example:

Scientific computation, image processing, simulations.

---

## Important Practical Note (Especially in Python)

In Python, multithreading is useful, but for CPU-heavy tasks, **multiprocessing is often preferred** because threads may be limited by the **GIL (Global Interpreter Lock)** in standard CPython.

So:

- **I/O-bound tasks** → often multithreading
- **CPU-bound tasks** → often multiprocessing

This is a very important practical preference.

---

# 10. Process vs Thread

This topic is related to the previous one, but it should be understood separately.

---

## What is a Process?

A **process** is:

> A program in execution.

It is an independent running instance of a program.

A process has:

- its own memory,
- its own address space,
- system resources,
- execution state.

### Example:

When you open:

- Chrome,
- VS Code,
- Calculator,

each one runs as a process.

---

## What is a Thread?

A **thread** is:

> The smallest unit of execution inside a process.

A process may contain:

- one thread,
- or multiple threads.

Threads inside the same process share resources.

---

## Example

Suppose a music app is running.

It may use one thread for:

- audio playback,

another for:

- UI interaction,

another for:

- downloading album art.

All of these are part of the same process.

---

## Detailed Comparison

| Feature            | Process                          | Thread                                |
| ------------------ | -------------------------------- | ------------------------------------- |
| Definition         | Independent program in execution | Small execution unit inside a process |
| Memory             | Separate                         | Shared                                |
| Creation Cost      | More expensive                   | Less expensive                        |
| Communication      | Harder                           | Easier                                |
| Speed of Switching | Slower                           | Faster                                |
| Isolation          | Strong                           | Weak                                  |

---

## Importance of This Difference

This matters because software design depends on whether the problem should be broken into:

- **separate processes**
  or
- **multiple threads**

That choice affects:

- performance,
- safety,
- communication,
- memory usage,
- debugging complexity.

---

# 11. Parallel Computing System Types

Parallel computing does not happen in only one way.  
It can happen at multiple levels.

---

## 1. Bit-Level Parallelism

### Definition

Bit-level parallelism improves performance by increasing the number of bits the processor can handle at once.

---

## Example

A:

- 8-bit processor handles 8 bits at a time
- 32-bit processor handles 32 bits at a time
- 64-bit processor handles 64 bits at a time

This means more data can be processed per operation.

---

## Importance

This improves low-level performance without changing the algorithm.

It is mainly a **hardware-level improvement**.

---

## 2. Instruction-Level Parallelism (ILP)

### Definition

Instruction-level parallelism means:

> Multiple instructions are executed or overlapped at the same time.

---

## Example

A CPU may:

- fetch one instruction,
- decode another,
- execute another,

all simultaneously.

This is often done through:

- pipelining,
- superscalar execution,
- out-of-order execution.

---

## Importance

ILP improves performance **inside the CPU**, even if the programmer does not explicitly write parallel code.

---

## 3. Task-Level Parallelism (TLP)

### Definition

Task-level parallelism means:

> Different tasks or threads are executed at the same time.

---

## Example

A program may do:

- file reading,
- processing,
- saving,
- UI updates

simultaneously.

---

## Importance

This is the type of parallelism most programmers deal with directly.

It is very common in:

- multithreading,
- multiprocessing,
- distributed systems.

---

## Comparison

| Type              | Focus                     | Example                    |
| ----------------- | ------------------------- | -------------------------- |
| Bit-Level         | More bits per instruction | 64-bit CPU                 |
| Instruction-Level | More instructions at once | Pipelining                 |
| Task-Level        | More tasks at once        | Multiple threads/processes |

---

# 12. Advantages of Parallel Computing

Parallel computing is popular because it provides many practical benefits.

---

## 1. Faster Execution

The biggest benefit is reduced execution time.

Large tasks can be divided and completed more quickly.

---

## 2. Better CPU Utilization

Instead of leaving CPU cores idle, parallel computing uses more of the available hardware.

---

## 3. Ability to Solve Bigger Problems

Some problems are too large for one processor to solve efficiently.

Parallel systems make these possible.

---

## 4. Improved Productivity

In many systems, users can do multiple things at once more smoothly.

---

## 5. Better Performance in Real-Time Systems

Systems like:

- live monitoring,
- gaming,
- simulations,
- robotics

often require fast response.

Parallelism helps achieve this.

---

## 6. Scalability

Parallel systems can often be expanded more easily than serial systems.

---

## 7. Better for Modern Applications

Many modern applications naturally involve multiple independent operations.

So parallel design often matches real-world computing needs better.

---

## Important Note

Parallel computing is powerful, but it is **not automatically better in every situation**.

It can also introduce:

- synchronization issues,
- communication overhead,
- race conditions,
- debugging difficulty.

So it should be used **when beneficial**, not just because it sounds advanced.

---

# 13. Distributed Computing vs Parallel Computing

These two are related but not identical.

This comparison is very important.

---

## Parallel Computing

Parallel computing usually means:

> Multiple processing units work together on a task, often within one machine or tightly coupled system.

---

## Distributed Computing

Distributed computing means:

> Multiple separate computers connected through a network work together on a task.

---

## Similarities

Both involve:

- dividing work,
- multiple execution units,
- improving efficiency,
- handling large tasks.

---

## Differences

| Feature          | Parallel Computing                    | Distributed Computing           |
| ---------------- | ------------------------------------- | ------------------------------- |
| System Type      | Usually one machine / tightly coupled | Multiple computers              |
| Communication    | Very fast                             | Slower than local communication |
| Memory           | Often shared or closely connected     | Separate memory                 |
| Failure Handling | Less independent                      | More fault-tolerant             |
| Scalability      | Good                                  | Usually higher                  |
| Example          | Multi-core CPU                        | Cluster of servers              |

---

## Which is Preferred?

### Prefer Parallel Computing when:

- low-latency execution is needed,
- processors are in the same machine,
- memory sharing is useful.

### Prefer Distributed Computing when:

- workload is very large,
- one machine is not enough,
- scalability matters,
- networked collaboration is acceptable.

---

## Practical Understanding

You can think of it like this:

### Parallel Computing:

**Many workers in one room**

### Distributed Computing:

**Many workers in different buildings connected by phone/internet**

Both can work together, but the second one has more communication distance.

---

# 14. Scale Up vs Scale Out

These are two important ways to improve system capacity.

---

## What is Scale Up?

**Scale Up** means:

> Improving the power of a single machine.

This is also called:

> **Vertical Scaling**

---

## Examples of Scale Up

- adding more RAM,
- using a faster CPU,
- increasing storage,
- increasing number of cores.

---

## Benefits of Scale Up

- simpler to manage,
- fewer machines,
- easier communication inside one system.

---

## Limitations of Scale Up

- hardware upgrades can become expensive,
- there is a physical limit,
- one machine can still become a bottleneck.

---

## What is Scale Out?

**Scale Out** means:

> Increasing capacity by adding more machines.

This is also called:

> **Horizontal Scaling**

---

## Examples of Scale Out

- using 5 web servers instead of 1,
- creating a cluster,
- adding more nodes to a distributed system.

---

## Benefits of Scale Out

- easier long-term expansion,
- better fault tolerance,
- useful for distributed applications.

---

## Limitations of Scale Out

- communication becomes more complex,
- coordination is harder,
- network overhead increases.

---

## Comparison Table

| Feature         | Scale Up            | Scale Out          |
| --------------- | ------------------- | ------------------ |
| Meaning         | Improve one machine | Add more machines  |
| Also Called     | Vertical Scaling    | Horizontal Scaling |
| Simplicity      | Simpler             | More complex       |
| Scalability     | Limited             | Better             |
| Fault Tolerance | Lower               | Higher             |

---

## Which is Preferred?

### Scale Up is preferred when:

- system is still small,
- one powerful machine is enough,
- simplicity matters.

### Scale Out is preferred when:

- growth is expected,
- traffic is large,
- distributed systems are needed.

In modern cloud systems, **scale out is often more common**.

---

# 15. High Throughput Computing vs High Performance Computing

These two are often confused, but they focus on different goals.

---

## High Throughput Computing (HTC)

### Definition

HTC focuses on:

> Completing a large number of tasks over time.

The goal is **maximum total work done**.

---

## Example

Suppose a system must process:

- 10,000 student files,
- 50,000 documents,
- or 1 million independent jobs.

The focus is not necessarily one super-fast result, but rather **handling many tasks efficiently**.

---

## High Performance Computing (HPC)

### Definition

HPC focuses on:

> Solving one very large or highly demanding problem as fast as possible.

The goal is **maximum speed and computational power**.

---

## Example

Used in:

- weather simulation,
- fluid dynamics,
- space science,
- molecular modeling,
- supercomputing.

---

## Detailed Comparison

| Feature           | HTC                | HPC                     |
| ----------------- | ------------------ | ----------------------- |
| Focus             | Many tasks         | One huge task           |
| Goal              | Total productivity | Maximum speed           |
| Example           | Batch jobs         | Scientific simulation   |
| Task Relationship | Often independent  | Often tightly connected |

---

## Which is Preferred?

### HTC is preferred when:

- there are many independent jobs,
- throughput matters more than immediate speed.

### HPC is preferred when:

- one very complex task must finish as fast as possible.

Both are important, but they serve different computing goals.

---

# 16. MPI Library in Python

This is an important practical topic in distributed and parallel programming.

---

## What is MPI?

**MPI** stands for:

> **Message Passing Interface**

It is a standard used for communication between multiple processes, especially in distributed memory systems.

---

## Why MPI is Needed

When processes are running separately, especially on different machines, they do not automatically share memory.

So they need a way to:

- send data,
- receive data,
- coordinate tasks,
- combine results.

MPI provides that communication system.

---

## MPI in Python

In Python, MPI is commonly used through the library:

```python
from mpi4py import MPI
```

This library allows Python programs to use MPI concepts.

---

## What MPI Helps Us Do

MPI allows processes to:

- know their identity,
- know total number of processes,
- send messages,
- receive messages,
- divide work,
- gather results.

---

## Important MPI Concepts

### 1. Rank

Each process has a unique ID called **rank**.

#### Example:

If there are 4 processes:

- rank 0
- rank 1
- rank 2
- rank 3

---

### 2. Size

The total number of processes running is called **size**.

---

### 3. Send and Receive

Processes can communicate using:

- `send()`
- `recv()`

---

## Example Use Case

Suppose we want to process a huge array.

MPI can be used to:

- split the array across processes,
- let each process compute part of the result,
- gather the final answer.

---

## Why MPI is Important

MPI is especially useful when:

- shared memory is not available,
- processes are on multiple machines,
- distributed computing is required,
- high-performance systems are used.

---

## Preference

MPI is preferred for:

- distributed-memory parallel systems,
- clusters,
- scientific parallel applications.

It is less necessary for very small programs running only inside one machine.

---

# 17. Amdahl’s Law

This is one of the most important laws in parallel computing.

---

## Definition

**Amdahl’s Law** states:

> The maximum improvement gained from parallelism is limited by the part of the program that must remain serial.

This means:

Even if we keep adding more processors, we cannot get unlimited speedup if some part of the program still runs sequentially.

---

## Main Idea Behind Amdahl’s Law

A program usually has two parts:

- **Parallel part** → can run on multiple processors
- **Serial part** → must run one after another

The serial part creates a limit.

---

## Formula

\[
Speedup = \frac{1}{(1 - P) + \frac{P}{N}}
\]

Where:

- `P` = fraction of the program that can be parallelized
- `1 - P` = fraction that is serial
- `N` = number of processors
- `Speedup` = performance improvement

---

## Meaning of the Formula

Suppose:

- 80% of a program can run in parallel
- 20% must remain serial

Even if you use many processors, that 20% serial part still takes time and limits total speedup.

---

## Why Amdahl’s Law is Important

It teaches a very practical lesson:

> Adding more processors does not always mean proportional speed increase.

This is extremely important in system design.

---

## Preference / Usefulness

Amdahl’s Law is useful when:

- problem size is fixed,
- we want to estimate realistic speedup,
- we want to understand limitations of parallelism.

---

## Main Limitation

Amdahl’s Law is a bit pessimistic for large-scale systems because it assumes:

> The total problem size remains fixed.

That is why Gustafson’s Law also becomes important.

---

# 18. Gustafson’s Law

Gustafson’s Law gives a more optimistic and practical view for large-scale computing.

---

## Definition

**Gustafson’s Law** states:

> As the number of processors increases, we can solve larger problems efficiently in nearly the same amount of time.

Instead of keeping the problem fixed, it assumes that the workload can grow.

---

## Formula

\[
S(N) = N - \alpha (N - 1)
\]

Where:

- `S(N)` = speedup using `N` processors
- `N` = number of processors
- `\alpha` (alpha) = serial fraction of the program

---

## Meaning of Variables

### `S(N)`

This shows the effective speedup.

### `N`

This is the number of processors used.

### `\alpha`

This is the part of the program that must still run serially.

---

## Main Idea

Amdahl’s Law says:

> “Fixed problem size limits speedup.”

Gustafson’s Law says:

> “If processors increase, we can solve larger problems efficiently.”

This is much more realistic for modern computing.

---

## Why It is Important

Gustafson’s Law better reflects real-world systems like:

- supercomputers,
- scientific computing,
- large simulations,
- big data processing.

Because in practice, when we get more power, we usually solve **bigger problems**, not just the same old small one faster.

---

## Amdahl vs Gustafson

| Feature    | Amdahl’s Law              | Gustafson’s Law            |
| ---------- | ------------------------- | -------------------------- |
| Assumption | Fixed problem size        | Scaled problem size        |
| View       | Pessimistic               | More practical/optimistic  |
| Focus      | Limitation of parallelism | Benefit of more processors |

---

# 19. Flynn’s Classification

Flynn’s Classification is used to categorize computer architectures based on:

- number of **instruction streams**
- number of **data streams**

This helps us understand different processing models.

There are 4 major categories.

---

## 19.1 SISD – Single Instruction, Single Data

### Definition

One processor executes:

- one instruction stream
- on one data stream

This is the traditional serial model.

---

### Characteristics

- simple architecture
- sequential execution
- no real parallelism

---

### Example

- simple calculator
- old single-core program
- basic sequential array processing

#### Programming Example

```python
for i in range(len(arr)):
    arr[i] = arr[i] + 1
```

This is SISD-style thinking.

---

### Importance

SISD is useful for understanding the **starting point** of computer architecture before parallelism.

---

## 19.2 SIMD – Single Instruction, Multiple Data

### Definition

A single instruction is applied to multiple data values at the same time.

---

### Characteristics

- same operation repeated on many values
- very useful for data-parallel problems

---

### Example

- array operations
- image processing
- vector addition
- matrix operations
- GPU workloads

---

### Why SIMD is Preferred

SIMD is preferred when:

- the same task must be repeated on many data items,
- data is highly regular,
- performance matters.

---

## 19.3 MISD – Multiple Instruction, Single Data

### Definition

Multiple instruction streams operate on the same data stream.

---

### Characteristics

- rare in general-purpose systems
- not commonly seen in everyday programming

---

### Example

Often discussed in:

- fault-tolerant systems,
- signal processing,
- systems where the same input is processed in multiple ways for safety.

---

### Importance

MISD is not common, but it is important academically because it completes Flynn’s model.

---

## 19.4 MIMD – Multiple Instruction, Multiple Data

### Definition

Multiple processors execute:

- different instructions
- on different data

This is one of the most important and practical parallel models.

---

### Characteristics

- flexible
- powerful
- common in modern systems

---

### Example

- multicore CPUs
- multiprocessing systems
- distributed systems
- clusters
- servers running multiple tasks

---

### Why MIMD is Preferred

MIMD is preferred when:

- tasks are different,
- data is different,
- system needs flexibility,
- real-world workloads are complex.

Most modern computing systems are closer to **MIMD**.

---

## Summary Table

| Type | Full Form                          | Meaning                                  | Example                |
| ---- | ---------------------------------- | ---------------------------------------- | ---------------------- |
| SISD | Single Instruction Single Data     | One instruction on one data              | Calculator             |
| SIMD | Single Instruction Multiple Data   | Same instruction on many data items      | Array operations       |
| MISD | Multiple Instruction Single Data   | Different instructions on same data      | Fault-tolerant systems |
| MIMD | Multiple Instruction Multiple Data | Different instructions on different data | Multicore systems      |

---

# 20. Parallel Algorithm Key Concepts

A **parallel algorithm** is an algorithm designed so that multiple parts of the work can run simultaneously.

To understand parallel algorithms, two major concepts are very important.

---

## 20.1 Task Decomposition

### Definition

Task decomposition means:

> Breaking a large problem into smaller sub-problems or tasks.

This is the foundation of parallel design.

---

### Example

Suppose we want to sum 1000 numbers.

Instead of one processor doing all 1000, we divide the work:

- Processor 1 → 1 to 250
- Processor 2 → 251 to 500
- Processor 3 → 501 to 750
- Processor 4 → 751 to 1000

Then combine results.

---

### Why It is Important

Task decomposition helps with:

- speed,
- load sharing,
- scalability,
- easier use of multiple processors.

---

### Good Task Decomposition Should Ensure

- tasks are balanced,
- no processor is overloaded,
- tasks are not too dependent on each other,
- communication is minimized.

---

### Preference

Task decomposition is preferred when:

- the problem can be broken into independent or semi-independent parts.

It becomes difficult when everything depends on everything else.

---

## 20.2 Synchronization

Even if tasks are divided, they often need to coordinate.

### Example:

If two threads update the same variable, they must be synchronized.

This prevents issues like:

- race conditions,
- inconsistent data,
- corrupted results.

---

## 20.3 Communication

In parallel and distributed systems, tasks often need to exchange information.

This communication can happen through:

- shared memory,
- message passing,
- queues,
- network communication.

Communication should be minimized when possible because it adds overhead.

---

## 20.4 Load Balancing

Load balancing means:

> Work should be distributed fairly across processors.

### Bad Case:

One processor is overloaded while others stay idle.

### Good Case:

All processors have nearly equal work.

This improves efficiency.

---

# 21. Memory Organization

Memory organization is a key concept in parallel systems because it determines:

- how processors access memory,
- how they share data,
- how they communicate.

There are two main approaches.

---

## 21.1 Shared Memory

In shared memory systems:

> Multiple processors or threads access the same memory space.

---

### Characteristics

- easy communication,
- all units can see shared variables,
- simpler programming in many cases.

---

### Example

Threads inside a process usually use shared memory.

---

### Advantages

- easier data sharing,
- lower communication overhead,
- simpler for some applications.

---

### Disadvantages

- synchronization becomes necessary,
- race conditions can occur,
- scaling can become difficult.

---

## 21.2 Distributed Memory

In distributed memory systems:

> Each processor has its own private memory.

Processors cannot directly access each other’s memory.

They communicate by sending messages.

---

### Characteristics

- separate memory spaces,
- message passing required,
- common in clusters and distributed systems.

---

### Example

Multiple computers in a cluster.

---

### Advantages

- scalable,
- independent nodes,
- suitable for large systems.

---

### Disadvantages

- communication is harder,
- programming is more complex,
- data exchange adds overhead.

---

## Shared vs Distributed Memory

| Feature       | Shared Memory                   | Distributed Memory      |
| ------------- | ------------------------------- | ----------------------- |
| Memory Access | Common memory                   | Separate memory         |
| Communication | Direct through shared variables | Through message passing |
| Simplicity    | Easier                          | More complex            |
| Scalability   | Limited                         | Better                  |

---

# 22. Shared Memory Models

Now we go deeper into memory architecture.

These models explain **how processors access memory in shared or related memory systems**.

---

## 22.1 UMA – Uniform Memory Access

### Definition

In UMA systems:

> All processors take approximately the same time to access any memory location.

---

### Characteristics

- one shared memory
- equal memory access time
- simpler design

---

### Example

A small symmetric multiprocessor system where all CPUs access RAM equally.

---

### Advantages

- easy to understand,
- simple programming model,
- predictable memory access.

---

### Disadvantages

- does not scale very well for very large systems.

---

### When Preferred

UMA is preferred when:

- system size is small to medium,
- simplicity matters,
- equal access performance is desired.

---

## 22.2 NUMA – Non-Uniform Memory Access

### Definition

In NUMA systems:

> Memory access time depends on which memory is being accessed.

A processor can access:

- its **local memory** faster
- another processor’s memory slower

---

### Characteristics

- memory is still logically shared,
- but physically distributed near processors.

---

### Example

A processor accesses its own attached memory quickly, but remote memory more slowly.

---

### Advantages

- better scalability than UMA,
- more efficient for larger multiprocessor systems.

---

### Disadvantages

- programming and optimization become more difficult,
- poor data placement can reduce performance.

---

### When Preferred

NUMA is preferred when:

- systems are large,
- scalability matters,
- high-performance multiprocessor systems are needed.

---

## 22.3 NORMA – No Remote Memory Access

### Definition

In NORMA systems:

> Each processor has its own private memory, and processors cannot directly access each other’s memory.

Communication must happen using messages.

---

### Characteristics

- no shared memory
- communication through message passing
- very similar to distributed-memory systems

---

### Example

A cluster of computers connected through a network.

---

### Advantages

- highly scalable,
- useful for distributed computing,
- clear separation of memory.

---

### Disadvantages

- communication is more complex,
- data sharing is harder,
- programming effort is higher.

---

### When Preferred

NORMA is preferred when:

- distributed computing is required,
- many separate nodes are used,
- message-passing systems are needed.

---

## 22.4 COMA – Cache Only Memory Architecture

> **Note:** If your teacher specifically wrote **CDMA**, follow your teacher’s wording.  
> Academically, this topic is more commonly written as **COMA**.

### Definition

In COMA systems:

> Main memory behaves more like a large cache.

Data can move dynamically to where it is needed.

---

### Main Idea

Instead of fixed memory ownership, the system tries to place data near the processor that is using it.

---

### Advantages

- better locality,
- improved memory flexibility,
- useful in some advanced high-performance systems.

---

### Disadvantages

- more complex hardware,
- harder system design.

---

### When Preferred

Used mainly in advanced or specialized architectures, not common in basic everyday systems.

---

# 23. Conclusion

Parallel and Distributed Computing is a very important field in modern computer science.

It exists because:

- modern problems are too large,
- performance requirements are too high,
- and one processor alone is often not enough.

By studying this subject, we understand how systems improve performance through:

- multithreading,
- multiprocessing,
- task decomposition,
- message passing,
- shared memory,
- distributed memory,
- and processor coordination.

This subject is highly important in areas such as:

- AI,
- cloud computing,
- scientific simulations,
- web systems,
- big data,
- graphics,
- and modern software engineering.

In short:

> Parallel and Distributed Computing helps computers do more work, in less time, with better scalability and efficiency.
