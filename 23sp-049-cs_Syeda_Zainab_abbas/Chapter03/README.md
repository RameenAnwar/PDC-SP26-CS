# ⚙️ Chapter 03 — Process-Based Parallelism

> **Topic:** The `multiprocessing` module — real parallelism, beyond the GIL

---

## 🎯 Overview
Where threads share memory and fight the GIL, **processes** each get their **own memory space and Python interpreter**. That means processes achieve *true* parallel execution on multiple CPU cores — the right tool for CPU-bound work. The trade-off: processes can't share memory directly, so they must **communicate** explicitly via Queues and Pipes.

---

## 🧠 Key Concepts

| Concept | Meaning |
|--------|---------|
| **Spawning a process** | `multiprocessing.Process(target=..., args=...)` then `.start()`. |
| **`join()`** | Wait for a process to finish before continuing. |
| **Daemon process** | A background process that is **killed automatically** when the main program exits. |
| **Process Pool** | A fixed set of reusable workers; `pool.map()` splits work among them. |
| **IPC (Inter-Process Communication)** | How separate processes exchange data — via **Queue** or **Pipe**. |
| **`terminate()`** | Forcefully kill a process; `is_alive()` checks its status. |

---

## 📂 Files in this folder

### Creating & managing processes
| File | What it demonstrates |
|------|----------------------|
| `spawning_processes.py` | Spawn a process that runs a function. |
| `myFunc.py` | The worker function in its own module. |
| `spawning_processes_namespace.py` | Spawn a function **imported** from another module. |
| `naming_processes.py` | Custom vs default process names. |
| `killing_processes.py` | Full lifecycle: start → run → `terminate()` → `join()` → exit code. |
| `process_in_subclass.py` | Define a process by **subclassing** `Process`. |

### Coordination
| File | What it demonstrates |
|------|----------------------|
| `process_pool.py` | `Pool.map()` squares 0–99 across **4 workers**. |
| `processes_barrier.py` | Barrier: `p1`,`p2` sync up; `p3`,`p4` don't. |
| `run_background_processes.py` | **Daemon** process (may not finish). |
| `run_background_processes_no_daemons.py` | Non-daemon variant (always finishes). |

### Communication (IPC)
| File | What it demonstrates |
|------|----------------------|
| `communicating_with_queue.py` | Producer/consumer processes sharing a `Queue`. |
| `communicating_with_pipe.py` | Pipe: P1 sends 0–9 → P2 squares them → main prints results. |

---

## ▶️ How to run
```bash
python process_pool.py                 # → [0, 1, 4, 9, ... 9801]
python communicating_with_pipe.py      # → 0 1 4 9 16 ... 81
python killing_processes.py            # watch the lifecycle prints
```

> ⚠️ Always keep the `if __name__ == '__main__':` guard. On **Windows/macOS** `multiprocessing` re-imports the module in each child, and without the guard you'd spawn processes endlessly.

---

## ✅ Summary
Processes = independent interpreters = real multi-core parallelism. The price is **no shared memory**, so you communicate through **Queues** and **Pipes**, and manage lifecycle with `start` / `join` / `terminate` / daemon flags.
