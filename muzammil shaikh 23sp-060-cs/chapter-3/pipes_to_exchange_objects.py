from multiprocessing import Process, Pipe

def send_message(conn):
    conn.send("Hello from child process")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    p = Process(target=send_message, args=(child_conn,))

    p.start()

    print(parent_conn.recv())

    p.join()