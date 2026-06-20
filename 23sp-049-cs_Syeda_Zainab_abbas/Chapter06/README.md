# 🛰️ Chapter 06 — Distributed Python

> **Topic:** Spreading work across processes and machines — Celery, Pyro4, and raw sockets

---

## 🎯 Overview
The final chapter goes fully **distributed**: work no longer runs in one program but across **separate processes and even separate computers**, coordinated over a network. Three approaches are shown, from high-level to low-level:

1. **Celery** — a distributed *task queue* (push jobs to remote workers via a message broker).
2. **Pyro4** — *Remote Method Invocation*: call an object's methods as if it were local, though it lives elsewhere.
3. **Sockets** — the raw TCP foundation everything above is built on.

> 📝 **Why is the code here `#` commented with the output written in?**
> Each example needs extra infrastructure — a **message broker** (RabbitMQ), a **Pyro name server**, or **two terminals** (server + client). So the code is preserved as comments and the **expected output is documented at the bottom** of each file.

---

## 🧠 Key Concepts

| Approach | Idea | Needs |
|----------|------|-------|
| **Celery** | Submit tasks to a queue; workers pick them up and run them. | A broker (RabbitMQ / Redis) |
| **Pyro4 (RMI)** | A *proxy* forwards your method call to a remote object. | A Pyro **name server** |
| **Sockets** | Direct byte-level send/receive over TCP. | Just Python's `socket` module |

---

## 📂 Files in this folder

### `Celery/`
| File | Role |
|------|------|
| `addTask.py` | Defines the Celery app + `add(x, y)` task. Start the worker: `celery -A addTask worker --loglevel=info` |
| `addTask_main.py` | Client: submits `add.delay(5, 5)` → result **10** runs on the worker. |

### `Pyro4/First Example/`
| File | Role |
|------|------|
| `pyro_server.py` | Exposes `welcomeMessage()` and registers it with the name server. |
| `pyro_client.py` | Looks up the object by name and calls it remotely. |

### `Pyro4/Second Example/` — a ring of servers (1 → 2 → 3 → 1)
| File | Role |
|------|------|
| `chainTopology.py` | The shared `Chain` object that forwards a message to the next server. |
| `server_chain_1.py` / `_2.py` / `_3.py` | The three ring servers. |
| `client_chain.py` | Sends `["hello"]` into server 1; result returns once the ring is closed. |

### `socket/`
| File | Role |
|------|------|
| `server.py` / `client.py` | A **time server**: client connects, receives the current time. |
| `server2.py` / `client2.py` | A **file transfer**: server streams `mytext.txt` to the client (`received.txt`). |
| `addTask.py` / `addTask_main.py` | Celery variant using the `pyamqp` broker. |

---

## ▶️ How to run (order matters!)

**Celery**
```bash
# terminal 1: start RabbitMQ broker, then the worker
celery -A addTask worker --loglevel=info
# terminal 2:
python addTask_main.py
```

**Pyro4 (first example)**
```bash
python -m Pyro4.naming      # terminal 1: name server
python pyro_server.py       # terminal 2
python pyro_client.py       # terminal 3
```

**Pyro4 chain**
```bash
python -m Pyro4.naming
python server_chain_1.py & python server_chain_2.py & python server_chain_3.py
python client_chain.py
# → ['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']
```

**Sockets**
```bash
python server.py            # terminal 1
python client.py            # terminal 2
```

## 🛠️ Setup
```bash
pip install celery pyro4
# Celery also needs a broker, e.g. RabbitMQ running on localhost
```

---

## ✅ Summary
Distribution = computation across **processes and machines**. Celery (task queue), Pyro4 (remote objects), and sockets (raw TCP) are three layers of the same idea — and together they tie off everything from threads (Ch 2) to processes (Ch 3) to message passing (Ch 4).
