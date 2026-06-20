# ⏳ Chapter 05 — Asynchronous Programming (`asyncio`)

> **Topic:** Single-threaded concurrency with coroutines and an event loop

---

## 🎯 Overview
`asyncio` gives you **concurrency without threads or processes**. A single thread runs an **event loop** that juggles many **coroutines**. Whenever a coroutine hits an `await` (waiting on I/O, a timer, etc.), it *yields control* back to the loop, which runs another coroutine in the meantime. This makes asyncio ideal for **I/O-bound** workloads (thousands of network calls) where threads would be wasteful.

> 📝 **Why is the code here `#` commented with the output written in?**
> Some examples take command-line arguments or run an endless loop, and the textbook versions use the **old `@asyncio.coroutine` / `yield from`** style. So the code is preserved as comments with the **expected output documented at the bottom** of each file.

---

## 🧠 Key Concepts

| Term | Meaning |
|------|---------|
| **Coroutine** | A function that can pause and resume (`async def` / old `@asyncio.coroutine`). |
| **Event loop** | The scheduler that runs coroutines and callbacks. |
| **`await` / `yield from`** | "Pause here, let others run, resume when ready." |
| **Task** | A coroutine wrapped so the loop schedules it to run. |
| **Future** | A placeholder for a result that will arrive later. |
| **Cooperative multitasking** | Tasks voluntarily yield — there's no pre-emption, so one blocking call stalls everyone. |

> 💡 **Modern syntax note:** These files use `@asyncio.coroutine` + `yield from`. On **Python 3.8+** rewrite as `async def` + `await`, and replace the removed `time.clock()` with `time.perf_counter()`.

---

## 📂 Files in this folder
| File | What it demonstrates |
|------|----------------------|
| `asyncio_task_manipulation.py` | Three coroutines (factorial, fibonacci, binomial) run as **Tasks** and interleave. |
| `asyncio_coroutine.py` | A **finite state machine** where each state is a coroutine calling the next. |
| `asyncio_event_loop.py` | Scheduling callbacks with `call_soon` / `call_later` on the loop. |
| `asyncio_and_futures.py` | **Futures** + done-callbacks; results delivered via `set_result`. |
| `concurrent_futures_pooling.py` | Benchmarks **Sequential vs ThreadPool vs ProcessPool**. |

---

## ▶️ How to run
```bash
python asyncio_and_futures.py 5 6     # args → sum=5, factorial=720
python asyncio_task_manipulation.py   # watch the 3 tasks interleave
```

## 📊 Expected behaviour
- In `asyncio_task_manipulation.py`, the three computations print **one step each per second**, proving they progress *together* on one thread.
- In `concurrent_futures_pooling.py`, the **ProcessPool** is fastest for this CPU-bound test, while the **ThreadPool** is no faster than sequential (GIL again — ties back to Chapter 1!).

---

## ✅ Summary
asyncio = **one thread, many cooperating coroutines, one event loop**. Brilliant for I/O-bound concurrency; not a substitute for processes when the work is CPU-bound.
