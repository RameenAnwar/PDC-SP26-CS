# 🧵 Chapter 02 — Thread-Based Parallelism

> **Topic:** Creating threads and synchronizing them safely

---

## 🎯 Overview
A **thread** is the smallest unit of execution inside a process; threads of the same process **share memory**. That sharing is powerful but dangerous: if two threads touch the same data at once you get a **race condition**. This chapter covers how to *create* threads two ways and, crucially, the five classic tools used to *synchronize* them.

---

## 🧠 Key Concepts

| Tool | Use it when… |
|------|--------------|
| **Lock** | You need *mutual exclusion* — only one thread in a critical section at a time. |
| **RLock** (re-entrant) | The same thread must acquire the lock again (e.g. a locked method calls another locked method). |
| **Semaphore** | You want to allow *N* threads through, or signal "an item is ready". |
| **Barrier** | A group of threads must all **wait for each other** at a common point. |
| **Condition** | One thread must `wait()` until another `notify()`s it (bounded producer/consumer). |
| **Event** | Simple on/off flag threads can wait on (`set` / `clear`). |
| **Queue** | The *safest* option — a thread-safe container that handles locking for you. |

> 💡 **Two ways to make a thread:**
> 1. Pass a target → `Thread(target=func, args=(...))`
> 2. Subclass `Thread` and override `run()`

---

## 📂 Files in this folder

### Creating threads
| File | What it demonstrates |
|------|----------------------|
| `Thread_definition.py` | Simplest thread: pass a target function. |
| `Thread_determine.py` | Name threads & read the current thread's name. |
| `Thread_name_and_processes.py` | Create a thread by **subclassing** `Thread`. |

### Synchronization
| File | What it demonstrates |
|------|----------------------|
| `MyThreadClass.py` | 9 threads, **no lock** → messages interleave (concurrent). |
| `MyThreadClass_lock.py` | Same, **with a Lock** → effectively serial, clean output. |
| `MyThreadClass_lock_2.py` | Lock released *early* (before `sleep`) → behaviour changes — shows *where* you release matters. |
| `Rlock.py` | Re-entrant lock; `add()`/`remove()` both re-enter via `execute()`. |
| `Semaphore.py` | Producer/consumer; semaphore starts at 0 so consumer waits for producer. |
| `Barrier.py` | 3 "runners" wait at a barrier; race ends only when all arrive. |
| `Condition.py` | Bounded (max 10) producer/consumer using `wait`/`notify`. |
| `Event.py` | Producer/consumer using an event flag. |
| `Threading_with_queue.py` | 1 producer + 3 consumers sharing a thread-safe `Queue`. |

---

## ▶️ How to run
```bash
python MyThreadClass.py          # watch interleaved output
python MyThreadClass_lock.py     # compare: now it's orderly
python Threading_with_queue.py   # the recommended pattern
```

## 🔍 What to compare
Run `MyThreadClass.py` vs `MyThreadClass_lock.py` back-to-back. The first prints a jumbled mix; the second prints each thread's block cleanly — that visual difference **is** the lesson on mutual exclusion.

---

## ✅ Summary
Threads share memory → race conditions are the enemy → locks, semaphores, conditions, events, barriers and queues are the defence. When in doubt, **use a `Queue`**.
