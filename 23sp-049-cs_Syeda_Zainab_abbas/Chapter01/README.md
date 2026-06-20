# 📘 Chapter 01 — Getting Started with Parallel Computing & Python

> **Course:** Parallel & Distributed Computing (PDC) · **Topic:** Foundations of parallelism + Python refresher

---

## 🎯 Overview
This chapter sets the stage for the whole course. It first refreshes core Python (classes, control flow, collections, files) and then introduces the single most important comparison in parallel computing: running the **same workload three different ways** and measuring how long each takes.

The benchmark workload is simple but CPU-heavy: fill a list with **10 million random numbers, repeated 10 times**. We run it:
1. **Serially** — one task after another on a single core.
2. **With threads** — 10 threads.
3. **With processes** — 10 processes.

---

## 🧠 Key Concepts

| Concept | Meaning |
|--------|---------|
| **Serial execution** | Tasks run one-by-one. Simple, predictable, but slow for heavy work. |
| **Concurrency** | Multiple tasks *in progress* at once (not necessarily literally simultaneous). |
| **Parallelism** | Multiple tasks literally running *at the same instant* on different cores. |
| **GIL (Global Interpreter Lock)** | A lock in CPython that lets only **one thread execute Python bytecode at a time**. This is *the* reason threads don't speed up CPU-bound work. |
| **Process** | An independent program with its **own memory + interpreter** → bypasses the GIL → real parallelism. |

> 💡 **Take-away of the whole chapter:** For **CPU-bound** work, use *processes*. For **I/O-bound** work (network, disk), *threads* are fine.

---

## 📂 Files in this folder

### Parallelism demos
| File | What it demonstrates |
|------|----------------------|
| `do_something.py` | Helper module. `do_something(count, out_list)` fills a list with random floats — the shared CPU-bound workload. |
| `serial_test.py` | Runs the workload **sequentially** (baseline timing). |
| `multithreading_test.py` | Runs it with **10 threads** — usually *no* speed-up due to the GIL. |
| `multiprocessing_test.py` | Runs it with **10 processes** — true parallel speed-up across cores. |
| `thread_and_processes.py` | All approaches in one file for side-by-side timing. |

### Python refresher
| File | What it demonstrates |
|------|----------------------|
| `classes.py` | OOP: difference between **class variables** (shared) and **instance variables** (per-object), plus inheritance. |
| `dir.py` | `if / elif / else` + summing a list with a `for` loop. |
| `flow.py` | The three control-flow tools: **IF**, **FOR**, **WHILE**. |
| `lists.py` | Lists, tuples, dictionaries, and functions as first-class values. |
| `file.py` | Basic file **write** then **read**. |

---

## ▶️ How to run
```bash
python serial_test.py
python multithreading_test.py
python multiprocessing_test.py
```

## 📊 What you should observe
```
serial time        ≈ slow   (baseline)
multithreading time ≈ same / slightly slower than serial  (GIL)
multiprocesses time ≈ noticeably faster on a multi-core CPU
```

> ⚠️ Run the `*_test.py` files from a **terminal**, not inside some IDE consoles — `multiprocessing` needs the `if __name__ == "__main__":` guard (already included) to spawn child processes correctly on Windows.

---

## ✅ Summary
Chapter 1 proves *why* we need parallelism, *where* it helps, and the GIL gotcha that shapes every later chapter.
