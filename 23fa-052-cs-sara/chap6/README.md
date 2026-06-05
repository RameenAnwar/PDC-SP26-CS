# What is Parallel Programming?

Simple Definition: Doing many tasks at the same time instead of one after another.

| Normal Way (Sequential) | Parallel Way |
|------------------------|---------------|
| Task 1 → Task 2 → Task 3 | Task 1, Task 2, Task 3 all together |
| Takes 30 seconds | Takes 10 seconds |
| Uses 1 worker | Uses many workers |

# Three Main Concepts

1. **Celery** - Background task processing
2. **Pyro4** - Remote function calling
3. **Sockets** - Network data transfer


## 1. Celery - Task Queue

### What is it?

Celery is like a task manager. You give it work, and it finds workers to do that work in the background.
### Real-Life Analogy
You call a pizza shop ──▶ Shop takes your order ──▶ Delivery boy brings pizza
(Producer) (Broker) (Worker)
### How Celery Works
┌──────────┐ ┌──────────┐ ┌──────────┐
│ You │────▶│ Broker │────▶│ Worker │
│ (Sender) │ │ (Storage)│ │ (Doer) │
└──────────┘ └──────────┘ └──────────┘
│ │ │
│ Send task │ Store task │ Do the work
│ Get result ◄─────────────────────┘
### Key Parts

| Part | What it does | Analogy |
|------|--------------|---------|
| **Task** | The work to do | "Make a pizza" |
| **Broker** | Stores waiting tasks | Order counter |
| **Worker** | Does the actual work | Pizza maker |
| **Backend** | Stores results | Pickup counter |

### When to Use Celery

| Good For |  Not Good For |
|-------------|-----------------|
| Sending emails | Real-time responses |
| Processing images | Simple calculations |
| Generating reports | CPU-heavy tasks |
| Web scraping | Tiny quick tasks |
## Key Concept: Async
SYNC (Without Celery):
You: "Send email" → WAIT (5 seconds) → "Done" → Next work

ASYNC (With Celery):
You: "Send email" → "OK, I'll do it" → Continue other work
│
└──→ (5 seconds later) Email sent

## 2. Pyro4 - Remote Objects

### What is it?

Pyro4 lets you call functions on another computer as if they were on your own computer.

### Real-Life Analogy
 You call a friend in another city ──▶ Friend answers ──▶ Friend does task
(Client) (Phone Network) (Server)

You don't need to go there! Just call and ask.
### How Pyro4 Works
┌──────────────┐ ┌──────────────┐
│ CLIENT │ │ SERVER │
│ (Your PC) │ │ (Other PC) │
├──────────────┤ ├──────────────┤
│ │ "Calculate 5+3" │ │
│ Call ──────┼───────────────────▶│ Function │
│ │ │ runs here │
│ │ │ │
│ Result 8 │◄───────────────────│ Return 8 │
│ │ │ │
└──────────────┘ └──────────────┘
▲ ▲
│ │
└─────────────┬─────────────────────┘
│
┌───────┴───────┐
│ Name Server │
│ (Phonebook) │
└───────────────┘
### Key Parts

| Part | What it does | Analogy |
|------|--------------|---------|
| **Name Server** | Helps find servers | Phonebook / Directory |
| **Daemon** | Listens for requests | Receptionist |
| **Proxy** | Connection to remote server | Phone line |
| **@Pyro4.expose** | Makes method visible | Public phone number |

### When to Use Pyro4

| Good For |  Not Good For |
|-------------|-----------------|
| Distributed systems | Single computer apps |
| Multiple computers | Simple scripts |
| Remote control | Heavy data transfer |
| Centralized services | Real-time games |
## Key Concept: Remote Transparency
LOCAL CALL:
result = add(5, 3) # Runs on YOUR computer

REMOTE CALL (Pyro4):
result = server.add(5, 3) # Runs on ANOTHER computer
## 3. Sockets - Network Communication

### What are Sockets?

Sockets are like **phone lines** between programs. One program calls, another answers.

### Real-Life Analogy
 Call center ──▶ Agent answers ──▶ "What time is it?" ──▶ "5:30 PM"
(Client) (Server)
### How Sockets Work
┌──────────────┐ ┌──────────────┐
│ CLIENT │ │ SERVER │
├──────────────┤ ├──────────────┤
│ │ │ │
│ 1. Create │ │ 1. Create │
│ 2. Connect │───────────────────▶│ 2. Bind │
│ 3. Receive │◄───────────────────│ 3. Listen │
│ 4. Close │───────────────────▶│ 4. Accept │
│ │ │ 5. Send │
│ │ │ 6. Close │
└──────────────┘ └──────────────┘
### Key Parts

| Part | What it does | Analogy |
|------|--------------|---------|
| **Socket** | Communication endpoint | Phone device |
| **IP Address** | Computer location | Phone number |
| **Port** | Specific program | Extension number |
| **Bind** | Reserve port | Get phone line |
| **Listen** | Wait for calls | Wait for ring |
| **Accept** | Answer call | Pick up phone |
| **Connect** | Call server | Dial number |
| **Send/Recv** | Exchange data | Talk |
| **Close** | End connection | Hang up |

### When to Use Sockets

|  Good For |  Not Good For |
|-------------|-----------------|
| Simple data transfer | Complex object passing |
| File transfer | Remote procedure calls |
| Chat applications | Background tasks |
| Real-time messages | Large scale systems |
### Key Concept: Client-Server Model
CLIENT SERVER
│ │
│ "Hello" ────────────────────▶│
│ │
│ "Hi there!" ◄────────────────│
│ │
│ "Bye" ──────────────────────▶│
│ │
│ "See ya!" ◄──────────────────│
│ │

Client starts conversation

Server always waits

One server can handle many clients
##  Comparison Table

### Celery vs Pyro4 vs Sockets

| Feature | Celery | Pyro4 | Sockets |
|---------|--------|-------|---------|
| **Main Purpose** | Background tasks | Remote method calls | Data transfer |
| **Async Support** |  Yes | Yes |  No |
| **Complexity** | Medium | Medium | Low |
| **Extra Software** | Broker needed | Name server needed | None |
| **Best For** | Long tasks | Distributed computing | Simple messaging |

### When to Use What?

| If you need to... | Use... |
|-------------------|--------|
| Send emails in background | **Celery** |
| Process images without waiting | **Celery** |
| Call function on another computer | **Pyro4** |
| Create distributed system | **Pyro4** |
| Send simple message | **Sockets** |
| Transfer files | **Sockets** |
